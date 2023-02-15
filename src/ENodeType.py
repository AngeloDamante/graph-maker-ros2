"""
    @file: ENodeType.py
    @description: Enum for Type of Node for ros2 framework
    @manteiner: AngeloDamante
    @license: GOGO
"""
from enum import Enum

class NodeType(Enum):
    PUB = "publisher"
    SUB = "subscriber"
    NULL= "nothing"