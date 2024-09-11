#!/usr/bin/env python

import rospy
import os
import sys
sys.path.remove('/opt/ros/{}/lib/python2.7/dist-packages'.format(os.getenv('ROS_DISTRO')))
sys.path.append('/opt/ros/{}/lib/python3/dist-packages'.format(os.getenv('ROS_DISTRO')))

import PyKDL
from cv_bridge import CvBridge
