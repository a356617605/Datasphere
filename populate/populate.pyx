#!python
# cython: embedsignature=True, binding=True

# Cython interface to the <c_populate.{c,h}> code.
# For more detailed explanations please confer
# http://cython.readthedocs.io/en/latest/src/tutorial/numpy.html

import numpy as np
cimport numpy as np

cdef extern from "c_populate.h":
    void init_ds(double *,
                 double *, double *, double *,
                 size_t, size_t, size_t,
                 double * );

    
def init_data_sphere(np.ndarray ZZ, np.ndarray YY, np.ndarray XX,
                     np.ndarray voxel_size):
    """Initialize data sphere np.array([data_X+voxel/2, data_Y+voxel/2, data_Z+voxel/2])

    Keyword arguments:
    ZZ -- (Nz, ) ndarray with point grid on the Z axis.
    YY -- (Ny, ) ndarray with point grid on the Y axis.
    XX -- (Nx, ) ndarray with point grid on the Z axis.
    voxel_size -- (1, ) ndarray with voxel size in nm.
    """
    assert ZZ.dtype == np.float64 and \
        YY.dtype == np.float64 and \
        XX.dtype == np.float64 and \
        voxel_size.dtype == np.float64, \
        "Input np arrays dtype not supported"
    assert ZZ.ndim == 1  and \
        YY.ndim == 1  and \
        XX.ndim == 1  and \
        voxel_size.ndim == 1,  \
        "input ndim not supported"

    cdef size_t Nx=XX.shape[0], Ny=YY.shape[0], Nz=ZZ.shape[0]
    cdef np.ndarray data_sphere_points=np.empty(shape=(XX.shape[0]*YY.shape[0]*ZZ.shape[0],3), dtype=ZZ.dtype)

    init_ds(<double*>data_sphere_points.data,
            <double*>ZZ.data, <double*>YY.data, <double*>XX.data,
            <size_t>Nz, <size_t>Ny, <size_t>Nx,
            <double*>voxel_size.data)

    return data_sphere_points
