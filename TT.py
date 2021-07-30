from multiprocessing import Process, Lock, Pool
import numpy as np
import cmath
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from numba import jit, njit, prange
from numba import vectorize
import multiprocessing as mp

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

ri = 0 # real index
M_size = 500 # number of pixcels
r_s = -2 # start point (real)
r_e = 1 # end point (real)
i_s = -1.5 # start point (imagenary)
i_e = 1.5 # end point (imagenary)

start = time.time()
M_out = np.zeros((M_size,M_size))
for r in np.arange (r_s, r_e, (r_e - r_s) / M_size):
    ii = 0 # imagenary index
    for i in np.arange (i_s, i_e, (i_e - i_s) / M_size):
        M_out[ri, ii] = Mf (r, i)
        ii += 1
    ri += 1
M_out = np.transpose(M_out)
end = time.time()
Exe_time = end - start
print("simple: {0}".format(Exe_time))

start = time.time()
ri = 0 # real index
M_size = 500 # number of pixcels
r_s = -2 # start point (real)
r_e = 1 # end point (real)
i_s = -1.5 # start point (imagenary)
i_e = 1.5 # end point (imagenary)

M_out_p = np.zeros((M_size,M_size))
for r in np.arange (r_s, r_e, (r_e - r_s) / M_size):
    ii = 0 # imagenary index
    for i in np.arange (i_s, i_e, (i_e - i_s) / M_size):
        M_out_p[ri, ii] = Mf_p (r, i)
        ii += 1
    ri += 1
M_out_p = np.transpose(M_out_p)
end = time.time()
Exe_time = end - start
print("parallel: {0}".format(Exe_time))

start = time.time()
ri = 0 # real index
M_size = 500 # number of pixcels
r_s = -2 # start point (real)
r_e = 1 # end point (real)
i_s = -1.5 # start point (imagenary)
i_e = 1.5 # end point (imagenary)

M_out_v = np.zeros((M_size,M_size))
for r in np.arange (r_s, r_e, (r_e - r_s) / M_size):
    #ii = 0 # imagenary index
    M_out_v[ri, :] = Mf_v (r, np.arange (i_s, i_e, (i_e - i_s) / M_size))
    ri += 1
M_out_v = np.transpose(M_out_v)
end = time.time()
Exe_time = end - start
print("vectorized: {0}".format(Exe_time))

ri = 0 # real index
M_size = 500 # number of pixcels
r_s = -2 # start point (real)
r_e = 1 # end point (real)
i_s = -1.5 # start point (imagenary)
i_e = 1.5 # end point (imagenary)


if __name__ == '__main__': # We have to use this to make it work in this interactive interpreter
    M_out_p = np.zeros((M_size,M_size))
    arr1 = np.arange (r_s, r_e, (r_e - r_s) / M_size)
    arr2 = np.arange (i_s, i_e, (i_e - i_s) / M_size)
    aa = list(product(arr1, arr2))
    
    start = time.time()
    pool = Pool()
    print(pool)
    M_out_p = pool.map(Mf_m, aa)
    pool.close()
    pool.join()
    end = time.time()
    
    M_out_m1 = np.transpose(M_out_p)
    M_out_m = np.reshape(M_out_m1, (M_size, M_size))
    M_out_m = np.transpose(M_out_m)
    
    Exe_time = end - start
    print("Multiprocessing: {0}".format(Exe_time))
