#! /usr/bin/env python

import rospy
import tf2_ros
import tf
from geometry_msgs.msg import TransformStamped
from tf.transformations import quaternion_from_euler



if __name__=="__main__":
    # 初始化节点
    rospy.init_node("object_detect")
    # 创建静态坐标广播器
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    # 创建并组织被广播的消息
    tfs = TransformStamped()

    tfs.header.frame_id = "Link_0"
    tfs.header.stamp = rospy.Time.now()
    tfs.header.seq = 101

    # 子坐标系
    tfs.child_frame_id = "kinect2_v0"
    # 偏移量
    tfs.transform.translation.x = 0
    tfs.transform.translation.y = -1.1
    tfs.transform.translation.z = 1.1

    # 四元数
    qtn = quaternion_from_euler(0, 1.57, 0)
    tfs.transform.rotation.x = qtn[0]
    tfs.transform.rotation.y = qtn[1]
    tfs.transform.rotation.z = qtn[2]
    tfs.transform.rotation.w = qtn[3]

    # 发布消息
    broadcaster.sendTransform(tfs)

    rospy.spin()