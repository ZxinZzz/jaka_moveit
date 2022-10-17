
(cl:in-package :asdf)

(defsystem "joint_motor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Tracker" :depends-on ("_package_Tracker"))
    (:file "_package_Tracker" :depends-on ("_package"))
    (:file "image_data" :depends-on ("_package_image_data"))
    (:file "_package_image_data" :depends-on ("_package"))
  ))