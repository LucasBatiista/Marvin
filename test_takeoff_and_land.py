import logging
import time
from guidance import Vant

logging_filename = f'takeoff_and_land_test.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)

""" Start of test code """
""" Description -> Takeoff and Land """

""" Arm and Takeoff in guided mode"""
vehicle.arm_and_takeoff()
time.sleep(5)
""" Land vehicle """
vehicle.land()
