;; Auto-generated. Do not edit!


(when (boundp 'joint_motor::image_data)
  (if (not (find-package "JOINT_MOTOR"))
    (make-package "JOINT_MOTOR"))
  (shadow 'image_data (find-package "JOINT_MOTOR")))
(unless (find-package "JOINT_MOTOR::IMAGE_DATA")
  (make-package "JOINT_MOTOR::IMAGE_DATA"))

(in-package "ROS")
;;//! \htmlinclude image_data.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass joint_motor::image_data
  :super ros::object
  :slots (_detected_point_x _detected_point_y _detected_point_depth _area ))

(defmethod joint_motor::image_data
  (:init
   (&key
    ((:detected_point_x __detected_point_x) (instance std_msgs::Int64 :init))
    ((:detected_point_y __detected_point_y) (instance std_msgs::Int64 :init))
    ((:detected_point_depth __detected_point_depth) (instance std_msgs::Float64 :init))
    ((:area __area) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _detected_point_x __detected_point_x)
   (setq _detected_point_y __detected_point_y)
   (setq _detected_point_depth __detected_point_depth)
   (setq _area __area)
   self)
  (:detected_point_x
   (&rest __detected_point_x)
   (if (keywordp (car __detected_point_x))
       (send* _detected_point_x __detected_point_x)
     (progn
       (if __detected_point_x (setq _detected_point_x (car __detected_point_x)))
       _detected_point_x)))
  (:detected_point_y
   (&rest __detected_point_y)
   (if (keywordp (car __detected_point_y))
       (send* _detected_point_y __detected_point_y)
     (progn
       (if __detected_point_y (setq _detected_point_y (car __detected_point_y)))
       _detected_point_y)))
  (:detected_point_depth
   (&rest __detected_point_depth)
   (if (keywordp (car __detected_point_depth))
       (send* _detected_point_depth __detected_point_depth)
     (progn
       (if __detected_point_depth (setq _detected_point_depth (car __detected_point_depth)))
       _detected_point_depth)))
  (:area
   (&rest __area)
   (if (keywordp (car __area))
       (send* _area __area)
     (progn
       (if __area (setq _area (car __area)))
       _area)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int64 _detected_point_x
    (send _detected_point_x :serialization-length)
    ;; std_msgs/Int64 _detected_point_y
    (send _detected_point_y :serialization-length)
    ;; std_msgs/Float64 _detected_point_depth
    (send _detected_point_depth :serialization-length)
    ;; std_msgs/Float64 _area
    (send _area :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int64 _detected_point_x
       (send _detected_point_x :serialize s)
     ;; std_msgs/Int64 _detected_point_y
       (send _detected_point_y :serialize s)
     ;; std_msgs/Float64 _detected_point_depth
       (send _detected_point_depth :serialize s)
     ;; std_msgs/Float64 _area
       (send _area :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int64 _detected_point_x
     (send _detected_point_x :deserialize buf ptr-) (incf ptr- (send _detected_point_x :serialization-length))
   ;; std_msgs/Int64 _detected_point_y
     (send _detected_point_y :deserialize buf ptr-) (incf ptr- (send _detected_point_y :serialization-length))
   ;; std_msgs/Float64 _detected_point_depth
     (send _detected_point_depth :deserialize buf ptr-) (incf ptr- (send _detected_point_depth :serialization-length))
   ;; std_msgs/Float64 _area
     (send _area :deserialize buf ptr-) (incf ptr- (send _area :serialization-length))
   ;;
   self)
  )

(setf (get joint_motor::image_data :md5sum-) "1f5298c36c9abfd1a7f6f23e0f3b7591")
(setf (get joint_motor::image_data :datatype-) "joint_motor/image_data")
(setf (get joint_motor::image_data :definition-)
      "std_msgs/Int64 detected_point_x
std_msgs/Int64 detected_point_y
std_msgs/Float64 detected_point_depth
std_msgs/Float64 area
================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :joint_motor/image_data "1f5298c36c9abfd1a7f6f23e0f3b7591")


