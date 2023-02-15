import unittest
from src.ENodeType import NodeType

topics = ['/t1', '/t2', 't3', '/t4', 't5']
nodes = ['/n1', '/n2', '/n3']
incidence_matrix = [[NodeType.PUB, NodeType.NULL, NodeType.SUB, NodeType.NULL, NodeType.PUB],
                    [NodeType.NULL, NodeType.PUB, NodeType.SUB, NodeType.NULL, NodeType.SUB],
                    [NodeType.PUB, NodeType.PUB, NodeType.PUB, NodeType.SUB, NodeType.SUB]]

class TestMaker(unittest.TestCase):

    def test_make_graph(self):
        # ordinary test
        pass

    def test_make_graph_failure(self):
        # empty case
        # Not correct format
        pass


if __name__ == '__main__':
    unittest.main()
