import logging

from guidance import Vant
from rrt import RRT

logging_filename = f'fly_RRT_no_obstacles.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

# rrt = RRT(start=[-3.0727307, -59.9910685], arrival=[-3.072650, -59.990975], logging_file=logging_filename)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)
start_latitude = vehicle.latitude
start_longitude = vehicle.longitude
rrt_graph = RRT(start=[-3.072756, -59.990974, 0], arrival=[-3.072650, -59.990975], logging_file=logging_filename)
path = rrt_graph.get_path()

""" Start of test code """
""" Description -> Test for RRT code with no obstacles """

""" Arm and Takeoff in guided mode"""
# vehicle.arm_and_takeoff()
#
# """ Move Vant in the points of path """
# for i in range(len(path)):
#     logging.info(f'Going to {i} path point Lat:{path[i][0]} Long:{path[i][1]}')
#     vehicle.goto_position_target_local_ned(north=2, east=0)
#
# """ Land vehicle """
# vehicle.land()
