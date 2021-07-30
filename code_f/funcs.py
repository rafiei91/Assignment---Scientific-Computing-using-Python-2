"""
The Mandelbrot set is coded here in 4 different implementation style. Each function recieves a complex input and return the belongness index.
"""

import cmath
from numba import jit, njit, vectorize

# Naive implementation
def Mf(r, i):
  c = complex(r, i)
  I = 200
  z = [complex(0, 0) for i in range(I+1) ]
  T = 2
  for i in range(I):
    z[i+1] = (z[i] ** 2) + c
    if abs(z[i+1]) > T:
        return (i+1)/I
  return 1

# Parallel Implementation
@njit(parallel=True)
def Mf_p(r, i):
  c = complex(r, i)
  I = 200
  z = [ complex(0, 0) for i in range(I+1) ]
  T = 2
  for i in range(I):
    z[i+1] = (z[i] ** 2) + c
    if abs(z[i+1]) > T:
        return (i+1)/I
  return 1

# Vectorized Implementation
@vectorize(['float32(float32, float32)',
            'float64(float64, float64)'])
def Mf_v(r, i):
  c = complex(r, i)
  I = 200
  z = [complex(0, 0) for i in range(I+1) ]
  T = 2
  for i in range(I):
    z[i+1] = (z[i] ** 2) + c
    if abs(z[i+1]) > T:
        return (i+1)/I
  return 1

# Multiprocessing Implementation
def Mf_m(r):
  c = complex(r[0], r[1])
  I = 200
  z = [complex(0, 0) for i in range(I+1) ]
  T = 2
  for i in range(I):
    z[i+1] = (z[i] ** 2) + c
    if abs(z[i+1]) > T:
        return (i+1)/I
  return 1
