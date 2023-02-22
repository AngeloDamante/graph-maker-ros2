"""
    @file: draw_elements.py
    @description: Library to draw elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import cv2
import numpy as np
from typing import Tuple
from src.ENodeType import NodeType

# default image
SIZE = (720, 1280, 3)
WHITE = (254, 254, 254)
IMG_BG = np.ones(SIZE, np.uint8)
IMG_BG[:, :, :] = WHITE
BORDER = [10, 10]


def compute_bb(name: str, origin: tuple, border: tuple = (10, 10)) -> Tuple[tuple, tuple]:
    """Compute bounding box coords with border

    For inner bounding box, select border = (0,0)

    :param name:
    :param origin:
    :param border:
    :return: top_left, bottom_right
    """
    (lbl_w, lbl_h), _ = cv2.getTextSize(name, fontScale=0.8, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, thickness=1)
    top_left = (origin[0] - border[0], origin[1] - border[1])
    bottom_right = (origin[0] + lbl_w + border[0], origin[1] + lbl_h + border[1])
    return top_left, bottom_right


def draw_node(name: str, origin: tuple, border: tuple = (10, 10), img_bg: np.ndarray = None) -> np.ndarray:
    """Create Graphic Node for input name

    :param name:
    :param origin:
    :param img_bg:
    :param border:
    :return: image(np.ndarray): image with ellipse
    """
    if img_bg is None: img_bg = IMG_BG.copy()
    top_left, bottom_right = compute_bb(name, origin, (0, 0))
    c = [(top_left[0] + bottom_right[0]) // 2, (top_left[1] + bottom_right[1]) // 2]
    axis_x, axis_y = (bottom_right[0] - top_left[0]) // 2 + border[0], (bottom_right[1] - top_left[1]) // 2 + border[1]
    ap = [origin[0], bottom_right[1]]
    img = cv2.putText(img_bg, name, ap, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(0, 0, 100))
    img = cv2.ellipse(img, c, (axis_x, axis_y), angle=0, startAngle=0, endAngle=360, color=(0, 0, 0), thickness=1)
    return img


def draw_topic(name: str, origin: tuple, border: tuple = (10, 10), img_bg: np.ndarray = None, ) -> np.ndarray:
    """Create graphic Topic for input name

    :param name:
    :param origin:
    :param img_bg:
    :param border:
    :return: image(np.ndarray): image with rectangle
    """
    if img_bg is None: img_bg = IMG_BG.copy()
    top_left, bottom_right = compute_bb(name, origin, (0, 0))
    ap = [origin[0], bottom_right[1]]
    img = cv2.putText(img_bg, name, ap, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(0, 0, 100))
    top_left, bottom_right = compute_bb(name, origin, border)
    img = cv2.rectangle(img, top_left, bottom_right, color=(0, 0, 0), thickness=2)
    return img


def draw_connection(node: tuple, topic: tuple, img_bg: np.ndarray = None, action: NodeType = NodeType.NULL) -> np.ndarray:
    """Draw connection between node and topic.

    :param node:
    :param topic:
    :param img_bg:
    :param action: desired connection type
    :return: image with desired connection
    """
    if img_bg is None:
        img_bg = IMG_BG.copy()
    if action.value == NodeType.NULL.value:
        return img_bg
    if action.value == NodeType.PUB.value:
        return cv2.arrowedLine(img_bg, node, topic, color=(0, 0, 0), thickness=1)
    if action.value == NodeType.SUB.value:
        return cv2.arrowedLine(img_bg, topic, node, color=(0, 0, 0), thickness=1)
