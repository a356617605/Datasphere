import numpy as np
from time import time
from datasphere.populate import init_data_sphere
import getpass, os, sys

def test_populate_init_data_sphere():
    
    Nx=3
    Ny=5
    Nz=7
    ZZ=np.arange(Nz, dtype=np.float64)
    YY=np.arange(Ny, dtype=np.float64)
    XX=np.arange(Nx, dtype=np.float64)

    print(XX,YY,ZZ)
    voxel_size=np.array([1.], dtype=np.float64)

    # (1) compute the result using our C extension
    t0 = time()
    out = init_data_sphere(ZZ, YY, XX,voxel_size)
    dt0 = time() - t0
    print("XX={}".format(XX))
    print("XX shape={}".format(XX.shape))
    print("out={}".format(out))
    print("out.shape={}".format(out.shape))


# MAIN
if __name__ == "__main__":
    test_populate_init_data_sphere()





