#!/usr/bin/env python3

import rospy
import numpy as np
from tellopy import Tello
import tf2_ros
import time
import cv2

# - ROS messages imports
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
from sensor_msgs.msg import Image
from tello_ros_wrapper.msg import FlightData


class TelloDriverRos:

    # - Publishers
    video_stream_pub = None
    tello_pose_pub = None
    tello_flight_data_pub = None

    robot_vel_world_pub = None
    robot_vel_robot_pub = None

    robot_acc_world_pub = None
    robot_acc_robot_pub = None

    # - Subscribers
    robot_collision_sub = None
    flag_sub_tello_vel_cmd_unstamped = True
    tello_vel_cmd_unstamped_sub = None
    tello_vel_cmd_stamped_sub = None

    # - Topics
    cmd_vel_topic_name = '/tello_cmd_vel'
    video_stream_topic_name = '/camera/image_raw'
    tello_flight_data_topic_name = '/tello_flight_data'
    tello_vel_cmd_unstamped_topic_name = '/tello_cmd'
    tello_vel_cmd_stamped_topic_name = '/tello_cmd_stamped'

    # - TF2
    tello_frame = 'tello_base_link'
    world_frame = 'world'
    tf2_broadcaster = None

    # - Flags
    flag_sub_tello_vel_cmd_unstamped = False

    # - Timers
    pub_step_timer = None
    pub_step_time_interval = 0.02

    def __init__(self):
        self.tello = Tello()

    def begin(self):
        rospy.init_node('Tello_driver_ros')
        self.init_pub()
        self.init_sub()
        self.init_timers()

    def init_pub(self):
        self.tello_flight_data_pub = rospy.Publisher(
            self.tello_flight_data_topic_name,
            FlightData
        )

    def init_sub(self):
        if self.flag_sub_tello_vel_cmd_unstamped:
            self.tello_vel_cmd_unstamped_sub = rospy.Subscriber(
                self.tello_vel_cmd_unstamped_topic_name,
                Twist
            )

        self.tello_vel_cmd_stamped_sub = rospy.Subscriber(
            self.tello_vel_cmd_stamped_topic_name,
            Twist
        )

    def init_timers(self):
        self.pub_step_timer = rospy.Timer(
            rospy.Duration(self.pub_step_time_interval),
            self.pub_step_timer_callback
        )

    # +-----------+
    # | Callbacks |
    # +-----------+

    def tello_vel_cmd_unstamped_callback(self, twist_msg):
        lin_vel_cmd = np.zeros((3,), dtype=float)
        lin_vel_cmd[0] = twist_msg.twist.linear.x
        lin_vel_cmd[1] = twist_msg.twist.linear.y
        lin_vel_cmd[2] = twist_msg.twist.linear.z

        alg_vel_cmd = np.zeros((3,), dtype=float)
        alg_vel_cmd[0] = twist_msg.twist.linear.x
        alg_vel_cmd[1] = twist_msg.twist.linear.y
        alg_vel_cmd[2] = twist_msg.twist.linear.z


    def tello_vel_cmd_stamped_callback(self, twist_msg):
        lin_vel_cmd = np.zeros((3,), dtype=float)
        lin_vel_cmd[0] = twist_msg.twist.linear.x
        lin_vel_cmd[1] = twist_msg.twist.linear.y
        lin_vel_cmd[2] = twist_msg.twist.linear.z

        alg_vel_cmd = np.zeros((3,), dtype=float)
        alg_vel_cmd[0] = twist_msg.twist.linear.x
        alg_vel_cmd[1] = twist_msg.twist.linear.y
        alg_vel_cmd[2] = twist_msg.twist.linear.z

    def pub_step_timer_callback(self, timer_msg):
        pass

    def drone_controller(self, lin_vel_cmd, ang_vel_cmd):
        pass

    def run(self):
        rospy.spin()
        return

    def set_tello_vel_cmd(self):
        pass


if __name__ == '__main__':
    tello_driver = TelloDriverRos()
    tello_driver.begin()
    tello_driver.run()
