import logging

from guidance import Vant
from rrt import RRT

logging_filename = f'fly_RRT_with_obstacles.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)
""" Getting first coordinates """
start_latitude = vehicle.latitude
start_longitude = vehicle.longitude
""" Calculating RRT path """
rrt_graph = RRT(start=[start_latitude, start_longitude, 0], arrival=[-3.072650, -59.990975],
                logging_file=logging_filename)

path = rrt_graph.get_path()

""" Start of test code """
""" Description -> Test for RRT code with obstacles """

""" Arm and Takeoff in guided mode"""
vehicle.arm_and_takeoff()

""" Move Vant in the points of path """
for i in range(len(path)):
    logging.info(f'Going to {i} path point Lat:{path[i][0]} Long:{path[i][1]}')
    vehicle.goto_position_target_local_ned(north=2, east=0)

""" Land vehicle """
vehicle.land()
