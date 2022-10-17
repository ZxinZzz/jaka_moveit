#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import geometry_msgs
import tf

 
moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)
rospy.init_node('move_group', anonymous=True)
robot = moveit_commander.robot.RobotCommander()


group_name = "arm"
arm_group = moveit_commander.move_group.MoveGroupCommander(group_name)
hand_group = moveit_commander.move_group.MoveGroupCommander("gripper")

#hand_group.set_named_target("close")
#plan = hand_group.go()


arm_group.set_goal_position_tolerance(0.01)
arm_group.set_goal_orientation_tolerance(0.01)
# arm_group.set_named_target("home_j")
joint_home = [0, pi/6, 0, -pi/6, 0, pi/6]
plan = arm_group.go(joint_home, wait=True)


print("Point 1")

# Open
#hand_group.set_joint_value_target([9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05, 9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05])
#hand_group.go(wait=True)
#print("Point 2")
# hand_group.set_named_target("open")
# plan = hand_group.go()
# print("Point 2")


pose_target = arm_group.get_current_pose().pose

# Block point
pose_target.position.x = 0.4
pose_target.position.y = 0.0
pose_target.position.z = pose_target.position.z+0.06



arm_group.set_pose_target(pose_target)
arm_group.go(pose_target, wait=True)
print("Point 2")

# Block point
pose_target.position.x = 0.4
pose_target.position.y = 0.0
pose_target.position.z = pose_target.position.z-0.07



arm_group.set_pose_target(pose_target)
arm_group.go(pose_target, wait=True)
print("Point 3")


# hand_group.set_named_target("close")
# plan = hand_group.go()
# print("Point 5")

pose_target.position.z = pose_target.position.z+0.05
arm_group.set_pose_target(pose_target)
plan = arm_group.go(pose_target, wait=True)
print("Point 4")


pose_target.position.z = pose_target.position.z+0.05
pose_target.position.x = 0.5
arm_group.set_pose_target(pose_target)
plan = arm_group.go(pose_target, wait=True)
print("Point 5")



# hand_group.set_named_target("open")
# plan = hand_group.go()
# print("Point 8")

rospy.sleep(5)
moveit_commander.roscpp_initializer.roscpp_shutdown()
