cmake_minimum_required(VERSION 3.8)
project(umi_gripper_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)
find_package(rviz2 REQUIRED)

install(DIRECTORY urdf meshes config
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  launch/display_robot.launch.py
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()


