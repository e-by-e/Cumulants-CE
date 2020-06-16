"""
Authors: B.Friman, A.Rustamov
"""

from ce_cumulants.cumulans import Cumulants

# creating the object od Cumulant
a = Cumulants(800, 800, 0.03, 0.03)
# computing nth order cumulant
n = 3
a.process(n)
a.get_num_values(1)
#a.get_formulas(1)

