#!/usr/bin/env python3
""" Investigate receiving a message using a callback function """
from geometry_msgs.msg import PointStamped
import rospy

rospy.init_node('receive_message')

# call back function
# needs to handle objects of type geometry_msgs/PointStamped

def process_point(msg):
        print(msg.header)


# subscribe to a specific topic
rospy.Subscriber("/my_point", PointStamped, process_point)

rospy.spin()


