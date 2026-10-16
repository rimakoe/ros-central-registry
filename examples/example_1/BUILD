load("@aspect_rules_py//py:defs.bzl", "py_binary", "py_library")
load("@pip_ros//:requirements.bzl", "requirement")
load("@rosdistro//ament:defs.bzl", "ament_package")
load("@rules_cc//cc:defs.bzl", "cc_library", "cc_shared_library")

config_setting(
    name = "dynamic_mode_off",
    values = {
        "dynamic_mode": "off",
    },
)

config_setting(
    name = "rmw_dynamic",
    flag_values = {"@rosdistro//:rmw": "dynamic"},
)

cc_library(
    name = "ros2_control_demo_example_1_lib",
    srcs = ["hardware/rrbot.cpp"],
    hdrs = glob(["hardware/include/**/*.hpp"]),
    includes = ["hardware/include"],
    visibility = ["//visibility:public"],
    deps = [
        "@hardware_interface//:hardware_interface_library",
        "@pluginlib//:pluginlib_library",
        "@rclcpp//:rclcpp_library",
        "@rclcpp_lifecycle//:rclcpp_lifecycle_library",
    ],
)

cc_shared_library(
    name = "ros2_control_demo_example_1",
    exports_filter = [
        ":ros2_control_demo_example_1_lib",
    ],
    visibility = ["//visibility:public"],
    deps = [":ros2_control_demo_example_1_lib"],
)

filegroup(
    name = "plugin_description",
    srcs = ["ros2_control_demo_example_1.xml"],
    visibility = ["//visibility:public"],
)

filegroup(
    name = "launch_and_config",
    srcs = glob([
        "description/launch/**",
        "description/ros2_control/**",
        "description/urdf/**",
        "bringup/launch/**",
        "bringup/config/**",
    ]),
    visibility = ["//visibility:public"],
)

py_library(
    name = "rrbot_launch",
    srcs = ["bringup/launch/rrbot.launch.py"],
    data = [
        ":ament_package",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "@launch",
        "@launch_ros",
        "@lifecycle_msgs//:py",
        "@rclpy",
        requirement("packaging"),
    ],
)

py_binary(
    name = "launch_runner",
    srcs = ["bringup/launch/launch_runner.py"],
    deps = [
        ":rrbot_launch",
    ],
)

ament_package(
    name = "ament_package",
    data = [":launch_and_config"],
    export_name = "ros2_control_demo_example_1",
    libraries = [":ros2_control_demo_example_1"],
    package_xml = "package.xml",
    plugin_category = "hardware_interface",
    plugins = ["ros2_control_demo_example_1.xml"],
    deps = [
        "@controller_manager//:ament_package",
        "@forward_command_controller//:ament_package",
        "@hardware_interface//:ament_package",
        "@joint_state_broadcaster//:ament_package",
        "@pluginlib//:ament_package",
        "@rclcpp//:ament_package",
        "@rclcpp_lifecycle//:ament_package",
        "@robot_state_publisher//:ament_package",
    ],
)
