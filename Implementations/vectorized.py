import numpy as np
import time
import sys
sys.path.append('../')
import os
from code.funcs import Mf_v
import h5py

start = time.time()
ri = 0 # real index
M_size = 1000 # number of pixcels
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

print("The execution time for the Vectorized version is {} seconds.".format(end - start))

if os.path.exists('vectorized') is False:
    os.mkdir('vectorized')

f = h5py.File("vectorized/" + 'vectorized.hdf5', 'w')
f.create_dataset('RND', data=M_out_v)
f.close()
