# pan_tilt_platform_ros

## download and build docker
```
mkdir -p pan_tilt_platform_ros
cd pan_tilt_platform_ros/
git clone https://github.com/uptopia/pan_tilt_platform_ros.git src
cd pan_tilt_platform_ros/src/docker/
./build.sh
./run.sh
```
## run pan_tilt server and client
inside docker env
```
cd ~/work
catkin_make

<termianl 1>
roscore

<termianl 2>
. devel/setup.bash
rosrun pan_tilt_server pan_tilt_server.py

<termianl 3>
. devel/setup.bash
rosrun pan_tilt_client pan_tilt_client.py <pan_actual_deg> <tilt_actual_deg>

e.x. rosrun pan_tilt_client pan_tilt_client.py 10 20
```
