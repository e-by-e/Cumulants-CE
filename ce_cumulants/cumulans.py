"""
Authors: B.Friman, A.Rustamov

The formalism and analytic formulas used in the package are based on the publication:

Peter Braun-Munzinger, Bengt Friman, Krzysztof Redlich, Anar Rustamov, Johanna Stachel
Relativistic nuclear collisions: Establishing the non-critical baseline for fluctuation measurements.

arXiv:2007.02463 [nucl-th]

If you use the code to produce results for a publication, we ask you to be fair and cite the above paper!

"""
from sympy import Function, symbols, simplify, expand_func, polylog, diff, Derivative, bell, Sum, Indexed, lambdify
from scipy import optimize, special
import numpy as np
from sympy.printing.cxxcode import cxxcode


class Cumulants:
    def __init__(self, NBx, NBbx, px, pbx):
        self.NBx = NBx
        self.NBbx = NBbx
        self.zr = 1.
        self.px = px
        self.pbx = pbx
        self.Bx = NBx - NBbx
        self.nc = 1
        self.S = Function('S')
        self.P = Function('P')
        self.Q = Function('Q')
        self.W = Function('W')
        self.n = symbols('n', integer=True)
        self.i = symbols('i', integer=True)
        self.j = symbols('j', integer=True)
        self.k = symbols('k', integer=True)
        self.B = symbols('B', integer=True)
        self.p, self.pb, self.NBc, self.NBbc, self.z, self.t, self.u, self.y = symbols(
            'pB, pBar, NB, NBar, z, t, u, y')
        self.c = {}
        self.cb = {}
        self.kminus = []
        self.bellkminus = []
        self.r = []
        self.fn = []
        self.ftilde = []
        self.kappax = []

    def cx(self, nmax):
        self.c[0] = self.p
        for i in range(2, nmax):
            self.c[i - 1] = (-1) ** (i - 1) * simplify(expand_func(polylog(1 - i, 1 - 1 / self.p)))

    def cbx(self, nmax):
        self.cb[0] = self.pb
        for i in range(2, nmax):
            self.cb[i - 1] = simplify(expand_func(polylog(1 - i, 1 - 1 / self.pb)))

    def kappaab(self, n):
        L = (self.NBc - self.NBbc) / 2 * (self.c[n - 1] + self.cb[n - 1])
        return L

    def kminusx(self, nmax):
        L = {}
        for n in range(0, nmax - 1):
            L[n] = (self.c[n] - self.cb[n]) / 2
        return L

    def ftildex(self, nmax):
        Q = self.Q
        z = self.z
        W = self.W
        S = self.S
        DS = 4 * Q(z) / z
        DQ = 2 * (Q(z) - W(z)) / z
        DW = 2 * (2 * Q(z) * Q(z) - S(z) * W(z)) / z
        L = {0: S(z)}
        if nmax == 2:
            return L
        elif nmax > 2:
            for i in range(0, nmax - 2):
                Lx = diff(L[i], z)
                L[i + 1] = simplify(
                    Lx.subs({Derivative(S(z), z): DS, Derivative(Q(z), z): DQ, Derivative(W(z), z): DW}))
        return L

    def fnx(self, nmax):
        z = self.z
        L = [self.ftilde[0]]
        if nmax == 2:
            return L
        elif nmax > 2:
            for i in range(1, nmax - 1):
                L.extend([simplify(z ** i * self.ftilde[i] - i * L[i - 1])])
        return L

    def bellyn(self, nmax):
        Lbell = [[0] * nmax for i in range(nmax)]
        Lbell[0][0] = 0
        for n in range(1, nmax):
            for k in range(1, n + 1):
                Lbell[n][k] = bell(n, k, self.kminus)
        return Lbell

    def rx(self, nmax):
        i = self.i
        L3 = []
        Lbell = [0, self.bellkminus[1][1]]
        if nmax == 2:
            return Lbell
        for n in range(2, nmax):
            for k in range(1, n + 1):
                L3.extend([self.bellkminus[n][k]])
            L1 = Sum(Indexed('y', i), (i, 0, n - 1))
            L12 = lambdify(self.y, L1)
            Lbell.extend([simplify(L12(L3))])
            L3 = []
        return Lbell

    def kappac(self, n):
        fn = self.fn
        r = self.r
        z = self.z
        y = self.y
        W = self.W
        Q = self.Q
        S = self.S
        NBc = self.NBc
        NBbc = self.NBbc
        j = self.j
        L1 = [fn[0] * bell(n, 1, (r))]
        for k in range(2, n + 1):
            L1.extend([fn[k - 1] * bell(n, k, r)])
        L2 = Sum(Indexed('y', j), (j, 0, n - 1))
        L22 = lambdify(y, L2)
        L3 = L22(L1)
        L4 = L3.subs({W(z): Q(z) * S(z) - NBc * NBbc})
        L5 = L4.subs({S(z): NBc + NBbc, Q(z): z*z - NBc * NBbc})
        return L5

    def kappa(self, n):
        L = self.kappaab(n) + self.kappac(n)
        return L

    def process(self, nc):
        self.nc = nc
        self.cx(nc + 1)
        self.cbx(nc + 1)
        self.kminus = self.kminusx(nc + 1)
        self.bellkminus = self.bellyn(nc + 1)
        self.r = self.rx(nc + 1)[1:nc + 1]
        self.ftilde = self.ftildex(nc + 1)
        self.fn = self.fnx(nc + 1)
        for n in range(1, nc + 1):
            self.kappax.extend([self.kappa(n)])

    def get_num_values(self, isprint=0):
        nc = self.nc
        NBx, NBbx = self.NBx, self.NBbx
        Bx = self.Bx

        def candensb(z, B):
            Ba = abs(B)
            if z < 0.1 * Ba:
                bd = (max(B, 0) + z ** 2 / (Ba + 1) - z ** 4 / ((Ba + 1) ** 2 * (Ba + 2))
                      + 2 * z ** 6 / ((Ba + 1) ** 3 * (Ba + 2) * (Ba + 3))
                      - (11 + 5 * Ba) * z ** 8 / ((Ba + 1) ** 4 * (Ba + 2) ** 2 * (Ba + 3) * (Ba + 4))
                      + 2 * (19 + 7 * Ba) * z ** 10 / ((Ba + 1) ** 5 * (Ba + 2) ** 2 * (Ba + 3) * (Ba + 4) * (Ba + 5)))
                return bd
            bd = z * special.ive(B - 1, 2 * z) / special.ive(B, 2 * z)
            return bd

        def candensab(z, B):
            Ba = abs(B)
            if z < 0.1 * Ba:
                abd = (max(-B, 0) + z ** 2 / (Ba + 1) - z ** 4 / ((Ba + 1) ** 2 * (Ba + 2))
                       + 2 * z ** 6 / ((Ba + 1) ** 3 * (Ba + 2) * (Ba + 3))
                       - (11 + 5 * Ba) * z ** 8 / ((Ba + 1) ** 4 * (Ba + 2) ** 2 * (Ba + 3) * (Ba + 4))
                       + 2 * (19 + 7 * Ba) * z ** 10 / ((Ba + 1) ** 5 * (Ba + 2) ** 2 * (Ba + 3) * (Ba + 4) * (Ba + 5)))
                return abd
            abd = z * special.ive(B + 1, 2 * z) / special.ive(B, 2 * z)
            return abd

        def func(x):
            L = np.float(candensb(x, Bx) - NBx)
            return L

        zx0 = np.sqrt(NBx * NBbx)
        zx = np.asscalar(optimize.fsolve(func, zx0))
        self.zr = zx
        NBcx = np.asscalar(candensb(zx, Bx))
        NBbcx = np.asscalar(candensab(zx, Bx))
        px, pbx = self.px, self.pbx
        kappax_num = {}
        for i in range(0, nc):
            kappax_num[i] = self.kappax[i].subs(
                {self.NBc: NBcx, self.NBbc: NBbcx, self.z: zx, self.p: px, self.pb: pbx})
            if isprint:
                print(f'kappa_{i+1} = {kappax_num[i]} \n')
        return kappax_num

    def get_formulas(self, isprint=0):
        if isprint:
            for i in range(0, self.nc):
                print(f'kappa_{i+1} = {cxxcode(self.kappax[i])} \n')
        kappaxcc = {}
        for i in range (0, self.nc):
            kappaxcc[i] = cxxcode(self.kappax[i])
        return kappaxcc

    def get_recalculatedz(self):
        return self.zr
