import unittest

import numpy as np

from src.ENodeType import NodeType
from src.draw_elements import draw_node, draw_topic, draw_connection, compute_bb
from src.Drawer import Drawer
import cv2

NODE = '/camera/img_sender'
TOPIC = '/camera/topic'


class TestDrawLib(unittest.TestCase):
    def test_create_node(self):
        img = draw_node(NODE, (50, 50))
        cv2.imwrite("image_node.png", img)

    def test_create_topic(self):
        img = draw_topic(TOPIC, (50, 50))
        cv2.imwrite("image_topic.png", img)

    def test_compute_bb(self):
        tl, br = compute_bb(NODE, (50, 50))
        self.assertEqual(tl, (40, 40))
        self.assertEqual(br, (275, 71))

    def test_draw_connection(self):
        img = draw_connection((50, 50), (150, 100), action=NodeType.PUB)
        cv2.imwrite("image_pub.png", img)
        img = draw_connection((50, 50), (150, 100), action=NodeType.SUB)
        cv2.imwrite("image_sub.png", img)
        img = draw_connection((50, 50), (150, 100))
        cv2.imwrite("image_null.png", img)

    def test_draw_node_in_little_image(self):
        img = np.ones((80, 80, 3), np.uint8)
        img = draw_node(NODE, (50, 50), img_bg=img)
        cv2.imwrite("little_image.png", img)


class TestDrawerClass(unittest.TestCase):
    def test_make_drawer(self):
        o_drawer = Drawer(origin=(50, 50), size=(1280, 720, 3))
        self.assertEqual(o_drawer.is_valid(), True)

    def test_make_drawer_failure(self):
        o_drawer = Drawer(origin=(50, 50), size=(1280, 72))
        self.assertEqual(o_drawer.is_valid(), False)
        o_drawer = Drawer(origin=(50, 50, 1), size=(1280, 72))
        self.assertEqual(o_drawer.is_valid(), False)
        o_drawer = Drawer(origin=(50, 50), size=(1280, 72, 3), color_bg=(100, 100))
        self.assertEqual(o_drawer.is_valid(), False)

    def test_draw_node(self):
        o_drawer = Drawer(origin=(50, 50), size=(640, 720, 3))
        for i in range(25):
            flag = o_drawer.add_node(NODE)
            if i <= 21:
                self.assertEqual(flag, True)
            else:
                self.assertEqual(flag, False)
        cv2.imwrite("image.png", o_drawer.get_img())

    def test_node_topic(self):
        o_drawer = Drawer(origin=(50, 50), size=(640, 720, 3))
        flag_node = o_drawer.add_node(NODE)
        flag_topic = o_drawer.add_topic(TOPIC)
        self.assertEqual(flag_topic and flag_node, True)
        cv2.imwrite("image.png", o_drawer.get_img())

    def test_reset_drawer(self):
        o_drawer = Drawer(origin=(50, 50), size=(640, 720, 3))
        cv2.imwrite("blank_image.png", o_drawer.get_img())
        o_drawer.add_node(NODE)
        cv2.imwrite("node_image.png", o_drawer.get_img())
        o_drawer.reset_drawer()
        cv2.imwrite("reset_image.png", o_drawer.get_img())

    def test_reset_drawer_failure(self):
        o_drawer = Drawer(origin=(50, 50, 1), size=(1280, 72))
        cv2.imwrite("blank_image.png", o_drawer.get_img())
        o_drawer.reset_drawer()


if __name__ == '__main__':
    unittest.main()
