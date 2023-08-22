import logging

from guidance import Vant
from rrt import RRT
import time
from dronekit import LocationGlobalRelative

logging_filename = f'fly_RRT_no_obstacles.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, level=logging.DEBUG)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)
rrt_graph = RRT(start=[vehicle.latitude, vehicle.longitude, 0], arrival=[-3.072650, -59.990975], logging_file=logging_filename,
                csv_filename='fly_RRT_no_obstacles')
path = rrt_graph.get_path()

""" Start of test code """
""" Description -> Test for RRT code with no obstacles """
""" Arm and Takeoff in guided mode"""
vehicle.arm_and_takeoff()


""" Move Vant in the points of path """
for i in range(len(path)):
    actual_location = LocationGlobalRelative(vehicle.latitude, vehicle.longitude, 3)
    next_location = LocationGlobalRelative(path[i][0], path[i][1], 3)
    bearing = vehicle.get_bearing(actual_location, next_location)
    print(f'Going to {i} path point Lat:{path[i][0]} Long:{path[i][1]}')
    logging.info(f'Going to {i} path point Lat:{path[i][0]} Long:{path[i][1]}') 
    vehicle.goto(path[i][0],path[i][1], 3)
    vehicle.condition_yaw(bearing)
    print(f'Actual location: Lat {vehicle.latitude}, Long {vehicle.longitude}')
    logging.info(f'Actual location: Lat {vehicle.latitude}, Long {vehicle.longitude}')
    time.sleep(5)

""" Land vehicle """
vehicle.land()
