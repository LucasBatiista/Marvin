import time
from dronekit import connect, VehicleMode
from constants import PIXHAWK_ADDRESS
import logging
from datetime import datetime

today = f'{datetime.now().date()}_{datetime.now().hour}_{datetime.now().minute}'

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=f'marvin_{today}.log', encoding='utf-8', level=logging.DEBUG)

vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    logging.info("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle )to initialise...")
        logging.info(" Waiting for vehicle )to initialise...")
        time.sleep(1)

    print("Arming motors")
    logging.info("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        logging.info(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    logging.info("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        logging.info(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            logging.info("Reached target altitude")
            break
        time.sleep(1)

    # Attempt to Land
    print("Preparing to LAND")
    logging.info("Preparing to LAND")
    vehicle.mode = VehicleMode("LAND")

    print("End of test")
    logging.info("End of test")


arm_and_takeoff(2)
