import os
import numpy as np
from setuptools import setup, Extension, Command


# assuming gcc, set (aggressive) optimization flags, to be appended to the default compile line
c_flags = []
#c_flags.append("-fsanitize=address")
#c_flags.append("-g")
#c_flags.append("-lasan")
c_flags.append("-O3")
# c_flags.append("-ffast-math")
#c_flags.append("-lgomp")
c_flags.append("-fopenmp")
c_flags.append("-march=native")
c_flags.append("-fPIC")
c_flags.append("-fopt-info")
c_flags.append("-std=c99")

# include directories
include_dirs = []
include_dirs.append(np.get_include())


# extra link flags are possible as well; we leave them empty here
ld_flags = []


ext_modules = []
ext_modules.append(
    Extension("datasphere.populate",
              sources=["populate/populate.pyx", "populate/c_populate.c"],
              extra_compile_args=c_flags,
              extra_link_args=ld_flags,
              include_dirs=[np.get_include()]
              )
)


class CleanCommand(Command):
    """Enable `python setup.py clean` to tidy up properly."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # better: use plain Python instead of UNIX commands
        os.system('rm -vrf build')
        os.system('rm -vrf dist')
        os.system('rm -vrf populate/populate.c')
        os.system('rm -vRf populate/__pycache__')
        os.system('rm -vrf populate.egg-info')
        os.system("find populate -name '*.so' -delete -print")
        os.system("find populate -name '*.pyc' -delete -print")


setup(name="interp",
      ext_modules=ext_modules,
      cmdclass={'clean': CleanCommand}
      )
