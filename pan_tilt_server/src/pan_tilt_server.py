#!/usr/bin/env python3

from __future__ import print_function

import sys
import time
import rospy

import ui2 as ui
from PyQt5 import QtCore, QtGui, QtWidgets
from pan_tilt_srv.srv import TurnPanTilt, TurnPanTiltResponse

def cmd_pan_tilt(req):
    # degree2radians
    pan_angle, tilt_angle = controller.degee2rev(req.pan), controller.degee2rev(req.tilt)
    
    # check pan, tilt limits
    pan_val, tilt_val = controller.l_p(pan_angle), controller.l_t(tilt_angle)

    # cmd pan
    controller.cmd("pp{}".format(pan_val))
    while(controller.cmd("pp")[-1] != pan_val):
        print("pp:", controller.rev2degee(controller.cmd("pp")[-1]))
    time.sleep(0.5)
    print("final pp:", controller.rev2degee(controller.cmd("pp")[-1]))
    print("-------------------------------------")

    # cmd tilt
    controller.cmd("tp{}".format(tilt_val))
    while(controller.cmd("tp")[-1] != tilt_val):
        print("tp:", controller.rev2degee(controller.cmd("tp")[-1]))
    time.sleep(0.5)
    print("final tp:", controller.rev2degee(controller.cmd("tp")[-1]))

    return True

def turn_pan_tilt_server():
    rospy.init_node('turn_pan_tilt_server')
    s = rospy.Service('turn_pan_tilt', TurnPanTilt, cmd_pan_tilt)
    print("Ready to turn pan_tilt platform.")
    rospy.spin()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    controller = ui.Ui_MainWindow()
    controller.setupUi(MainWindow) #initial
    turn_pan_tilt_server()
