import logging
import time
from guidance import Vant

logging_filename = f'fly_2_meters_north.log'
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)

""" Start of test code """
""" Description -> Movement in north direction for 2 meters """

""" Arm and Takeoff in guided mode"""
vehicle.arm_and_takeoff()

""" Move Vant in 2 meters north """
vehicle.goto_position_target_local_ned(north=2, east=0)
time.sleep(10)
""" Land vehicle """
vehicle.land()
