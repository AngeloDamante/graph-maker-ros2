import cv2
import numpy as np
from src.draw_elements import draw_node, draw_topic
from typing import Tuple

SIZE = (720, 1280, 3)
BG_FRAME = np.ones(SIZE, np.uint8) * 245
SPACE = (50, 50)  # space between nodes
INIT_NODES = (50, 50)
INIT_TOPICS = (150, 50)


class GraphMaker:
    def __init__(self, nodes: list, topics: list, incidence_matrix: list):
        self.nodes = nodes
        self.topics = topics
        self.incidence_matrix = incidence_matrix
        self.img = BG_FRAME
        self.size = SIZE
        self.space = SPACE

    def is_valid(self) -> bool:
        # PREconditions
        if len(self.nodes) != len(self.incidence_matrix): return False
        if len(self.topics) != len(self.incidence_matrix[0]): return False
        return True

    def set_nodes(self, nodes: list):
        self.nodes = nodes

    def set_topics(self, topics: list):
        self.topics = topics

    def set_incidence_matrix(self, matrix: list):
        self.incidence_matrix = matrix

    def set_size(self, size: tuple):
        self.size = size
        self.img = np.ones(self.size, np.uint8) * 245

    def set_space(self, space: tuple):
        self.space = space

    def get_graph(self) -> np.ndarray:
        return self.img




# TEMP
def make_graph(nodes: list, topics: list, incidence_matrix: list, background: np.ndarray = BG_FRAME) -> Tuple[
    bool, np.ndarray]:
    # PREconditions
    if len(nodes) != len(incidence_matrix): return False, np.zeros(background.shape)
    if len(topics) != len(incidence_matrix[0]): return False, np.zeros(background.shape)

    # create nodes
    origin_node = list(INIT_NODES)
    num_line = 1
    img = BG_FRAME.copy()
    for node in nodes:
        img, tl, br = draw_node(node, origin_node, background=img)
        origin_node = [br[0] + SPACE[0], tl[1]]

        if origin_node[0] > SIZE[0]:
            num_line += 1
            origin_node = [INIT_NODES[0], INIT_NODES[1] * num_line]

    # create topics TODO

    return True, img
