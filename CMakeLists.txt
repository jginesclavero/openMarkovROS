cmake_minimum_required(VERSION 3.0.2)
project(openmarkov_roswrap)


find_package(catkin REQUIRED COMPONENTS
rospy
std_msgs
message_generation)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  OMvariable.msg
  StateWithProb.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  GetVarProbs.srv
  SetFinding.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES openmarkov_ros
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)
