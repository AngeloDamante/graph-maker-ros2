import rclpy
from typing import List, Tuple
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from graph_maker.graph_maker_ros2.GraphMaker import GraphMaker
from graph_maker.graph_maker_ros2.src.ENodeType import NodeType


def make_matrix(nodes: list, topics: List[Tuple[str, list, list]]) -> List[list]:
    incidence_matrix = [len(nodes) * [NodeType.NULL] for _ in range(len(topics))]
    for t, (topic, l_pub, l_sub) in enumerate(topics):
        for pub in l_pub:
            for n, node in enumerate(nodes):
                if pub == node:
                    incidence_matrix[t][n] = NodeType.PUB
        for sub in l_sub:
            for n, node in enumerate(nodes):
                if sub == node:
                    incidence_matrix[t][n] = NodeType.SUB
    return incidence_matrix


class GraphMakerNode(Node):
    def __init__(self):
        super().__init__("graph_maker")
        self.publisher = self.create_publisher(Image, "debug", 5)
        self.timer = self.create_timer(1.5, self.maker)
        self.bridge = CvBridge()
        self.o_gm = GraphMaker()

    def maker(self):
        # get nodes and topics
        nodes = self.get_node_names()
        topics = [value[0] for value in self.get_topic_names_and_types()]

        # get subscribers and publishers for each topic
        topics_pub_sub = []
        for topic in topics:
            publishers = []
            for pub in self.get_publishers_info_by_topic(topic):
                publishers.append(pub.node_name)

            subscribers = []
            for sub in self.get_subscriptions_info_by_topic(topic):
                subscribers.append(sub.node_name)
            topics_pub_sub.append((topic, publishers, subscribers))

        # get matrix
        incidence_matrix = make_matrix(nodes, topics_pub_sub)

        # set drawer
        self.o_gm.set_nodes(nodes)
        self.o_gm.set_nodes(topics)
        self.o_gm.set_nodes(incidence_matrix)

        # make graph
        self.o_gm.make_graph()

        # log
        self.get_logger().info("rqt")

        # msg
        msg = self.bridge.cv2_to_imgmsg(self.o_gm.get_graph(), encoding="passthrough")
        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = GraphMakerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
