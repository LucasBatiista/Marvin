import logging
import datetime
from guidance import Vant
from rrt import RRT
import time
from dronekit import LocationGlobalRelative
from constants import FLIGHT_ALTITUDE_METERS

logging_filename = f'fly_RRT_with_obstacles_final.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, level=logging.DEBUG)

# fim do campo [-3.072650, -59.990975]
# fim do campo 2 [-3.072655081328897, -59.99097170261287]
# começo [-3.072764893793319,-59.99096969095618]

""" Initializing vehicle connection"""
vehicle = Vant(logging_filename)
rrt_graph = RRT(start=[vehicle.latitude, vehicle.longitude, 0], arrival=[-3.072764893793319, -59.99096969095618], logging_file=logging_filename,
                csv_filename='fly_RRT_with_obstacles_final')
path = rrt_graph.get_path()

""" Start of test code """
""" Description -> Test for RRT code with no obstacles """
""" Arm and Takeoff in guided mode"""
vehicle.arm_and_takeoff()
start_full_path_time = datetime.datetime.now()
csv_file_counter = 1
""" Move Vant in the points of path """
while len(path) != 0:
    actual_location = LocationGlobalRelative(vehicle.latitude, vehicle.longitude, FLIGHT_ALTITUDE_METERS)
    next_location = LocationGlobalRelative(path[0][0], path[0][1], FLIGHT_ALTITUDE_METERS)
    bearing = vehicle.get_bearing(actual_location, next_location)
    print(f'Going to path point Lat:{path[0][0]} Long:{path[0][1]}')
    logging.info(f'Going to path point Lat:{path[0][0]} Long:{path[0][1]}')
    vehicle.goto(path[0][0],path[0][1], FLIGHT_ALTITUDE_METERS)
    vehicle.condition_yaw(bearing)
    print(f'Actual location: Lat {vehicle.latitude}, Long {vehicle.longitude}')
    logging.info(f'Actual location: Lat {vehicle.latitude}, Long {vehicle.longitude}')
    time.sleep(4)
    if 0.3 < vehicle.lidar_distance < 1.0:
        start_time_rrt = datetime.datetime.now()
        print("OBSTACLE DETECTED !")
        logging.info("OBSTACLE DETECTED !")
        rrt_graph = RRT(start=[vehicle.latitude, vehicle.longitude, 0], arrival=[-3.072764893793319, -59.99096969095618], logging_file=logging_filename,
                        csv_filename=f'fly_RRT_with_obstacles_final{csv_file_counter}')
        path = rrt_graph.get_path()
        finish_time_rrt = datetime.datetime.now()
        print(f"New generation took {finish_time_rrt - start_time_rrt}")
        print("NEW PATH !")
        csv_file_counter += 1
    path.pop(0)

finish_full_path_time = datetime.datetime.now()
print(f"Execution to reach goal took {finish_full_path_time - start_full_path_time}")
""" Land vehicle """
vehicle.land()
