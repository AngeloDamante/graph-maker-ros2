"""
    @file: GraphMaker.py
    @description: Class to make graph with ros2 elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import numpy as np
from src.ENodeType import NodeType
from src.Drawer import Drawer
from typing import Tuple

SIZE = (720, 1280, 3)
ORIGIN = (50, 50)


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
        self._drawer = Drawer(ORIGIN, SIZE)

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

    def set_drawer(self, drawer: Drawer) -> None:
        self._drawer = drawer

    def get_graph(self) -> np.ndarray:
        return self._drawer.get_img()

    def make_graph(self) -> bool:
        if not self.is_valid(): return False
        # TODO

# # TEMP
# def make_graph(nodes: list, topics: list, incidence_matrix: list, background: np.ndarray = BG_FRAME) -> Tuple[
#     bool, np.ndarray]:
#     # PREconditions
#     if len(nodes) != len(incidence_matrix): return False, np.zeros(background.shape)
#     if len(topics) != len(incidence_matrix[0]): return False, np.zeros(background.shape)
#
#     # create nodes
#     origin_node = list(INIT_NODES)
#     num_line = 1
#     img = BG_FRAME.copy()
#     for node in nodes:
#         img, tl, br = draw_node(node, origin_node, background=img)
#         origin_node = [br[0] + SPACE[0], tl[1]]
#
#         if origin_node[0] > SIZE[0]:
#             num_line += 1
#             origin_node = [INIT_NODES[0], INIT_NODES[1] * num_line]
#
#     # create topics TODO
#
#     return True, img
