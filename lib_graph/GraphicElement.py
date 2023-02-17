"""
    Virtual class to define Graphic Element.
"""
class GraphicElement:
    def __init__(self, name: str, top_left: tuple, bottom_right: tuple):
        self.name = name
        self.top_left = top_left
        self.bottom_right = bottom_right

    def set_name(self, name: str):
        self.name = name

    def set_top_left(self, tl: tuple):
        self.top_left = tl

    def set_bottom_right(self, br: tuple):
        self.bottom_right = br

    def make_bb_points(self) -> set:
        raise NotImplementedError()