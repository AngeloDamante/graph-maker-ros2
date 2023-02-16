import unittest
from src.ENodeType import NodeType
from src.draw_elements import draw_node, draw_topic, compute_bb
from src.GraphMaker import make_graph
import cv2

topics = ['/t1', '/t2', 't3', '/t4', 't5']
nodes = ['/camera/img_sender', '/n2', '/n3']
incidence_matrix = [[NodeType.PUB, NodeType.NULL, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                    [NodeType.NULL, NodeType.PUB, NodeType.SUB, NodeType.NULL, NodeType.SUB],
                    [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]


class TestMaker(unittest.TestCase):

    def test_create_node(self):
        img, _, _ = draw_node(nodes[0], [50, 50])
        cv2.imwrite("image_node.png", img)

    def test_create_topic(self):
        img, _, _ = draw_topic(topics[0], [50, 50])
        cv2.imwrite("image_topic.png", img)

    def test_compute_bb(self):
        img, tl, br = compute_bb(nodes[0], [50, 50])
        cv2.imwrite("image_bb.png", img)


class TestGraph(unittest.TestCase):

    def test_make_graph(self):
        flag, img = make_graph(nodes, topics, incidence_matrix)
        cv2.imwrite("graph.png", img)
        self.assertEqual(flag, True)

    def test_make_graph_failure(self):
        pass


if __name__ == '__main__':
    unittest.main()
