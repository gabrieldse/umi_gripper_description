import os
from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'umi_gripper_description'
    urdf_file_name = 'urdf/umi_gripper.urdf'
    rviz_file_name = 'config/rviz.rviz'
    
    urdf_file_path = os.path.join(get_package_share_directory(package_name), urdf_file_name)
    rviz_file_path = os.path.join(get_package_share_directory(package_name), rviz_file_name)

    with open(urdf_file_path, 'r') as urdf_file:
        urdf_content = urdf_file.read()

    return LaunchDescription([
        DeclareLaunchArgument('robot_description', default_value=urdf_content, description='URDF content as string'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_content}],
        ),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory(package_name), rviz_file_path)], 
        ),
    ])
