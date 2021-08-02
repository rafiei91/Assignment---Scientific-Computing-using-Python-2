# Lorenz

This file includes the codes related to solving the ODE problem, and saves and plots the results.

The explanation regarding each code is as below:

## run

This file includes the _execute_ function that is called by the _case_ files to receive the differential equations and the initial conditions.

After receiving the differential equations and the initial conditions, the _execute_ function call the _ode_solver_ function (defined in solver) to solve the ODE problem.

Then, the outputs are given to the _saveing_ (defined in filehandling), and _plot_2D_ and _plot_3D_ (defined in plot) to save and plot the results, respectively.

## solver

This file includes the _ode_solver_ function that gets the ODEs, initial conditions, and steps details, and uses the simple Newton Euler algorithm to solve the model. 

The output is the solving results along with the related time points to them.

## filehandling

This file includes the _saveing_ function that gets the solver's results and the case number, then saves the results in hdf5 format.

## plot

This file includes two _plot_2D_ and _plot_3D_ functions that each receives solver's results and the case number, then plot and save them in 2D and 3D in pdf format.
