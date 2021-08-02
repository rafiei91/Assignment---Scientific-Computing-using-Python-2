import numpy as np
import time
import sys
sys.path.append('../')
import os
from code_f.funcs import Mf_p
import h5py
import matplotlib.pyplot as plt
import matplotlib.cm as cm

start = time.time()
ri = 0 # real index
M_size = 1000 # number of pixcels
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
print("The execution time for the Parallel version is {} seconds.".format(end - start))

if os.path.exists('parallel') is False:
    os.mkdir('parallel')

f = h5py.File("parallel/" + 'parallel.hdf5', 'w')
f.create_dataset('RND', data=M_out_p)
f.close()

fig, ax = plt.subplots(figsize=(20, 20))
im = ax.imshow(M_out_p, cmap=cm.hot, extent=[-2, 1, -1.5, 1.5])
plt.savefig("parallel/" + 'parallel.png')
