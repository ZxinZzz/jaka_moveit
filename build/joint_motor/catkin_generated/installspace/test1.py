#!/usr/bin/env python2
import sys
import rospy
import moveit_commander
import geometry_msgs
import tf
from math import pi
 
moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)
rospy.init_node('move_group', anonymous=True)
robot = moveit_commander.robot.RobotCommander()

arm_group = moveit_commander.move_group.MoveGroupCommander("arm")

#hand_group.set_named_target("close")
#plan = hand_group.go()

joint_home = [0, pi/6, 0, -pi/6, 0, pi/6]
plan = arm_group.go(joint_home, wait=True)

# arm_group.set_named_target("home")
plan = arm_group.go(joint_home)

print("Point 1")

# Open
#hand_group.set_joint_value_target([9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05, 9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05])
#hand_group.go(wait=True)
#print("Point 2")
#hand_group.set_named_target("open")
#plan = hand_group.go()
#print("Point 2")


pose_target = arm_group.get_current_pose().pose

# Block point
pose_target.position.x = 0.4
pose_target.position.y = 0.0
pose_target.position.z = pose_target.position.z+0.06



arm_group.set_pose_target(pose_target)
arm_group.go(wait=True)
print("Point 2")

# Block point
pose_target.position.x = 0.4
pose_target.position.y = 0.0
pose_target.position.z = pose_target.position.z-0.07



arm_group.set_pose_target(pose_target)
arm_group.go(wait=True)
print("Point 3")


#hand_group.set_named_target("close")
#plan = hand_group.go()
#print("Point 5")

pose_target.position.z = pose_target.position.z+0.05
arm_group.set_pose_target(pose_target)
plan = arm_group.go()
print("Point 4")


pose_target.position.z = pose_target.position.z+0.05
pose_target.position.x = 0.5
arm_group.set_pose_target(pose_target)
plan = arm_group.go()
print("Point 5")



#hand_group.set_named_target("open")
#plan = hand_group.go()
#print("Point 8")

rospy.sleep(5)
moveit_commander.roscpp_initializer.roscpp_shutdown()

