import logging
import datetime
from guidance import Vant
from rrt import RRT
import time
from dronekit import LocationGlobalRelative
from constants import FLIGHT_ALTITUDE_METERS

logging_filename = f'mock_LIDAR_obstacles.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, level=logging.DEBUG)

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)
rrt_graph = RRT(start=[vehicle.latitude, vehicle.longitude, 0], arrival=[-3.072650, -59.990975], logging_file=logging_filename,
                csv_filename='mock_LIDAR_obstacles')
path = rrt_graph.get_path()

""" Start of test code """
""" Description -> Test for RRT code with no obstacles """
""" Arm and Takeoff in guided mode"""
start_full_path_time = datetime.datetime.now()

""" Move Vant in the points of path """
while len(path) != 0:
    print(vehicle.lidar_distance)
    time.sleep(4)
    if 0.3 < vehicle.lidar_distance < 1.0:
        start_time_rrt = datetime.datetime.now()
        print("MOCK RANGEFINDER")
        rrt_graph = RRT(start=[vehicle.latitude, vehicle.longitude, 0], arrival=[-3.072650, -59.990975], logging_file=logging_filename,
                        csv_filename='mock_LIDAR_obstacles')
        path = rrt_graph.get_path()
        finish_time_rrt = datetime.datetime.now()
        print(f"New generation took {finish_time_rrt - start_time_rrt}")
        print("NEW PATH !")
    path.pop(0)
    mock_rangefinder +=1

finish_full_path_time = datetime.datetime.now()
print(f"Execution to reach goal took {finish_full_path_time - start_full_path_time}")
