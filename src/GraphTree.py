import cv2
import numpy as np
from src.graph_maker import create_node, create_topic
from typing import Tuple

SIZE = (720, 1280, 3)
BG_FRAME = np.ones(SIZE, np.uint8) * 245
SPACE = (50, 50)  # space between nodes
INIT_NODES = (50, 50)
INIT_TOPICS = (150, 50)



def make_graph(nodes: list, topics: list, incidence_matrix: list, background: np.ndarray = BG_FRAME) -> Tuple[bool, np.ndarray]:
    # PREconditions
    if len(nodes) != len(incidence_matrix): return False, np.zeros(background.shape)
    if len(topics) != len(incidence_matrix[0]): return False, np.zeros(background.shape)

    # create nodes
    origin_node = list(INIT_NODES)
    num_line = 1
    img = BG_FRAME.copy()
    for node in nodes:
        img, tl, br = create_node(node, origin_node, background=img)
        origin_node = [br[0] + SPACE[0], tl[1]]

        if origin_node[0] > SIZE[0]:
            num_line += 1
            origin_node = [INIT_NODES[0], INIT_NODES[1] * num_line]

    # create topics TODO

    return True, img



