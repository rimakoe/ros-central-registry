load("@aspect_rules_py//py:defs.bzl", "py_binary")
load("@pip_ros//:requirements.bzl", "requirement")

def ros2_py_launch(
        name,
        package,
        launchfile,
        deps = [],
        data = [],
        **kwargs):
    """Creates a Python ROS launch executable."""

    py_binary(
        name = name,
        srcs = ["@rules_ros2//py:launch.py"],
        args = [
            "--package",
            package,
            "--launch-file",
            launchfile,
        ],
        deps = deps + [
            "@launch",
            "@launch_ros",
            "@lifecycle_msgs//:py",
            "@rclpy",
            requirement("packaging"),
        ],
        data = data + [launchfile],
        main = "@rules_ros2//py:launch.py",
        **kwargs
    )
