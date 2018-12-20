#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['rviz_visualization'],
   package_dir={'rviz_visualization': 'src/rviz_visualization'}
)

setup(**d)
