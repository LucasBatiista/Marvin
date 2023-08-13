import time
from dronekit import connect
import logging

logging.basicConfig(filename=f'collect_data.log', encoding='utf-8', level=logging.DEBUG)
PIXHAWK_ADDRESS = '/dev/ttyACM0'
vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)

print("Collect data test start!")
logging.info("Collect data test start!")
while True:
    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
    logging.info(f" Altitude: {vehicle.location.global_relative_frame.alt}")
    print(f"Global Location: {vehicle.location.global_frame}")
    logging.info(f"Global Location: {vehicle.location.global_frame}")
    print(f"Global Location (relative altitude): {vehicle.location.global_relative_frame}")
    logging.info(f"Global Location (relative altitude): {vehicle.location.global_relative_frame}")
    print(f"Local Location: {vehicle.location.local_frame}")
    logging.info(f"Local Location: {vehicle.location.local_frame}")
    time.sleep(1)
