# code_f

This file includes the code related to defining the functions to assess if the input belongs to the Mandelbrot set.

The explanation regarding code is as below:

## funcs

This file includes the functions that is called by the implementation codes to receive a complex point and calculate the index of belonging to the Mandelbrot set.

The defined functions here are:

- _Mf_ : for Naive version
- _Mf_p_ : for Parallel version
- _Mf_v_ : for Vectorized version
- _Mf_m_ : for Multi-processing version

## \__init__

This file is made to make it possible to import the _Mf_ function in the test code.
