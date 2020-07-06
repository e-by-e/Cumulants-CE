"""
Authors: B.Friman, A.Rustamov
"""

from ce_cumulants.cumulans import Cumulants

# creating the object of Cumulant

CE = Cumulants(370, 20, 0.068, 0.106)

# 370: number of baryons in 4pi
# 30: number of anti-baryons in 4pi
# 0.068: accepted protons
# 0.106: accepted anti-protons

# specifying the order of the cumulant
n = 2

# calculating
CE.process(n)

# extracting oputput information
cumNumerical = CE.get_num_values()  # numerical values
cumAnalytic = CE.get_formulas()   # analytic formulas

z = CE.get_recalculatedz()  # recalculated value of the partition function

print(f'\nrecalculated z = {z[0]:.6}\n')

print("Numerical values of cumulants ____\n")
for i in range(0, n):
    print(f'kappa_{i} = {cumNumerical[i]:.6}')

print("\nAnalytic formulas of cumulants ____\n")
for i in range(0, n):
    print(f'kappa_{i} = {cumAnalytic[i]}')
