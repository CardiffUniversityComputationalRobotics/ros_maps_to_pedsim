from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "map_path", default_value=".", description="Path to the map directory"
            ),
            DeclareLaunchArgument(
                "map_name", default_value="map.yaml", description="Map YAML file name"
            ),
            DeclareLaunchArgument(
                "scenario_path",
                default_value=LaunchConfiguration("map_path"),
                description="Path to output scenario",
            ),
            DeclareLaunchArgument(
                "scenario_name",
                default_value="scene.xml",
                description="Scenario file name",
            ),
            DeclareLaunchArgument(
                "use_map_origin",
                default_value="false",
                description="Use map origin (true/false)",
            ),
            DeclareLaunchArgument(
                "add_agents",
                default_value="true",
                description="Whether to add agents (true/false)",
            ),
            DeclareLaunchArgument(
                "agents_info_path",
                default_value=LaunchConfiguration("map_path"),
                description="Path to the agents YAML",
            ),
            DeclareLaunchArgument(
                "agents_info_name",
                default_value="agents.yaml",
                description="Agents info YAML filename",
            ),
            Node(
                package="ros_maps_to_pedsim",
                executable="ros_maps_to_pedsim",
                name="ros_maps_to_pedsim",
                output="screen",
                parameters=[
                    {
                        "map_path": LaunchConfiguration("map_path"),
                        "map_name": LaunchConfiguration("map_name"),
                        "scenario_path": LaunchConfiguration("scenario_path"),
                        "scenario_name": LaunchConfiguration("scenario_name"),
                        "use_map_origin": LaunchConfiguration("use_map_origin"),
                        "add_agents": LaunchConfiguration("add_agents"),
                        "agents_info_path": LaunchConfiguration("agents_info_path"),
                        "agents_info_name": LaunchConfiguration("agents_info_name"),
                    }
                ],
            ),
        ]
    )
