"""
    Derived class Topic from GraphicElement.
"""
from lib_graph.GraphicElement import GraphicElement


class Topic(GraphicElement):
    def __init__(self, name: str, top_left: tuple, bottom_right: tuple):
        super().__init__(name, top_left, bottom_right)
