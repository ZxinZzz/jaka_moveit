#!/usr/bin/env python2
import sys
import rospy
import moveit_commander
import geometry_msgs
import tf

 
moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)
rospy.init_node('move_group_grasp', anonymous=True)
robot = moveit_commander.robot.RobotCommander()

arm_group = moveit_commander.move_group.MoveGroupCommander("arm")
hand_group = moveit_commander.move_group.MoveGroupCommander("gripper")

#hand_group.set_named_target("close")
#plan = hand_group.go()



arm_group.set_named_target("home")
plan = arm_group.go()

print("Point 1")

# Open
#hand_group.set_joint_value_target([9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05, 9.800441184282249e-05, -9.800441184282249e-05, 9.800441184282249e-05])
#hand_group.go(wait=True)
#print("Point 2")
# joint_position = [0.9]
hand_group.set_named_target("open")
hand_group.go()
print("Point 2")


pose_target = arm_group.get_current_pose().pose

# Block point  0.1 0.0 0.775
pose_target.position.x = 0.1
pose_target.position.y = 0.0
pose_target.position.z = 0.2



arm_group.set_pose_target(pose_target)
arm_group.go(wait=True)
print("Point 3")

# Block point
pose_target.position.x = 0.1
pose_target.position.y = 0.0
pose_target.position.z = pose_target.position.z-0.07



arm_group.set_pose_target(pose_target)
arm_group.go(wait=True)
print("Point 4")

joint_position = [-0.5]

# hand_group.set_named_target("close")
hand_group.set_joint_value_target(joint_position)
plan = hand_group.go()
print("Point 5")

pose_target.position.z = pose_target.position.z+0.05
arm_group.set_pose_target(pose_target)
plan = arm_group.go()
print("Point 6")


pose_target.position.z = pose_target.position.z+0.05
pose_target.position.x = 0.5
arm_group.set_pose_target(pose_target)
plan = arm_group.go()
print("Point 7")



hand_group.set_named_target("open")
plan = hand_group.go()
print("Point 8")

rospy.sleep(5)
moveit_commander.roscpp_initializer.roscpp_shutdown()
