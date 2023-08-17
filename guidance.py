import time
from dronekit import connect, VehicleMode
from constants import PIXHAWK_ADDRESS, FLIGHT_ALTITUDE_METERS
import logging
from pymavlink import mavutil


class Vant:
    def __init__(self, logging_file):
        self.vehicle = connect(PIXHAWK_ADDRESS, wait_ready=True)
        self.altitude = FLIGHT_ALTITUDE_METERS
        self.vehicle.groundspeed = 1  # m/s
        self.logging = logging_file

    def collect_info(self):
        print("Mode: %s" % self.vehicle.mode.name)
        print("Autopilot Firmware version: %s" % self.vehicle.version)
        print("Autopilot capabilities (supports ftp): %s" % self.vehicle.capabilities.ftp)
        print("Global Location: %s" % self.vehicle.location.global_frame)
        print("Global Location (relative altitude): %s" % self.vehicle.location.global_relative_frame)
        print("Local Location: %s" % self.vehicle.location.local_frame)  # NED
        print("Attitude: %s" % self.vehicle.attitude)
        print("Velocity: %s" % self.vehicle.velocity)
        print("GPS: %s" % self.vehicle.gps_0)
        print("Groundspeed: %s" % self.vehicle.groundspeed)
        print("Airspeed: %s" % self.vehicle.airspeed)
        print("Gimbal status: %s" % self.vehicle.gimbal)
        print("Battery: %s" % self.vehicle.battery)
        print("EKF OK?: %s" % self.vehicle.ekf_ok)
        print("Last Heartbeat: %s" % self.vehicle.last_heartbeat)
        print("Rangefinder: %s" % self.vehicle.rangefinder)
        print("Rangefinder distance: %s" % self.vehicle.rangefinder.distance)
        print("Rangefinder voltage: %s" % self.vehicle.rangefinder.voltage)
        print("Heading: %s" % self.vehicle.heading)
        print("Is Armable?: %s" % self.vehicle.is_armable)
        print("System status: %s" % self.vehicle.system_status.state)
        print("Mode: %s" % self.vehicle.mode.name)
        print("Armed: %s" % self.vehicle.armed)
        logging.info("Mode: %s" % self.vehicle.mode.name)
        logging.info("Autopilot Firmware version: %s" % self.vehicle.version)
        logging.info("Autopilot capabilities (supports ftp): %s" % self.vehicle.capabilities.ftp)
        logging.info("Global Location: %s" % self.vehicle.location.global_frame)
        logging.info("Global Location (relative altitude): %s" % self.vehicle.location.global_relative_frame)
        logging.info("Local Location: %s" % self.vehicle.location.local_frame)  # NED
        logging.info("Attitude: %s" % self.vehicle.attitude)
        logging.info("Velocity: %s" % self.vehicle.velocity)
        logging.info("GPS: %s" % self.vehicle.gps_0)
        logging.info("Groundspeed: %s" % self.vehicle.groundspeed)
        logging.info("Airspeed: %s" % self.vehicle.airspeed)
        logging.info("Gimbal status: %s" % self.vehicle.gimbal)
        logging.info("Battery: %s" % self.vehicle.battery)
        logging.info("EKF OK?: %s" % self.vehicle.ekf_ok)
        logging.info("Last Heartbeat: %s" % self.vehicle.last_heartbeat)
        logging.info("Rangefinder: %s" % self.vehicle.rangefinder)
        logging.info("Rangefinder distance: %s" % self.vehicle.rangefinder.distance)
        logging.info("Rangefinder voltage: %s" % self.vehicle.rangefinder.voltage)
        logging.info("Heading: %s" % self.vehicle.heading)
        logging.info("Is Armable?: %s" % self.vehicle.is_armable)
        logging.info("System status: %s" % self.vehicle.system_status.state)
        logging.info("Mode: %s" % self.vehicle.mode.name)
        logging.info("Armed: %s" % self.vehicle.armed)

    def arm_and_takeoff(self):
        """
        Arms vehicle and fly to aTargetAltitude.
        """

        print("Basic pre-arm checks")
        logging.info("Basic pre-arm checks")
        # Don't let the user try to arm until autopilot is ready
        while not self.vehicle.is_armable:
            print(" Waiting for vehicle to initialise...")
            logging.info(" Waiting for vehicle to initialise...")
            time.sleep(1)

        print("Arming motors")
        logging.info("Arming motors")
        # Copter should arm in GUIDED mode
        self.vehicle.mode = VehicleMode("GUIDED")
        self.vehicle.armed = True

        while not self.vehicle.armed:
            print(" Waiting for arming...")
            logging.info(" Waiting for arming...")
            time.sleep(1)

        print("Taking off!")
        logging.info("Taking off!")
        self.vehicle.simple_takeoff(self.altitude)  # Take off to target altitude

        # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
        #  after Vehicle.simple_takeoff will execute immediately).
        while True:
            print(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            logging.info(" Altitude: ", self.vehicle.location.global_relative_frame.alt)
            if self.vehicle.location.global_relative_frame.alt >= self.altitude * 0.95:  # Trigger just below target alt.
                print("Reached target altitude")
                logging.info("Reached target altitude")
                break
            time.sleep(1)

    def condition_yaw(self, heading, relative=False):
        """
        Send MAV_CMD_CONDITION_YAW message to point vehicle at a specified heading (in degrees).

        This method sets an absolute heading by default, but you can set the `relative` parameter
        to `True` to set yaw relative to the current yaw heading.

        By default, the yaw of the vehicle will follow the direction of travel. After setting
        the yaw using this function there is no way to return to the default yaw "follow direction
        of travel" behaviour (https://github.com/diydrones/ardupilot/issues/2427)

        For more information see:
        http://copter.ardupilot.com/wiki/common-mavlink-mission-command-messages-mav_cmd/#mav_cmd_condition_yaw
        """
        if relative:
            is_relative = 1  # yaw relative to direction of travel
        else:
            is_relative = 0  # yaw is an absolute angle
        # create the CONDITION_YAW command using command_long_encode()
        msg = self.vehicle.message_factory.command_long_encode(
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW,  # command
            0,  # confirmation
            heading,  # param 1, yaw in degrees
            0,  # param 2, yaw speed deg/s
            1,  # param 3, direction -1 ccw, 1 cw
            is_relative,  # param 4, relative offset 1, absolute angle 0
            0, 0, 0)  # param 5 ~ 7 not used
        # send command to vehicle
        self.vehicle.send_mavlink(msg)

    def goto_position_target_local_ned(self, north, east):
        """
        Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified
        location in the North, East, Down frame.

        It is important to remember that in this frame, positive altitudes are entered as negative
        "Down" values. So if down is "10", this will be 10 metres below the home altitude.

        Starting from AC3.3 the method respects the frame setting. Prior to that the frame was
        ignored. For more information see:
        http://dev.ardupilot.com/wiki/copter-commands-in-guided-mode/#set_position_target_local_ned

        See the above link for information on the type_mask (0=enable, 1=ignore).
        At time of writing, acceleration and yaw bits are ignored.

        """
        down = -self.altitude
        msg = self.vehicle.message_factory.set_position_target_local_ned_encode(
            0,  # time_boot_ms (not used)
            0, 0,  # target system, target component
            mavutil.mavlink.MAV_FRAME_BODY_FRD,  # frame
            0b0000111111111000,  # type_mask (only positions enabled)
            north, east, down,  # x, y, z positions (or North, East, Down in the MAV_FRAME_BODY_NED frame
            0, 0, 0,  # x, y, z velocity in m/s  (not used)
            0, 0, 0,  # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
            0, 0)  # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
        # send command to vehicle
        self.vehicle.send_mavlink(msg)

    def land(self):
        print("Preparing to LAND")
        logging.info("Preparing to LAND")
        self.vehicle.mode = VehicleMode("LAND")
