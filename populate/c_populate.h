#include <stddef.h>

void init_ds(double *, // data_sphere_points: empty array
	     double *, double *, double *, // ZZ,YY,XX
	     size_t, size_t, size_t, // sizes of ZZ,YY,ZZ
	     double * // voxel. (1,) ndarray
	     );
