from __future__ import print_function

import logging
import time
from datetime import datetime

from dronekit import VehicleMode

from guidance import Vant

today = f'{datetime.now().date()}_{datetime.now().hour}_{datetime.now().minute}'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=f'square_test_{today}.log', encoding='utf-8', level=logging.DEBUG)

vehicle = Vant()

"""=====================================TEST CODE================================================================"""

print("SQUARE path using SET_POSITION_TARGET_LOCAL_NED and position parameters")
logging.info("SQUARE path using SET_POSITION_TARGET_LOCAL_NED and position parameters")
# Arm and take off to altitude of 2 meters
vehicle.arm_and_takeoff()

print("Set groundspeed to 1m/s.")
logging.info("Set groundspeed to 1m/s.")

# Going to first point
print("Going to first point")
logging.info("Going to first point")
vehicle.goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
vehicle.condition_yaw(90, True)
time.sleep(10)

# Going to second point
print("Going to second point")
logging.info("Going to second point")
vehicle.goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
vehicle.condition_yaw(90, True)
time.sleep(10)

# Going to third point
print("Going to third point")
logging.info("Going to third point")
vehicle.goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
vehicle.condition_yaw(90, True)
time.sleep(10)

# Going to fourth point
print("Going to fourth point")
logging.info("Going to fourth point")
vehicle.goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
vehicle.condition_yaw(90, True)
time.sleep(10)

# TEST FINISHED PREPARING TO LAND
print("TEST FINISHED PREPARING TO LAND !")
logging.info("TEST FINISHED PREPARING TO LAND !")
print("Setting LAND mode...")
logging.info("Setting LAND mode...")
vehicle.mode = VehicleMode("LAND")
