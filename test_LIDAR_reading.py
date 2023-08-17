from guidance import Vant
import logging

logging_filename = f'test_LIDAR_reading.log'
logging.basicConfig(format='[%(asctime)s][%(module)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    filename=logging_filename, encoding='utf-8', level=logging.DEBUG)

vehicle = Vant(logging_file=logging_filename)

while vehicle.lidar_distance > 1.0:
    print(vehicle.lidar_distance)

print(f'LIDAR distance: {vehicle.lidar_distance}')
