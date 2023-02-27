# create a pkg in the src file
ros2 pkg create graph_maker --build-type ament_python --dependencies rclpy
mv graph-maker-ros2/ graph_maker/graph_maker_ros2

# extract example node
cd graph_maker
mv graph_maker_ros2/node_example.py node_example.py