import logging
import time
from guidance import Vant

logging_filename = f'fly_2_meters_north.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

""" Initializing vehicle connection"""
print("Initializing vehicle connection")
logging.info("Initializing vehicle connection")

vehicle = Vant(logging_filename)

""" Start of test code """
print(" Start of test code")
logging.info(" Start of test code")
""" Description -> Movement in north direction for 2 meters """
print("Description -> Movement in north direction for 2 meters")
logging.info("Description -> Movement in north direction for 2 meters")
""" Arm and Takeoff in guided mode"""
print("Arm and Takeoff in guided mode")
logging.info("Arm and Takeoff in guided mode")

vehicle.arm_and_takeoff()

""" Move Vant in 2 meters north """
print("Move Vant in 2 meters north")
logging.info("Move Vant in 2 meters north")

vehicle.goto_position_target_local_ned(north=2, east=0)
""" Sleeping for 5 seconds """
print("Sleeping for 5 seconds")
logging.info("Sleeping for 5 seconds")

time.sleep(5)

""" Land vehicle """
print("Land vehicle")
logging.info("Land vehicle")

vehicle.land()
