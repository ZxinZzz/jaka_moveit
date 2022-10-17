#!/usr/bin/env python



import rospy, sys, numpy as np
import geometry_msgs.msg
import moveit_msgs.msg
from joint_motor.msg import Tracker
from std_msgs.msg import Header
from std_msgs.msg import Bool
from std_srvs.srv import Empty

def gripper_status(msg):
    if msg.data:
        return True
        # print('gripper status = {}'.format(msg.data))

def gripper_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper1_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper1/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper1/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper2_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper2/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper2/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper3_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper3/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper3/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper4_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper4/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper4/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper5_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper5/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper5/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper6_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper6/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper6/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper7_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper7/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper7/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper8_on():
    # Wait till the srv is available
    rospy.wait_for_service('/jaka_zu3/gripper8/on')
    try:
        # Create a handle for the calling the srv
        turn_on = rospy.ServiceProxy('/jaka_zu3/gripper8/on', Empty)
        # Use this handle just like a normal function and call it
        resp = turn_on()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)


def gripper_off():
    rospy.wait_for_service('/jaka_zu3/gripper/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper1_off():
    rospy.wait_for_service('/jaka_zu3/gripper1/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper1/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper2_off():
    rospy.wait_for_service('/jaka_zu3/gripper2/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper2/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper3_off():
    rospy.wait_for_service('/jaka_zu3/gripper3/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper3/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper4_off():
    rospy.wait_for_service('/jaka_zu3/gripper4/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper4/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper5_off():
    rospy.wait_for_service('/jaka_zu3/gripper5/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper5/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper6_off():
    rospy.wait_for_service('/jaka_zu3/gripper6/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper6/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper7_off():
    rospy.wait_for_service('/jaka_zu3/gripper7/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper7/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def gripper8_off():
    rospy.wait_for_service('/jaka_zu3/gripper8/off')
    try:
        turn_off = rospy.ServiceProxy('/jaka_zu3/gripper8/off', Empty)
        resp = turn_off()
        return resp
    except rospy.ServiceException as e:
        print ("Service call failed: %s" % e)

def trigger(msg):
    gripper_trigger = msg.flag2
    if gripper_trigger:
        gripper_on()
        gripper1_on()
        gripper2_on()
        gripper3_on()
        gripper4_on()
        gripper5_on()
        gripper6_on()
        gripper7_on()
        gripper8_on()

    else:
        gripper_off()
        gripper1_off()
        gripper2_off()
        gripper3_off()
        gripper4_off()
        gripper5_off()
        gripper6_off()
        gripper7_off()
        gripper8_off()
       

rospy.init_node("jaka_gripper", anonymous=False)

gripper_status_sub = rospy.Subscriber('/jaka_zu3/gripper/grasping', Bool, gripper_status, queue_size=1)

cxy_sub = rospy.Subscriber('cxy1', Tracker, trigger, queue_size=1)

rospy.spin()
