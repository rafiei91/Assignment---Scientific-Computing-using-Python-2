import sys
sys.path.append('../')
from code import funcs
import unittest
from scipy.integrate import solve_ivp
import numpy as np

start = time.time()
ri = 0 # real index
M_size = 100 # number of pixcels
r_s = -2 # start point (real)
r_e = 1 # end point (real)
i_s = -1.5 # start point (imagenary)
i_e = 1.5 # end point (imagenary)

def Mf_t(r, i):
  c = complex(r, i)
  I = 200
  z = [complex(0, 0) for i in range(I+1) ]
  T = 2
  for i in range(I):
    z[i+1] = (z[i] ** 2) + c
    if abs(z[i+1]) > T:
        return (i+1)/I
  return 1

class TestMethod(unittest.TestCase):

    def test_naive(self):
        
        M_out = np.zeros((M_size,M_size))
        for r in np.arange (r_s, r_e, (r_e - r_s) / M_size):
            ii = 0 # imagenary index
            for i in np.arange (i_s, i_e, (i_e - i_s) / M_size):
                M_out_t[ri, ii] = Mf_t (r, i)
                M_out[ri, ii] = funcs.Mf (r, i)
                ii += 1
            ri += 1
        
       self.assertEqual(M_out_t, M_out)
