"""
    @file: GraphMaker.py
    @description: Class to make graph with ros2 elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import numpy as np
from src.ENodeType import NodeType
from src.Drawer import Drawer, BORDER
from src.utils import compute_bb_points, compute_min_distance_between_points

SIZE = (720, 1280, 3)
ORIGIN_NODE = (50, 50)
ORIGIN_TOPIC = (50, 550)


class GraphMaker:
    """GraphMaker to read and draw indices matrix

    Example parameters:
        nodes = [a, b, c]
        topics = [d, e]

    Incidence Matrix Form:
            a       b       c
        d   PUB     NULL    SUB
        e   SUB     PUB     NULL

    Attributes:
        nodes
        topics
        incidence_matrix
    """

    def __init__(self, nodes: list, topics: list, incidence_matrix: list):
        self.nodes = nodes
        self.topics = topics
        self.incidence_matrix = incidence_matrix
        self._node_drawer = Drawer(ORIGIN_NODE, SIZE)  # default drawer for nodes
        self._topic_drawer = Drawer(ORIGIN_TOPIC, SIZE)  # default drawer for topics

    def is_valid(self) -> bool:
        # PREconditions
        if len(self.nodes) != len(self.incidence_matrix): return False
        if len(self.topics) != len(self.incidence_matrix[0]): return False
        if not all(isinstance(x, str) for x in self.nodes): return False
        if not all(isinstance(x, str) for x in self.topics): return False
        if not all(isinstance(x[i], NodeType)
                   for x in self.incidence_matrix
                   for i in range(len(self.incidence_matrix))): return False
        return True

    def set_nodes(self, nodes: list) -> None:
        self.nodes = nodes

    def set_topics(self, topics: list) -> None:
        self.topics = topics

    def set_incidence_matrix(self, matrix: list) -> None:
        self.incidence_matrix = matrix

    def get_graph(self) -> np.ndarray:
        return self._node_drawer.get_img()

    def make_graph(self) -> bool:
        """Make Graph from incidence_matrix

        :return: check flag
        """
        if not self.is_valid(): return False
        if not self._node_drawer.is_valid(): return False
        if not self._topic_drawer.is_valid(): return False

        # draw topics with topic drawer
        drawed_topics = []
        for topic in self.topics:
            b_flag, tl, br = self._topic_drawer.add_topic(topic)
            if b_flag: drawed_topics.append({'name': topic, 'tl': tl, 'br': br})

        # draw nodes with node drawer
        self._node_drawer.set_img(self._topic_drawer.get_img())
        drawed_nodes = []
        for node in self.nodes:
            b_flag, tl, br = self._node_drawer.add_node(node)
            if b_flag: drawed_nodes.append({'name': node, 'tl': tl, 'br': br})

        # draw connections with node drawer
        for n in range(len(self.nodes)):
            for t in range(len(self.topics)):
                if self.incidence_matrix[n][t].value != NodeType.NULL.value:
                    _node = [item for item in drawed_nodes if item['name'] == self.nodes[n]][0]
                    _topic = [item for item in drawed_topics if item['name'] == self.topics[t]][0]
                    _bb_node = compute_bb_points(_node['tl'], _node['br'], BORDER)
                    _bb_topic = compute_bb_points(_topic['tl'], _topic['br'], BORDER)
                    _min_n, _min_t = compute_min_distance_between_points(_bb_node, _bb_topic)
                    self._node_drawer.draw_connection(_min_n, _min_t, self.incidence_matrix[n][t])
        return True
