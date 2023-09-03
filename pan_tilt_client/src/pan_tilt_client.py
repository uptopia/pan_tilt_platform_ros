#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from pan_tilt_srv.srv import *

def turn_pan_tilt_client(pan_deg, tilt_deg):
    rospy.wait_for_service('turn_pan_tilt')
    try:
        turn_pan_tilt = rospy.ServiceProxy('turn_pan_tilt', TurnPanTilt)
        res = turn_pan_tilt(pan_deg, tilt_deg)
        return res.reached
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [pan_absolute_degree tilt_absolute_degree]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        pan_absolute_deg = int(sys.argv[1])
        tilt_absolute_deg = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting [pan_absolute_degree tilt_absolute_degree]=%f, %f"%(pan_absolute_deg, tilt_absolute_deg))
    print("Reached requested angle: %r"%(turn_pan_tilt_client(pan_absolute_deg, tilt_absolute_deg)))