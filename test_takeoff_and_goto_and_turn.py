import logging
import time
from guidance import Vant


logging_filename = f'takeoff_and_land_test.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, level=logging.DEBUG)

""" Initializing vehicle connection"""
print("Initializing vehicle connection")
logging.info("Initializing vehicle connection")

vehicle = Vant(logging_filename)

print(vehicle.latitude)
print(vehicle.longitude)

""" Start of test code """
print("Start of test code")
logging.info("Start of test code")
""" Description -> Takeoff and Land """
print("Description -> Takeoff and Land")
logging.info("Description -> Takeoff and Land")
""" Arm and Takeoff in guided mode """
print("Arm and Takeoff in guided mode")
logging.info("Arm and Takeoff in guided mode")

vehicle.arm_and_takeoff()

""" Going to location """

vehicle.goto(-3.072659798378274, -59.99096992871654, 5)
time.sleep(15)
vehicle.condition_yaw(226)
time.sleep(15)
vehicle.condition_yaw(140)
time.sleep(15)
vehicle.condition_yaw(0)
time.sleep(15)
vehicle.condition_yaw(90)

print("Sleeping for 5 seconds")
logging.info("Sleeping for 5 seconds")
time.sleep(5)
