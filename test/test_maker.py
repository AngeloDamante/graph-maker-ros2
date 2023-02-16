import unittest
from src.ENodeType import NodeType
from src.graph_maker import create_node, create_topic
import cv2

topics = ['/t1', '/t2', 't3', '/t4', 't5']
nodes = ['/camera/img_sender', '/n2', '/n3']
incidence_matrix = [[NodeType.PUB, NodeType.NULL, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                    [NodeType.NULL, NodeType.PUB, NodeType.SUB, NodeType.NULL, NodeType.SUB],
                    [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]


class TestMaker(unittest.TestCase):

    def test_create_node(self):
        img = create_node(nodes[0], [50, 50])
        cv2.imwrite("image_node.png", img)

    def test_create_topic(self):
        img = create_topic(topics[0], [50, 50])
        cv2.imwrite("image_topic.png", img)


class TestGraph(unittest.TestCase):
    def test_make_graph(self):
        pass

    def test_make_graph_failure(self):
        pass


if __name__ == '__main__':
    unittest.main()
