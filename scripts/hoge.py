#!/usr/bin/env python

import os
import sys
print(f"original PYTHONPATH:{sys.path}")
sys.path.remove('/opt/ros/{}/lib/python2.7/dist-packages'.format(os.getenv('ROS_DISTRO')))
sys.path.append('/opt/ros/{}/lib/python3/dist-packages'.format(os.getenv('ROS_DISTRO')))
print(f"modified PYTHONPATH:{sys.path}")

import PyKDL
from cv_bridge import CvBridge
