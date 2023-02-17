"""
    Virtual class to define Graphic Element.
"""
class GraphicElement:
    """GraphicElelement to handle graphic element and where it placed.

    Attributes:
        name(str)
        top_left(tuple)
        bottom_right(tuple)
    """
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

    def make_bb_points(self, border: tuple) -> list:
        """Make Bounding Box Points.

        :param border:
        :return: points of bounding box
        """
        points = []
        tl = (self.top_left[0] - border[0], self.top_left[1] - border[1])
        br = (self.bottom_right[0] + border[0], self.bottom_right[1] + border[1])

        px, py = tl[0], tl[1]
        ex, ey = br[0], br[1]
        while px < ex:
            points.append((px, py))
            points.append((px, ey))
            px += 1
        px, py = tl[0], tl[1]
        while py < ey:
            points.append((px, py))
            points.append((ex, py))
            py += 1
        return points