import argparse
import time

from dronekit import connect

# Connect to UDP endpoint.
vehicle = connect('/dev/serial/by-id/usb-ArduPilot_Pixhawk1_3F0049001451353430383030-if00', wait_ready=True)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print("Mode: %s" % vehicle.mode.name)
print("Autopilot Firmware version: %s" % vehicle.version)
print("Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
print("Global Location: %s" % vehicle.location.global_frame)
print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print("Local Location: %s" % vehicle.location.local_frame)  # NED
print("Attitude: %s" % vehicle.attitude)
print("Velocity: %s" % vehicle.velocity)
print("GPS: %s" % vehicle.gps_0)
print("Groundspeed: %s" % vehicle.groundspeed)
print("Airspeed: %s" % vehicle.airspeed)
print("Gimbal status: %s" % vehicle.gimbal)
print("Battery: %s" % vehicle.battery)
print("EKF OK?: %s" % vehicle.ekf_ok)
print("Last Heartbeat: %s" % vehicle.last_heartbeat)
print("Rangefinder: %s" % vehicle.rangefinder)
print("Rangefinder distance: %s" % vehicle.rangefinder.distance)
print("Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
print("Heading: %s" % vehicle.heading)
print("Is Armable?: %s" % vehicle.is_armable)
print("System status: %s" % vehicle.system_status.state)
print("Mode: %s" % vehicle.mode.name)
print("Armed: %s" % vehicle.armed)


#
# from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
# import time
# import socket
# import math
# import argparse

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect
    baud_rate = 921600
    vehicle = connect(connection_string, baud_rate, wait_ready=True)
    return vehicle


def arm():
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    print("ready")
    print("")

    vehicle.armed = True
    while not vehicle.armed:
        print("waiting ")
        time.sleep(1)

    print("armed")
    print("spin")

    return None


vehicle = connectMyCopter()
arm()
print("end")
