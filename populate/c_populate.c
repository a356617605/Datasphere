#include <stdio.h>
#include <math.h>
#include "c_populate.h"
#include <sys/types.h>
#include <unistd.h>

void init_ds(double * data_sphere_points,
	     double * ZZ, double * YY, double * XX,
	     size_t Nz, size_t Ny, size_t Nx,
	     double * voxel){

  pid_t pid = getpid();
  printf("\nPID %lun ENTERED PT_INTERP FUNCTION\n", pid);

  if(!data_sphere_points){ printf("data_sphere_points pointer is null");return;}
  if(!ZZ){ printf("ZZ pointer is null");return;}
  if(!YY){ printf("YY pointer is null");return;}
  if(!XX){ printf("XX pointer is null");return;}
  if(!voxel){ printf("voxel pointer is null");return;}

  double hf_voxel=voxel[0]/2;
  printf("\nhf voxel = %f \n", hf_voxel)

  size_t I,J,K;
  for (size_t i=0;i<Nx;++i){
    I=i*Ny*Nz*3;
    for (size_t j=0;j<Ny;++j){
      J=j*Nz*3;
      printf("\nENTERED for loop i=%zu j=%zu\n",i,j);
      #pragma omp parallel for shared(data_sphere_points, ZZ,YY,XX, hf_voxel, I,J, Nz)
      for (size_t k=0; k<Nz; ++k){
	printf("\n  ENTERED for loop I=%zu J=%zu k=%zu\n",I,J,k);
	K=k*3;
	data_sphere_points[I+J+K   ] = XX[i] + hf_voxel;
	data_sphere_points[I+J+K +1] = YY[j] + hf_voxel;
	data_sphere_points[I+J+K +2] = ZZ[k] + hf_voxel;
      }
    }
  }
  printf("\nPID %lun EXITING PT_INTERP FUNCTION\n", pid);

}
