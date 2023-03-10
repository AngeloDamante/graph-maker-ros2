"""
    @file: Drawer.py
    @description: Class to draw elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import numpy as np
import cv2
from src.draw_elements import draw_node, draw_topic, compute_bb
from src.ENodeType import NodeType
from typing import Tuple

BG = (248, 255, 250)
TEXT = (16, 57, 133)
STEP = (50, 50)
BORDER = (10, 10)
t_failure = False, (-1, -1), (-1, -1)


class Drawer:
    """Drawer Class

    Attributes:
        origin: initial point of sheet (x,y)
        size: sheet dimension (w,h,ch)
        color_bg: (b,g,r)
        color_text: (b,g,r)
    """

    def __init__(self, origin: tuple, size: tuple, color_bg: tuple = None, color_text: tuple = None) -> None:
        if color_bg is None: color_bg = BG
        if color_text is None: color_text = TEXT

        # public
        self.origin = origin
        self.size = size
        self.color_bg = color_bg
        self.color_text = color_text

        # private
        self._cursor = self.origin
        self._step = STEP
        self._img = np.ndarray(size, dtype=np.uint8)
        self.reset_drawer()

    def _evaluate_bb(self, text: str) -> Tuple[bool, tuple, tuple]:
        """Evaluate bounding box for selected text

        :param text:
        :return: flag, top_left, bottom_right
        """
        tl, br = compute_bb(text, self._cursor, (0, 0))
        if br[0] > self.size[0]:
            self._cursor = (self.origin[0], br[1] + self._step[1])
            tl, br = compute_bb(text, self._cursor, (0, 0))

        # vertical space is finished
        if br[1] > self.size[1]: return False, tl, br

        # horizontal space is finished and vertical space too
        if br[0] > self.size[0] and (self._cursor[1] + self._step[1]) > self.size[1]: return False, tl, br
        return True, tl, br

    def is_valid(self) -> bool:
        # type
        if not isinstance(self.origin, tuple): return False
        if not isinstance(self.size, tuple): return False
        if not isinstance(self.color_bg, tuple): return False
        if not isinstance(self.color_text, tuple): return False

        # dim
        if len(self.origin) != 2: return False
        if len(self.size) != 3: return False
        if len(self.color_bg) != 3: return False
        if len(self.color_text) != 3: return False
        return True

    def reset_drawer(self) -> None:
        """Reset drawer with origin, size and color_bg

        :return: None
        """
        if not self.is_valid(): return
        self._img = np.ndarray((self.size[1], self.size[0], self.size[2]), dtype=np.uint8)
        self._cursor = self.origin
        self._img[:, :, :] = self.color_bg

    def set_img(self, img: np.ndarray) -> bool:
        """Image setter for the custom background

        :param img:
        :return: chek flag
        """
        if not self.is_valid(): return False
        if self._img.shape != img.shape: return False
        self._img = img
        return True

    def set_step(self, step: int) -> None:
        """Define space between elements (along_x,along_y)

        :param step: tuple
        :return: None
        """
        self._step = step

    def get_step(self) -> tuple:
        """Get space setted

        :return: tuple for step
        """
        return self._step

    def get_img(self) -> np.ndarray:
        """Getter method for Image with drawed elements

        :return: image
        """
        return self._img

    def add_node(self, node_name: str) -> Tuple[bool, tuple, tuple]:
        """Draw node into image, actual cursor will be updated

        :param node_name:
        :return: check flag
        """
        if not self.is_valid(): return t_failure
        b_valid, tl, br = self._evaluate_bb(node_name)
        if not b_valid: return t_failure

        self._img = draw_node(node_name, self._cursor, img_bg=self._img)
        self._cursor = (br[0] + self._step[0], tl[1])
        return True, tl, br

    def add_topic(self, topic_name: str) -> Tuple[bool, tuple, tuple]:
        """Draw topic into image, actual cursor will be updated

        :param topic_name:
        :return: check flag
        """
        if not self.is_valid(): return t_failure
        b_valid, tl, br = self._evaluate_bb(topic_name)
        if not b_valid: return t_failure

        self._img = draw_topic(topic_name, self._cursor, img_bg=self._img)
        self._cursor = (br[0] + self._step[0], tl[1])
        return True, tl, br

    def draw_connection(self, p_node: tuple, p_topic: tuple, action: NodeType) -> bool:
        """Draw connection between two points (node and topic)

        :param p_node:
        :param p_topic:
        :param action: PUB or SUB
        :return:
        """
        if not self.is_valid(): return False
        if action.value == NodeType.PUB.value:
            self._img = cv2.arrowedLine(self._img, p_node, p_topic, color=(0, 0, 0), thickness=1)
        if action.value == NodeType.SUB.value:
            self._img = cv2.arrowedLine(self._img, p_topic, p_node, color=(0, 0, 0), thickness=1)
        return True
