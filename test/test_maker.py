import unittest
import cv2
from src.ENodeType import NodeType
from GraphMaker import GraphMaker

nodes = ['/camera/img_sender', '/n2', '/n3']
topics = ['/t1', '/t2', 't3', '/t4', 't5']
incidence_matrix = [[NodeType.PUB, NodeType.NULL, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                    [NodeType.NULL, NodeType.PUB, NodeType.SUB, NodeType.NULL, NodeType.SUB],
                    [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]

bad_incidence_matrix = [[NodeType.PUB, 0, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                        [NodeType.NULL, "PUB", NodeType.SUB, NodeType.NULL, NodeType.SUB],
                        [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]

class TestMaker(unittest.TestCase):
    def test_graph_maker(self):
        o_gm = GraphMaker(nodes, topics, incidence_matrix)
        self.assertEqual(o_gm.is_valid(), True)

    def test_graph_maker_failure(self):
        o_gm = GraphMaker(nodes, topics, bad_incidence_matrix)
        self.assertEqual(o_gm.is_valid(), False)

    def test_make_graph(self):
        o_gm = GraphMaker(nodes, topics, incidence_matrix)
        b_flag = o_gm.make_graph()
        self.assertEqual(b_flag, True)
        cv2.imwrite("image.png", o_gm.get_graph())



if __name__ == '__main__':
    unittest.main()
