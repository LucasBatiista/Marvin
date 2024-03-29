import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from constants import PIXHAWK_ADDRESS
import logging
from datetime import datetime

today = f'{datetime.now().date()}_{datetime.now().hour}_{datetime.now().minute}'

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=f'fly_in_line_test_{today}.log', encoding='utf-8', level=logging.DEBUG)

vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)


def arm_and_takeoff(altitude):
    """
    Arms vehicle and fly to a certain altitude.
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
    vehicle.simple_takeoff(altitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        logging.info(f" Altitude: {vehicle.location.global_relative_frame.alt}")
        print(f" GPS Location: {vehicle.gps_0}")
        logging.info(f" GPS Location: {vehicle.gps_0}")
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
            print("Reached target altitude")
            logging.info("Reached target altitude")
            break
        time.sleep(1)

    print("End of test")
    logging.info("End of test")


arm_and_takeoff(2)

time.sleep(5)
print("Set default/target airspeed to 0.5")
logging.info("Set default/target airspeed to 0.5")
vehicle.airspeed = 0.5

print("Going to location !")
logging.info("Going to location !")
destination = LocationGlobalRelative(-3.072670, -59.990967, 1)
vehicle.simple_goto(destination)
time.sleep(30)

print("Preparing to LAND")
logging.info("Preparing to LAND")
vehicle.mode = VehicleMode("LAND")

print("End of test")
logging.info("End of test")
