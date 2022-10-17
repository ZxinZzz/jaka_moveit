# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "joint_motor: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ijoint_motor:/home/axin/jaka_test2_ws/src/joint_motor/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(joint_motor_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_custom_target(_joint_motor_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "joint_motor" "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" "std_msgs/Float64:std_msgs/Int64"
)

get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_custom_target(_joint_motor_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "joint_motor" "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joint_motor
)
_generate_msg_cpp(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joint_motor
)

### Generating Services

### Generating Module File
_generate_module_cpp(joint_motor
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joint_motor
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(joint_motor_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(joint_motor_generate_messages joint_motor_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_cpp _joint_motor_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_cpp _joint_motor_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joint_motor_gencpp)
add_dependencies(joint_motor_gencpp joint_motor_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joint_motor_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joint_motor
)
_generate_msg_eus(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joint_motor
)

### Generating Services

### Generating Module File
_generate_module_eus(joint_motor
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joint_motor
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(joint_motor_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(joint_motor_generate_messages joint_motor_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_eus _joint_motor_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_eus _joint_motor_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joint_motor_geneus)
add_dependencies(joint_motor_geneus joint_motor_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joint_motor_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joint_motor
)
_generate_msg_lisp(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joint_motor
)

### Generating Services

### Generating Module File
_generate_module_lisp(joint_motor
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joint_motor
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(joint_motor_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(joint_motor_generate_messages joint_motor_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_lisp _joint_motor_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_lisp _joint_motor_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joint_motor_genlisp)
add_dependencies(joint_motor_genlisp joint_motor_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joint_motor_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joint_motor
)
_generate_msg_nodejs(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joint_motor
)

### Generating Services

### Generating Module File
_generate_module_nodejs(joint_motor
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joint_motor
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(joint_motor_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(joint_motor_generate_messages joint_motor_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_nodejs _joint_motor_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_nodejs _joint_motor_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joint_motor_gennodejs)
add_dependencies(joint_motor_gennodejs joint_motor_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joint_motor_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Float64.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Int64.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor
)
_generate_msg_py(joint_motor
  "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor
)

### Generating Services

### Generating Module File
_generate_module_py(joint_motor
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(joint_motor_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(joint_motor_generate_messages joint_motor_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/image_data.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_py _joint_motor_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/axin/jaka_test2_ws/src/joint_motor/msg/Tracker.msg" NAME_WE)
add_dependencies(joint_motor_generate_messages_py _joint_motor_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(joint_motor_genpy)
add_dependencies(joint_motor_genpy joint_motor_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS joint_motor_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joint_motor)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/joint_motor
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(joint_motor_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joint_motor)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/joint_motor
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(joint_motor_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joint_motor)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/joint_motor
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(joint_motor_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joint_motor)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/joint_motor
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(joint_motor_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/joint_motor
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(joint_motor_generate_messages_py std_msgs_generate_messages_py)
endif()
