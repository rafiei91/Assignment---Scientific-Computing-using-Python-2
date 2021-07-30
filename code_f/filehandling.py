import h5py

def saveing(file, case): # hdf5 file saving

    f = h5py.File(case + "/" + case + '.hdf5', 'w')
    f.create_dataset('RND', data=file)
    f.close()
