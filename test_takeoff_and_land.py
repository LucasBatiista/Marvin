import logging
import time
from guidance import Vant

logging_filename = f'takeoff_and_land_test.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

""" Initializing vehicle connection"""
print("Initializing vehicle connection")
logging.info("Initializing vehicle connection")

vehicle = Vant(logging_filename)

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

print("Sleeping for 5 seconds")
logging.info("Sleeping for 5 seconds")
time.sleep(5)
""" Land vehicle """
print("Land vehicle")
logging.info("Land vehicle")

vehicle.land()
