from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,#'0.1',
    install_requires=[
        'cloudpickle',
        'numpy<2',
        'opencv-python~=3.4',
        # 'gym[atari,box2d,classic_control]~=0.26',
        'gym@git+https://github.com/mikesongming/gym.git#egg=gym[all]',
        'ipython',
        'joblib',
        'matplotlib',
        # 'mpi4py',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn',
        # 'tensorflow>=1.8.0,<2.0',
        'torch',
        'tqdm'
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
