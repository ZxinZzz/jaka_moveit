#! /usr/bin/env python


import imp
from multiprocessing.connection import Listener
import rospy
import tf2_ros
from tf2_geometry_msgs import PointStamped
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy

cam0_path = '/home/axin/butterfly/mvimage/'

def imgcallback(data):
    

if __name__ == "__main__":
    # 初始化
    rospy.init_node("object_detect")
    # 创建订阅对象
    buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buffer)

    rate = rospy.Rate(1)

    img_sub = rospy.Subscriber("/head_mount_kinect2/rgb/image_raw", Image, imgcallback, queue_size=1)

    