"""
    @file: Drawer.py
    @description: Class to draw elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import numpy as np
from src.draw_elements import draw_node, draw_topic, draw_connection

BG = (248, 255, 250)
TEXT = (16, 57, 133)
STEP = (50, 50)


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
        self._img = np.ndarray((size[1], size[0], size[2]), dtype=np.uint8)
        self.reset_drawer()

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
        self._cursor = self.origin
        self._img[:, :, :] = self.color_bg

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

    def add_node(self, node_name: str) -> bool:
        """Draw node into image, actual cursor will be updated

        :param node_name:
        :return: check flag
        """
        if not self.is_valid(): return False
        img_temp, tl, br = draw_node(node_name, self._cursor, self._img.copy())
        # FIXME: missing recheck for is_full
        if self._is_full(br): return False
        if br[0] > self.size[0]:
            self._cursor = (self.origin[0], br[1] + self._step[1])
            self._img, tl, br = draw_node(node_name, self._cursor, self._img.copy())
        else:
            self._img = img_temp
        print(f'tl = {tl}, br = {br}')
        self._cursor = (br[0] + self._step[0], tl[1])
        return True

    def add_topic(self, topic_name: str) -> bool:
        """Draw topic into image, actual cursor will be updated

        :param topic_name:
        :return: check flag
        """
        if not self.is_valid(): return False

        self._img, tl, br = draw_topic(topic_name, self._cursor, self._img)
        self._cursor = (br[0] + self._step[0], tl[1])
        return True

    # def _update_cursor(self, tl: tuple, br: tuple) -> None:
    #     """Update curson in accord to image dimension
    #
    #     There are two cases:
    #         1. right space is finished => reset x and move cursor to below
    #         2. right space is not finished => move cursor to the right
    #
    #     :param tl: top_left
    #     :param br: bottom_right
    #     :return: None
    #     """
    #     if br[0] > self.size[0]:
    #         self._cursor = (self.origin[0], br[1])
    #         self._img = draw_node(node_name, self._cursor, self._img.copy())
    #     self._cursor = (br[0] + self._step[0], tl[1])

    def _is_full(self, bottom_right: tuple) -> bool:
        """To handle no-space cases

        Two cases:
            1. vertical space is finished
            2. horizontal space is finished and vertical space too

        :param bottom_right:
        :return: flag to verify if there is space for another element
        """
        if bottom_right[1] > self.size[1]: return True
        if bottom_right[0] > self.size[0] and (self._cursor[1] + self._step[1]) > self.size[1]: return True
        return False
