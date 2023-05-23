## Sensor Fusion for SLAM
### Frontier Device Introduction
The Frontier device consists of an embedded computer, multi-camera system, lidar, and an inertial measurement unit (IMU). These sensors help in solving the SLAM (simultaneous localization and mapping) problem, which is crucial for robotics. [![[/snapshots/-XU54IsG8Vo/00-00-19.png]]](<https://youtu.be/-XU54IsG8Vo?t=18s>)

### Lidar, IMU, and Camera Fusion for SLAM [![[/snapshots/-XU54IsG8Vo/00-01-03.png]]](<https://youtu.be/-XU54IsG8Vo?t=62s>)
The cameras function as our eyes, while the lidar provides a point cloud of the environment by measuring the return time of fired lasers. The IMU is like our inner ear, giving us a sense of gravity and rotation speed. By fusing the data from these sensors, localization and mapping can be achieved. [![[/snapshots/-XU54IsG8Vo/00-00-37.png]]](<https://youtu.be/-XU54IsG8Vo?t=34s>)

### Loop Closure in SLAM
Loop closure is the recognition of the system returning to a previous position. This allows the correction of accumulated errors and leads to a better map. [![[/snapshots/-XU54IsG8Vo/00-01-37.png]]](<https://youtu.be/-XU54IsG8Vo?t=95s>)

### 3D Map Building
The 3D map is mainly built using the LiDAR, which provides a continuous stream of point clouds. The accurate knowledge of the robot's position is achieved by fusing the IMU. [![[/snapshots/-XU54IsG8Vo/00-02-33.png]]](<https://youtu.be/-XU54IsG8Vo?t=150s>)

### SLAM Applications
SLAM is essential for robotic autonomy, enabling remote inspection, mission planning, and dangerous tasks such as nuclear decommissioning. [![[/snapshots/-XU54IsG8Vo/00-05-39.png]]](<https://youtu.be/-XU54IsG8Vo?t=336s>)

### Factor Graph - Solving for SLAM [![[/snapshots/-XU54IsG8Vo/00-07-29.png]]](<https://youtu.be/-XU54IsG8Vo?t=444s>)
Factor graph is a technique used in solving the SLAM problem by modelling unknowns as nodes and the measurements from the sensors create relationships between these nodes. By combining these relationships, an optimization problem is formed, providing the best solution for the unknown positions and landmarks. 

### Loop Closure Correction
Loop closure correction warps the map to match reality by recognizing the same position in the map, which solves the SLAM problem for a specific situation but not generally due to noise and inaccuracy in the sensors. 

Source: [(161) SLAM Robot Mapping - Computerphile - YouTube](https://www.youtube.com/watch?v=-XU54IsG8Vo)
