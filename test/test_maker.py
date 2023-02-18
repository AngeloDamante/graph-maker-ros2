import unittest
from src.ENodeType import NodeType
from src.draw_elements import draw_node, draw_topic, compute_inner_bb, draw_connection
from GraphMaker import GraphMaker
import cv2

nodes = ['/camera/img_sender', '/n2', '/n3']
topics = ['/t1', '/t2', 't3', '/t4', 't5']
incidence_matrix = [[NodeType.PUB, NodeType.NULL, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                    [NodeType.NULL, NodeType.PUB, NodeType.SUB, NodeType.NULL, NodeType.SUB],
                    [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]

bad_incidence_matrix = [[NodeType.PUB, 0, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                        [NodeType.NULL, "PUB", NodeType.SUB, NodeType.NULL, NodeType.SUB],
                        [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]


class TestGraphicLib(unittest.TestCase):

    def test_create_node(self):
        img, _, _ = draw_node(nodes[0], [50, 50])
        cv2.imwrite("image_node.png", img)

    def test_create_topic(self):
        img, _, _ = draw_topic(topics[0], [50, 50])
        cv2.imwrite("image_topic.png", img)

    def test_compute_bb(self):
        img, tl, br = compute_inner_bb(nodes[0], [50, 50])
        cv2.imwrite("image_bb.png", img)

    def test_draw_connection(self):
        img = draw_connection((50, 50), (150, 100), action=NodeType.PUB)
        cv2.imwrite("image_pub.png", img)
        img = draw_connection((50, 50), (150, 100), action=NodeType.SUB)
        cv2.imwrite("image_sub.png", img)
        img = draw_connection((50, 50), (150, 100))
        cv2.imwrite("image_null.png", img)


class TestMaker(unittest.TestCase):

    def test_make_graph(self):
        o_gm = GraphMaker(nodes, topics, incidence_matrix)
        self.assertEqual(o_gm.is_valid(), True)

    def test_make_graph_failure(self):
        o_gm = GraphMaker(nodes, topics, bad_incidence_matrix)
        self.assertEqual(o_gm.is_valid(), False)


if __name__ == '__main__':
    unittest.main()
