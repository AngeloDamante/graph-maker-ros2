import cv2
import numpy as np
from typing import Tuple

SIZE = (720, 1280, 3)
BG_FRAME = np.ones(SIZE, np.uint8) * 245
SPACE = (100, 100)  # space between nodes




def make_graph(nodes: list, topics: list, incidence_matrix: list, background: np.ndarray = BG_FRAME) -> Tuple[bool, np.ndarray]:
    # PREconditions
    if len(nodes) != len(incidence_matrix): return False, np.zeros(background.shape)
    if len(topics) != len(incidence_matrix[0]): return False, np.zeros(background.shape)

    # cv2.imwrite("image.png", img)
