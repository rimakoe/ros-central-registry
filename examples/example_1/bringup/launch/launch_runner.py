from launch import LaunchContext, LaunchService
from launch.launch_description_sources import (
    PythonLaunchDescriptionSource,
)


def main():
    source = PythonLaunchDescriptionSource(
        "/home/developer/ares/workspace/integrations/ros-central-registry/examples/example_1/bringup/launch/rrbot.launch.py"
    )
    context = LaunchContext()

    launch_description = source.get_launch_description(context)

    launch_service = LaunchService()
    launch_service.include_launch_description(launch_description)

    return launch_service.run()


if __name__ == "__main__":
    raise SystemExit(main())
