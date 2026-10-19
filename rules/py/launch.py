from launch import LaunchService
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch.utilities import perform_substitutions
from launch import LaunchContext
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--launch-file", required=True)
    args = parser.parse_args()

    context = LaunchContext()
    launch_path = perform_substitutions(
        context,
        [
            PathJoinSubstitution([
                FindPackageShare(args.package),
                args.launch_file,
            ])
        ],
    )
    source = PythonLaunchDescriptionSource(launch_path)
    service = LaunchService()
    service.include_launch_description(
        source.get_launch_description(context)
    )
    return service.run()


if __name__ == "__main__":
    raise SystemExit(main())
