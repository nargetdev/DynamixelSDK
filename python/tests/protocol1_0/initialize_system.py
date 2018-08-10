#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Ping Example      *********
#
#
# Available Dynamixel model on this example : All models using Protocol 1.0
# This example is tested with a Dynamixel MX-28, and an USB2DYNAMIXEL
# Be sure that Dynamixel MX properties are already set as %% ID : 1 / Baudnum : 34 (Baudrate : 57600)
#

import os
import time

import LXMoCo

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                 # Uses Dynamixel SDK library
from LXMoCo import *                 # Uses Dynamixel SDK library

# Protocol version
PROTOCOL_VERSION        = 1.0               # See which protocol version is used in the Dynamixel

BAUDRATE                = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME              = '/dev/ttyACM0'    # Check which port is being used on your controller
                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
PING_RANGE = 8

# Our LXMoCo instance
moco = LXMoCo()

moco.network_discovery()

# moco.command_wheel_mode(2)
moco.keyboard_interface(2)



# Close port
# portHandler.closePort()
