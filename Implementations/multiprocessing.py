import numpy as np
import time
from itertools import product
from multiprocessing import Process, Pool
import sys
sys.path.append('../')
import os
from code.funcs import Mf_m

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
    M_out_p = pool.map(Mf_m, aa)
    pool.close()
    pool.join()
    end = time.time()
    
    M_out_m1 = np.transpose(M_out_p)
    M_out_m = np.reshape(M_out_m1, (M_size, M_size))
    M_out_m = np.transpose(M_out_m)

print("The execution time for the Multiprocessing version is {} seconds.".format(end - start))