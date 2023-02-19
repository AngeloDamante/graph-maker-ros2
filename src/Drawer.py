"""
    @file: Drawer.py
    @description: Class to draw elements
    @manteiner: AngeloDamante
    @license: GOGO
"""
import numpy as np

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
        self._cursor = origin
        self._step = STEP
        self._img = np.ndarray(size, dtype=np.uint8) * color_bg

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
        self._cursor = self.origin
        self._img = np.ndarray(self.size, dtype=np.uint8) * self.color_bg

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

    # def add_node(self, node_name: str) -> bool:
    #     if not self.is_valid(): return False
