from dronekit import connect
from constants import PIXHAWK_ADDRESS

vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)
print("CONNECTION SUCCEEDED !")

