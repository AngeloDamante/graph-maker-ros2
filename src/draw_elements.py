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

SIZE = (720, 1280, 3)
BG_FRAME = np.ones(SIZE, np.uint8) * 245
BORDER = [10, 10]


def compute_inner_bb(name: str, origin: list, background: np.ndarray = None) -> Tuple[np.ndarray, tuple, tuple]:
    """Compute Bounding Box coords and image with text.

    :param name:
    :param origin:
    :param background:
    :return:
        image with applied text
        top_left(tuple)
        bottom_right(tuple)
    """
    if background is None: background = BG_FRAME.copy()
    img = background

    # extract dimension
    (lbl_w, lbl_h), _ = cv2.getTextSize(name, fontScale=0.8, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, thickness=1)

    # text
    ap = [origin[0], origin[1] + lbl_h]
    img = cv2.putText(img, name, ap, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(0, 0, 100))

    # bb
    top_left = [origin[0], origin[1]]
    bottom_right = [origin[0] + lbl_w, origin[1] + lbl_h]
    return img, tuple(top_left), tuple(bottom_right)


def draw_node(name: str, origin: list, background: np.ndarray = None, border=None) -> Tuple[np.ndarray, tuple, tuple]:
    """Create Graphic Node for input name.

    :param name:
    :param origin:
    :param background:
    :param border:
    :return:
        image(np.ndarray): image with ellipse
        top_left(tuple)
        bottom_right(tuple)
    """
    if border is None:
        border = BORDER
    img, top_left, bottom_right = compute_inner_bb(name, origin, background)
    center = [(top_left[0] + bottom_right[0]) // 2, (top_left[1] + bottom_right[1]) // 2]
    axis_x, axis_y = (bottom_right[0] - top_left[0]) // 2 + border[0], (bottom_right[1] - top_left[1]) // 2 + border[1]
    img = cv2.ellipse(img, center, (axis_x, axis_y), angle=0, startAngle=0, endAngle=360, color=(0, 0, 0), thickness=1)
    return img, tuple(top_left), tuple(bottom_right)


def draw_topic(name: str, origin: list, background: np.ndarray = None, border=None) -> Tuple[np.ndarray, tuple, tuple]:
    """Create graphic Topic for input name

    :param name:
    :param origin:
    :param background:
    :param border:
    :return:
        image(np.ndarray): image with rectangle
        top_left(tuple)
        bottom_right(tuple)
    """
    if border is None:
        border = BORDER
    img, top_left, bottom_right = compute_inner_bb(name, origin, background)
    top_left = (top_left[0] - border[0], top_left[1] - border[1])
    bottom_right = (bottom_right[0] + border[0], bottom_right[1] + border[1])
    img = cv2.rectangle(img, top_left, bottom_right, color=(0, 0, 0), thickness=2)
    return img, tuple(top_left), tuple(bottom_right)


def draw_connection(node: tuple, topic: tuple, background: np.ndarray = None, action: NodeType = NodeType.NULL) -> np.ndarray:
    """Draw connection between node and topic.

    :param node:
    :param topic:
    :param background:
    :param action: desired connection type
    :return: image with desired connection
    """
    if background is None:
        background = BG_FRAME.copy()
    if action.value == NodeType.NULL.value:
        return background
    if action.value == NodeType.PUB.value:
        return cv2.arrowedLine(background, node, topic, color=(0, 0, 0), thickness=1)
    if action.value == NodeType.SUB.value:
        return cv2.arrowedLine(background, topic, node, color=(0, 0, 0), thickness=1)
