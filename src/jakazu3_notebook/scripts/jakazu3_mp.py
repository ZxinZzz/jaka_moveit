#!/usr/bin/env python
# - * - coding: UTF - 8 - * -
"""
  by zx
"""

import rospy, sys, numpy as np
import moveit_commander
from copy import deepcopy
from geometry_msgs.msg import Twist
import moveit_msgs.msg
from sensor_msgs.msg import Image
from joint_motor.msg import Tracker
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from time import sleep
tracker = Tracker()



class jaka_mp:
    def __init__(self):
        rospy.init_node("jaka_zu3_mp", anonymous=False)
        self.cxy_sub = rospy.Subscriber('cxy', Tracker, self.tracking_callback, queue_size=1)
        self.cxy_pub = rospy.Publisher('cxy1', Tracker, queue_size=1)
        self.phase = 1
        self.object_cnt = 0
        self.track_flag = False
        self.default_pose_flag = True
        self.cx = 320.0
        self.cy = 240.0
        self.points=[]
        self.state_change_time = rospy.Time.now()

        rospy.loginfo("Starting node moveit_cartesian_path")

        rospy.on_shutdown(self.cleanup)

        # Initialize the move_group API
        moveit_commander.roscpp_initializer.roscpp_initialize(sys.argv)

        # Initialize the move group for the jaka
        self.arm = moveit_commander.move_group.MoveGroupCommander('arm')

        # Get the name of the end-effector link
        self.end_effector_link = self.arm.get_end_effector_link()

        # Set the reference frame for pose targets
        reference_frame = "/Link_0"

        # Set the jaka_arm reference frame accordingly
        self.arm.set_pose_reference_frame(reference_frame)

        # Allow replanning to increase the odds of a solution
        self.arm.allow_replanning(True)

        # Allow some leeway in position (meters) and orientation (radians)
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)
        self.arm.set_planning_time(0.1)
        self.arm.set_max_acceleration_scaling_factor(.5)
        self.arm.set_max_velocity_scaling_factor(.5)

        # Get the current pose so we can add it as a waypoint
        start_pose = self.arm.get_current_pose(self.end_effector_link).pose

        # Initialize the waypoints list
        self.waypoints= []
        self.pointx = []
        self.pointy = []
        # Set the first waypoint to be the starting pose
        # Append the pose to the waypoints list
        wpose = deepcopy(start_pose)

        # Set the next waypoint to the right 0.5 meters

        wpose.position.x = -0.2
        wpose.position.y = -0.2
        wpose.position.z = 0.3
        self.waypoints.append(deepcopy(wpose))

        # wpose.position.x = 0.1052
        # wpose.position.y = -0.4271
        # wpose.position.z = 0.4005
        #
        # wpose.orientation.x = 0.4811
        # wpose.orientation.y = 0.5070
        # wpose.orientation.z = -0.5047
        # wpose.orientation.w = 0.5000

        # self.waypoints.append(deepcopy(wpose))


        if np.sqrt((wpose.position.x-start_pose.position.x)**2+(wpose.position.y-start_pose.position.y)**2 \
            +(wpose.position.z-start_pose.position.z)**2)<0.1:
            rospy.loginfo("Warnig: target position overlaps with the initial position!")

        # self.arm.set_pose_target(wpose)




        # Specify default (idle) joint states
        # ?????????????????????
        # self.default_joint_states = self.arm.get_current_joint_values()
        # self.default_joint_states[0] = 0.1
        # self.default_joint_states[1] = 0.7
        # self.default_joint_states[2] = -1.2
        # self.default_joint_states[3] = 2.12182
        # self.default_joint_states[4] = 1.5950
        # self.default_joint_states[5] = 0

        # ????????????
        self.default_joint_states = self.arm.get_current_joint_values()
        self.default_joint_states[0] = 1
        self.default_joint_states[1] = 1
        self.default_joint_states[2] = -1.2
        self.default_joint_states[3] = 2
        self.default_joint_states[4] = 1.6
        self.default_joint_states[5] = 0

        self.arm.set_joint_value_target(self.default_joint_states)

        # Set the internal state to the current state
        self.arm.set_start_state_to_current_state()
        plan = self.arm.plan()

        self.arm.execute(plan)

        # Specify end states (drop object)  ?????????????????? ???????????????
        self.end_joint_states = deepcopy(self.default_joint_states)
        # self.end_joint_states[0] = -3.65
        # self.end_joint_states[1] = -1.3705
        self.end_joint_states[1] = 1

        self.transition_pose = deepcopy(self.default_joint_states)
        self.transition_pose[0] = -3.65
        self.transition_pose[4] = -1.95

    def cleanup(self):
        rospy.loginfo("Stopping the robot")

        # Stop any current arm movement
        self.arm.stop()

        #Shut down MoveIt! cleanly
        rospy.loginfo("Shutting down Moveit!")
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

    def tracking_callback(self, msg):
        self.Zc = 0.77
        self.f = 0.58937
        self.track_flag = msg.flag1
        self.cx = msg.x
        self.cy = msg.y
        self.Xc = self.cx * self.Zc / self.f 
        self.Yc = self.cy * self.Zc / self.f 
        self.error_x = msg.error_x
        self.error_y = msg.error_y
        if len(self.pointx)>9:
            self.track_flag = True
        if self.phase == 2:
            self.track_flag = False
            self.phase = 1

        if (self.track_flag and -0.6 < self.waypoints[0].position.x and self.waypoints[0].position.x < 0.6):
            self.execute()
            self.default_pose_flag = False
        else:
            if not self.default_pose_flag:
                self.track_flag = False
                self.execute()
                self.default_pose_flag = True



    def execute(self):
        if self.track_flag:


            # Get the current pose so we can add it as a waypoint
            start_pose = self.arm.get_current_pose(self.end_effector_link).pose

            # Initialize the waypoints list
            self.waypoints= []

            # Set the first waypoint to be the starting pose
            # Append the pose to the waypoints list
            wpose = deepcopy(start_pose)

            # wpose.position.x = -0.5215
            # wpose.position.y = 0.2014
            # wpose.position.z = 0.4102


            if len(self.pointx)>8:
                if len(self.pointx)==9:
                    x_speed = np.mean(np.asarray(self.pointx[4:8]) - np.asarray(self.pointx[3:7]))
                    wpose.position.x += 2 * x_speed
                    wpose.position.z = 0.05


                else:
                    if len(self.pointx)==11:
                        tracker.flag2 = 1
                        self.cxy_pub.publish(tracker)

                    if len(self.pointx)<12:
                        x_speed = np.mean(np.asarray(self.pointx[4:8])-np.asarray(self.pointx[3:7]))
                        wpose.position.x += (x_speed-self.error_x*0.015/105)

                    else:
                        if tracker.flag2:
                            self.track_flag=False
                        transition_pose = deepcopy(start_pose)
                        transition_pose.position.z = 0.77
                        # transition_pose.position.z = 0.4000

                        self.waypoints.append(deepcopy(transition_pose))

                        self.arm.set_start_state_to_current_state()
                        plan, fraction = self.arm.compute_cartesian_path(self.waypoints, 0.02, 0.0, True)
                        self.arm.execute(plan)

                        self.arm.set_max_acceleration_scaling_factor(.15)
                        self.arm.set_max_velocity_scaling_factor(.25)



                        self.arm.set_joint_value_target(self.transition_pose)
                        self.arm.set_start_state_to_current_state()
                        plan = self.arm.plan()
                        self.arm.execute(plan)

                        self.arm.set_joint_value_target(self.end_joint_states)
                        self.arm.set_start_state_to_current_state()
                        plan = self.arm.plan()
                        self.arm.execute(plan)

                        if -0.1+0.02*self.object_cnt<0.2:
                            self.object_cnt += 1

                        self.waypoints = []
                        start_pose = self.arm.get_current_pose(self.end_effector_link).pose
                        transition_pose = deepcopy(start_pose)
                        transition_pose.position.x -= 0.1
                        transition_pose.position.z = -0.1 + self.object_cnt*0.025
                        self.waypoints.append(deepcopy(transition_pose))

                        self.arm.set_start_state_to_current_state()
                        plan, fraction = self.arm.compute_cartesian_path(self.waypoints, 0.02, 0.0, True)
                        self.arm.execute(plan)

                        self.phase = 2
                        tracker.flag2 = 0
                        self.cxy_pub.publish(tracker)



            # Set the next waypoint to the right 0.5 meters
            else:
                wpose.position.x -= self.error_x*0.05/105
                wpose.position.y += self.error_y*0.04/105
                wpose.position.z = 0.15
                #wpose.position.z = 0.4005

            if self.phase == 1:
                self.waypoints.append(deepcopy(wpose))


                self.pointx.append(wpose.position.x)
                self.pointy.append(wpose.position.y)

                # Set the internal state to the current state
                # self.arm.set_pose_target(wpose)

                self.arm.set_start_state_to_current_state()

                # Plan the Cartesian path connecting the waypoints

  
                plan, fraction = self.arm.compute_cartesian_path(self.waypoints, 0.01, 0.0, True)


                # plan = self.arm.plan()

                # If we have a complete plan, execute the trajectory
                if 1-fraction < 0.2:
                    rospy.loginfo("Path computed successfully. Moving the arm.")
                    num_pts = len(plan.joint_trajectory.points)
                    rospy.loginfo("\n# intermediate waypoints = "+str(num_pts))
                    self.arm.execute(plan)
                    rospy.loginfo("Path execution complete.")
                else:
                    rospy.loginfo("Path planning failed")

        else:
            # Get the current pose so we can add it as a waypoint
            start_pose = self.arm.get_current_pose(self.end_effector_link).pose

            # Initialize the waypoints list
            self.waypoints= []
            self.pointx = []
            self.pointy = []
            # Set the first waypoint to be the starting pose
            # Append the pose to the waypoints list
            wpose = deepcopy(start_pose)

            # Set the next waypoint to the right 0.5 meters

            wpose.position.x = 0.1052
            wpose.position.y = -0.4271
            wpose.position.z = 0.4005

            wpose.orientation.x = 0.4811
            wpose.orientation.y = 0.4994
            wpose.orientation.z = -0.5121
            wpose.orientation.w = 0.5069

            self.pointx.append(wpose.position.x)
            self.pointy.append(wpose.position.y)
            self.waypoints.append(deepcopy(wpose))
            # Set the internal state to the current state
            # self.arm.set_pose_target(wpose)

            self.arm.set_start_state_to_current_state()

            # Plan the Cartesian path connecting the waypoints

        
            plan, fraction = self.arm.compute_cartesian_path(self.waypoints, 0.01, 0.0, True)


            # plan = self.arm.plan()

            # If we have a complete plan, execute the trajectory
            if 1-fraction < 0.2:
                rospy.loginfo("Path computed successfully. Moving the arm.")
                num_pts = len(plan.joint_trajectory.points)
                rospy.loginfo("\n# intermediate waypoints = "+str(num_pts))
                self.arm.execute(plan)
                rospy.loginfo("Path execution complete.")
            else:
                rospy.loginfo("Path planning failed")
        # print self.points




mp = jaka_mp()

rospy.spin()
