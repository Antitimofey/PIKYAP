# create main xacro file
```xacro
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro"  name="robot">
    <xacro:include filename="robot_core.xacro" />
</robot>
```
main xacro file includes all xacro file with robot description by this command
``` <xacro:include filename="robot_core.xacro" /> ```

# create xacro file with eobot description
## create empty hacro file
```
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" >

</robot>
```
note that this file doesnd have ```name``` filed in 2 line exept of main harco file
## seting up colors
```
<material name="white">
    <color rgba="1 1 1 1" />
</material>
```
## create base link
base link is the main node of robot, usually is it his center
```
<link name="base_link">

</link>
```
## create chassis
### create chassis joint
```
<joint name="chassis_joint" type="fixed">
    <parent link="base_link"/>
    <child link="chassis"/>
    <origin xyz="-0.1 0 0"/>
</joint>
```
here ```<origin xyz="-0.1 0 0"/>``` means placement  relative to the center
### create chassis link
```
<link name="chassis">
    <visual>
        <origin xyz="0.15 0 0.075"/>
        <geometry>
            <box size="0.3 0.3 0.15"/>
        </geometry>
        <material name="white"/>
    </visual>
</link>
```
## create wheels
### create wheel joint
```
<joint name="left_wheel_joined" type="continuous">
    <parent link="base_link"/>
    <child link="left_wheel"/>
    <origin xyz="0 0.175 0" rpy="-${pi/2} 0 0"/>
    <axis xyz="0 0 1"/>
</joint>
```
- ```type="continuous"``` means that the child link cat move relative to parent link
- ```rpy="-${pi/2} 0 0"``` means that we rotate wheel under clockwise on {pi/2} degree by x axis
- ```axis xyz="0 0 1"``` set the axis of rotation of the wheel
### create wheel link
```
<link name="left_wheel">
    <visual>
        <geometry>
            <cylinder radius="0.05" length="0.04"/>
        </geometry>
        <material name="black"/>
    </visual>
</link>
```
## create collision forms
```
<link name="chassis">
    <visual>
        <origin xyz="0.15 0 0.075"/>
        <geometry>
            <box size="0.3 0.3 0.15"/>
        </geometry>
        <material name="white"/>
    </visual>
    <collision>
        <origin xyz="0.15 0 0.075"/>
        <geometry>
            <box size="0.3 0.3 0.15"/>
        </geometry>
    </collision>
</link>
```
here we add  ```<collision>```  tag and copy there all code from ```visual``` except from ```material``` tag

# start simulation
- ```source install/setup.bash```
- ```colcon build && ros2 launch articubot_one rsp.launch.py``` in first term
- ```rviz2``` in second term
- ```ros2 run joint_state_publisher_gui joint_state_publisher_gui``` in third term if you have continuous joints