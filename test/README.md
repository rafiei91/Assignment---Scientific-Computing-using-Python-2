# test

This file uses _unittest_ method to test the code.

The testing procedure is done on the Naive version.

The output of two functions are compared:

1. the Mf function that was defined in /code_f/funcs , that is called here;
2. the Mf_t function that is defined in the test code.

And then, with the same process that has been done in the "naive" code, is done in testing phase. Just for each complex point, they have been sent for both Mf and Mf_t functions.
```
- M_out_t[ri, ii] = Mf_t (r, i)
- M_out[ri, ii] = code_f.funcs.Mf (r, i)
```

Finally, the output of both are compared by:
```
assert np.allclose(M_out_t, M_out)
```
