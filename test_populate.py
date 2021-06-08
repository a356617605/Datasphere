#!/usr/bin/env python

import numpy as np
from time import time
from datasphere.populate import init_data_sphere
import getpass, os, sys

#pt_interpolate=pti

def test_populate_init_data_sphere():
    
    Nx=2
    Ny=2
    Nz=2
    ZZ=np.arange(Nz, dtype=np.float64)
    YY=np.arange(Ny, dtype=np.float64)
    XX=np.arange(Nx, dtype=np.float64)
    
    voxel_size=np.array([1.], dtype=np.float64)

    # (1) compute the result using our C extension
    t0 = time()
    out = init_data_sphere(ZZ, YY, XX,voxel)
    dt0 = time() - t0
    print("XX={}".format(XX))
    print("XX shape={}".format(XX.shape))
    print("out={}".format(out))
    print("out.shape={}".format(out.shape))


    # (3) compare both the results, be careful with NumPy temporary arrays
    #try:
    #    assert(np.allclose(out, out_sci))
    #except:
    #    raise
    #else:
    #    print("OK! t(C)=%f, t(NumPy)=%f" % (dt0, dt1), flush=True)

# MAIN
if __name__ == "__main__":
    test_populate_init_data_sphere()





