#!/usr/bin/env python3
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
import rospy

# initalize with roscore
rospy.init_node('test_message')

# defined both fields for the pointstamped message
my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
my_point = Point(1.0, 2.0, 0.0)

# create pointstamped
my_point_stamped = PointStamped(header=my_header, point=my_point)


# # print message
# print(my_point_stamped)

# OUTPUT
    # header: 
    #   seq: 0
    #   stamp: 
    #     secs: 1600629911
    #     nsecs: 267103672
    #   frame_id: "odom"
    # point: 
    #   x: 1.0
    #   y: 2.0
    #   z: 0.0


# publish messages to a topic called my_point
publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
r = rospy.Rate(2)       # 2 Hz
while not rospy.is_shutdown():
    my_point_stamped.header.stamp = rospy.Time.now()        # update timestamp
    publisher.publish(my_point_stamped)
    r.sleep()

    
