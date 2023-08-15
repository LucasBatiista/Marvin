from __future__ import print_function

import logging
import time
from datetime import datetime
from constants import PIXHAWK_ADDRESS
from dronekit import connect, VehicleMode
from pymavlink import mavutil

today = f'{datetime.now().date()}_{datetime.now().hour}_{datetime.now().minute}'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=f'square_test_{today}.log', encoding='utf-8', level=logging.DEBUG)

vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)


def arm_and_takeoff(altitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    logging.info("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        logging.info(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    logging.info("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        logging.info(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    logging.info("Taking off!")
    vehicle.simple_takeoff(altitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        logging.info(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= altitude * 0.95:  # Trigger just below target alt.
            print("Reached target altitude")
            logging.info("Reached target altitude")
            break
        time.sleep(1)


def condition_yaw(heading, relative=False):
    """
    Send MAV_CMD_CONDITION_YAW message to point vehicle at a specified heading (in degrees).

    This method sets an absolute heading by default, but you can set the `relative` parameter
    to `True` to set yaw relative to the current yaw heading.

    By default the yaw of the vehicle will follow the direction of travel. After setting
    the yaw using this function there is no way to return to the default yaw "follow direction
    of travel" behaviour (https://github.com/diydrones/ardupilot/issues/2427)

    For more information see:
    http://copter.ardupilot.com/wiki/common-mavlink-mission-command-messages-mav_cmd/#mav_cmd_condition_yaw
    """
    if relative:
        is_relative = 1  # yaw relative to direction of travel
    else:
        is_relative = 0  # yaw is an absolute angle
    # create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW,  # command
        0,  # confirmation
        heading,  # param 1, yaw in degrees
        0,  # param 2, yaw speed deg/s
        1,  # param 3, direction -1 ccw, 1 cw
        is_relative,  # param 4, relative offset 1, absolute angle 0
        0, 0, 0)  # param 5 ~ 7 not used
    # send command to vehicle
    vehicle.send_mavlink(msg)


def goto_position_target_local_ned(north, east, down):
    """
    Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified
    location in the North, East, Down frame.

    It is important to remember that in this frame, positive altitudes are entered as negative
    "Down" values. So if down is "10", this will be 10 metres below the home altitude.

    Starting from AC3.3 the method respects the frame setting. Prior to that the frame was
    ignored. For more information see:
    http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned

    See the above link for information on the type_mask (0=enable, 1=ignore).
    At time of writing, acceleration and yaw bits are ignored.

    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,  # time_boot_ms (not used)
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_FRD,  # frame
        0b0000111111111000,  # type_mask (only positions enabled)
        north, east, down,  # x, y, z positions (or North, East, Down in the MAV_FRAME_BODY_NED frame
        0, 0, 0,  # x, y, z velocity in m/s  (not used)
        0, 0, 0,  # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to vehicle
    vehicle.send_mavlink(msg)


"""=====================================TEST CODE================================================================"""
print("SQUARE path using SET_POSITION_TARGET_LOCAL_NED and position parameters")
logging.info("SQUARE path using SET_POSITION_TARGET_LOCAL_NED and position parameters")
ALTITUDE_CONSTANT = 2
# Arm and take off to altitude of 2 meters
arm_and_takeoff(ALTITUDE_CONSTANT)

print("Set groundspeed to 1m/s.")
logging.info("Set groundspeed to 1m/s.")
vehicle.groundspeed = 1

# Going to first point
print("Going to first point")
logging.info("Going to first point")
goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
condition_yaw(90, True)
time.sleep(10)

# Going to second point
print("Going to second point")
logging.info("Going to second point")
goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
condition_yaw(90, True)
time.sleep(10)

# Going to third point
print("Going to third point")
logging.info("Going to third point")
goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
condition_yaw(90, True)
time.sleep(10)

# Going to fourth point
print("Going to fourth point")
logging.info("Going to fourth point")
goto_position_target_local_ned(2, 0, -ALTITUDE_CONSTANT)
time.sleep(10)
print("Turning 90 degrees")
logging.info("Turning 90 degrees")
condition_yaw(90, True)
time.sleep(10)

# TEST FINISHED PREPARING TO LAND
print("TEST FINISHED PREPARING TO LAND !")
logging.info("TEST FINISHED PREPARING TO LAND !")
print("Setting LAND mode...")
logging.info("Setting LAND mode...")
vehicle.mode = VehicleMode("LAND")

