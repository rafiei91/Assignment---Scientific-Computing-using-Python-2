# Case

## case1 to case5

This folder contains 5 codes regarding the 5 parameter cases.

Each code includes a function defining the Lorenz attraction ode with the related parameters to the case number. This function returns the differential equations.

Then, the path to save the results is created.

Finally, the function _execute_ (defined in lorenz/run) is called and the defined ODE function, initial conditions, and the case name are given to it as its inputs.

## \__init__

This file is made to make it possible to import the _case1_ code in the test code.
