cmake_minimum_required(VERSION 2.8.3)
project(rviz_visualization)

########################################################################
# ROS dependency
########################################################################
find_package(catkin REQUIRED COMPONENTS
  osm_map_msgs
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)


catkin_python_setup()


catkin_package(CATKIN_DEPENDS
  osm_map_msgs
)

