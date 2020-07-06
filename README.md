Bengt Friman, Anar Rustamov


## Python package for claculation of net-baryon (net-protons) cumulants

## The package provides both, analytical and numerical results

### The formalism and analytic formulas used in the package are based on the publication

- ### *Peter Braun-Munzinger, Bengt Friman, Krzysztof Redlich, Anar Rustamov, Johanna Stachel*
       Relativistic nuclear collisions: Establishing the non-critical baseline for fluctuation measurements

### *Citation of the above publication is mandatory for the results obtained with this* 
### *package and/or for developments based on this package*

## Users guide
The fast and efficiant way of running the program is to use the provided graphical interface
This is dove via the command:

### python example_GUI.py

after this a Graphycal User Interface is opened

The user should provide the following input information:

- NB: number of baryons in 4pi  (the default value is 370)
- NBar: number of anti-baryons in 4pi (the default value is 20)
- pB: accepted protons (the default value is 0.068)
- pBar: accepted anti-protons (the default value is 0.106)

The cumulant order can be selected in the field **cumulant order** (the default value is 2)

After pressing the **calculate** button the program first recalculates the partition function **z**, and uses it for 
estimating numerical values of cumulants, which are then printed.

If the checkbox **print analytic formulas** is selected the analytical formulas are also printed below the numerical values

The second option is to use the provided package directly in the users code
The example is provided in the **example.py** file and futhter documentation therein. 

### python example.py

## Needed python modules/libraries/bindings

- sympy
- scipy
- numpy
- PyQt5

## Contact infomration

for additional details contact

- b.friman@gsi.de
- a.rustamov@cern.ch, a.rustamov@gsi.de
