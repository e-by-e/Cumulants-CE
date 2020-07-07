Bengt Friman, Anar Rustamov


## A Python package for computing net-baryon (net-proton) cumulants.

## The package provides both, analytical and numerical results.

### The formalism and analytic formulas used in the package are based on the publication

- ### *Peter Braun-Munzinger, Bengt Friman, Krzysztof Redlich, Anar Rustamov, Johanna Stachel*
  #### Relativistic nuclear collisions: Establishing the non-critical baseline for fluctuation measurements.
  #### arXiv:2007.02463 [nucl-th]
       
### *If you use the code to produce results for a publication,* 
### *we ask you to be fair and cite the above paper!*

## Users guide
A fast and efficient way to run the code, is to use the graphical interface,
which is started with the command:

### python example_GUI.py

Subsequently a Graphical User Interface is opened.

The user should provide the following input information:

- NB: number of baryons in 4pi  (the default value is 370),
- NBar: number of anti-baryons in 4pi (the default value is 20),
- pB: probability for accepting protons (the default value is 0.068),
- pBar: probability for accepting anti-protons (the default value is 0.106),

The maximum cumulant order can be selected in the field **cumulant order** (the default value is 2, 
the higher the maximum order is, the longer the code runs).

After pressing the **calculate** button the program first recalculates the partition function **z**, and uses it for 
computing the numerical values of the cumulants, which are then printed.

If the checkbox **print analytic formulas** is selected the analytical formulas are also printed below the numerical values.
If the checkbox **Generate .cc file** is selected, a dedicated  **C++** code  **ce_cumulants.cc**, which contains 
functions for computing the cumulants, is created and saved.

The second option is to implement the provided package directly in your own code.
The example is provided in the **example.py** file and furhter documentation therein. This example code can be run as:

### python example.py

## Python modules/libraries/bindings needed 

- sympy
- scipy
- numpy
- PyQt5

## Contact information

- b.friman@gsi.de
- a.rustamov@cern.ch, a.rustamov@gsi.de
