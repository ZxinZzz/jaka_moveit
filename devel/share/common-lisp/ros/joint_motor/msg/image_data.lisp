; Auto-generated. Do not edit!


(cl:in-package joint_motor-msg)


;//! \htmlinclude image_data.msg.html

(cl:defclass <image_data> (roslisp-msg-protocol:ros-message)
  ((detected_point_x
    :reader detected_point_x
    :initarg :detected_point_x
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (detected_point_y
    :reader detected_point_y
    :initarg :detected_point_y
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (detected_point_depth
    :reader detected_point_depth
    :initarg :detected_point_depth
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (area
    :reader area
    :initarg :area
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
)

(cl:defclass image_data (<image_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <image_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'image_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joint_motor-msg:<image_data> is deprecated: use joint_motor-msg:image_data instead.")))

(cl:ensure-generic-function 'detected_point_x-val :lambda-list '(m))
(cl:defmethod detected_point_x-val ((m <image_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joint_motor-msg:detected_point_x-val is deprecated.  Use joint_motor-msg:detected_point_x instead.")
  (detected_point_x m))

(cl:ensure-generic-function 'detected_point_y-val :lambda-list '(m))
(cl:defmethod detected_point_y-val ((m <image_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joint_motor-msg:detected_point_y-val is deprecated.  Use joint_motor-msg:detected_point_y instead.")
  (detected_point_y m))

(cl:ensure-generic-function 'detected_point_depth-val :lambda-list '(m))
(cl:defmethod detected_point_depth-val ((m <image_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joint_motor-msg:detected_point_depth-val is deprecated.  Use joint_motor-msg:detected_point_depth instead.")
  (detected_point_depth m))

(cl:ensure-generic-function 'area-val :lambda-list '(m))
(cl:defmethod area-val ((m <image_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joint_motor-msg:area-val is deprecated.  Use joint_motor-msg:area instead.")
  (area m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <image_data>) ostream)
  "Serializes a message object of type '<image_data>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'detected_point_x) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'detected_point_y) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'detected_point_depth) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'area) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <image_data>) istream)
  "Deserializes a message object of type '<image_data>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'detected_point_x) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'detected_point_y) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'detected_point_depth) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'area) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<image_data>)))
  "Returns string type for a message object of type '<image_data>"
  "joint_motor/image_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'image_data)))
  "Returns string type for a message object of type 'image_data"
  "joint_motor/image_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<image_data>)))
  "Returns md5sum for a message object of type '<image_data>"
  "1f5298c36c9abfd1a7f6f23e0f3b7591")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'image_data)))
  "Returns md5sum for a message object of type 'image_data"
  "1f5298c36c9abfd1a7f6f23e0f3b7591")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<image_data>)))
  "Returns full string definition for message of type '<image_data>"
  (cl:format cl:nil "std_msgs/Int64 detected_point_x~%std_msgs/Int64 detected_point_y~%std_msgs/Float64 detected_point_depth~%std_msgs/Float64 area~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'image_data)))
  "Returns full string definition for message of type 'image_data"
  (cl:format cl:nil "std_msgs/Int64 detected_point_x~%std_msgs/Int64 detected_point_y~%std_msgs/Float64 detected_point_depth~%std_msgs/Float64 area~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <image_data>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'detected_point_x))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'detected_point_y))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'detected_point_depth))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'area))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <image_data>))
  "Converts a ROS message object to a list"
  (cl:list 'image_data
    (cl:cons ':detected_point_x (detected_point_x msg))
    (cl:cons ':detected_point_y (detected_point_y msg))
    (cl:cons ':detected_point_depth (detected_point_depth msg))
    (cl:cons ':area (area msg))
))
