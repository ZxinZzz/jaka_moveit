#!/usr/bin/env python
# - * - coding: UTF - 8 - * -

import sys
import rospy
import moveit_commander
import geometry_msgs
import tf
from math import pi
 
 


# 初始化move_group的API
moveit_commander.roscpp_initialize(sys.argv)
        
# 初始化ROS节点
rospy.init_node('moveit_ik_demo')
                
# 初始化需要使用move group控制的机械臂中的arm group
arm = moveit_commander.move_group.MoveGroupCommander('arm')
gripper = moveit_commander.move_group.MoveGroupCommander('gripper')
                
# 获取终端link的名称，这个在setup assistant中设置过了
end_effector_link = arm.get_end_effector_link()
                        
# 设置目标位置所使用的参考坐标系
reference_frame = 'Link_0'
arm.set_pose_reference_frame(reference_frame)
                
# 当运动规划失败后，允许重新规划
arm.allow_replanning(True)
        
# 设置位置(单位：米)和姿态（单位：弧度）的允许误差
arm.set_goal_position_tolerance(0.001)
arm.set_goal_orientation_tolerance(0.01)       
# 设置允许的最大速度和加速度
arm.set_max_acceleration_scaling_factor(0.5)
arm.set_max_velocity_scaling_factor(0.5)
# 控制机械臂先回到初始化位置
arm.set_named_target('home')
arm.go()
gripper.set_named_target('open')
gripper.go()
rospy.sleep(1)
               
# 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
# 姿态使用四元数描述，基于base_link坐标系
# target_pose = PoseStamped()
# #参考坐标系，前面设置了
# target_pose.header.frame_id = reference_frame
# target_pose.header.stamp = rospy.Time.now() #时间戳？
#末端位置   
joint_taget_zhua = [-1.35795, 1.23025, -1.59852, 2.02732, 1.58512, -0.25533]
        
# 设置机器臂当前的状态作为运动初始状态
arm.set_start_state_to_current_state()
        
# 设置机械臂终端运动的目标位姿
arm.set_joint_value_target(joint_taget_zhua)
        
# 规划运动路径，返回虚影的效果
traj = arm.plan()
        
# 按照规划的运动路径控制机械臂运动
arm.execute(traj)
gripper.set_named_target('close')
gripper.go()
rospy.sleep(1)  #执行完成后休息1s
 
# joint_taget_wait = [3.9552851497989012, 3.722591838366397, -2.03199510532788, 4.285572913079537, 2.434284373156803, 1.8409467673834357]
joint_taget_wait = [0.06219418266278698, 1.318720491902277, -1.979834554153113, 0.8207231020572134, -1.3979860633055008, 1.5317844345764797]
arm.set_joint_value_target(joint_taget_wait)
arm.go()
rospy.sleep(1)



# 控制机械臂回到初始化位置
joint_taget_fang = [0.07049681036650668, 0.9993714678084515, -1.8802913694409806, 0.9354421068834196, -1.3962929387277256, 1.5102246731466398]
arm.set_joint_value_target(joint_taget_fang)
traj = arm.plan()
        
# 按照规划的运动路径控制机械臂运动
arm.execute(traj)
gripper.set_named_target('open')
gripper.go()
rospy.sleep(1)  #执行完成后休息1s

pose_taget = arm.get_current_pose().pose
pose_taget.position.z += 0.06
arm.set_pose_target(pose_taget)
arm.go()

 
# 关闭并退出moveit
moveit_commander.roscpp_shutdown()
moveit_commander.os._exit(0)
