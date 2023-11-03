import os
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch import LaunchDescription


from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    robot_state_publisher = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('baa_bot_description'),
                    'launch',
                    'robot_state_publisher.launch.py'
                ])
            ])
    )

    start_joint_pub_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen')
    
    rviz_config_file = os.path.join(
        get_package_share_directory('baa_bot_description'), 'config','rviz','show.rviz')

    start_rviz_cmd = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen')

    ld = LaunchDescription()

    ld.add_action(robot_state_publisher)
    ld.add_action(start_joint_pub_gui)
    ld.add_action(start_rviz_cmd)

    return ld