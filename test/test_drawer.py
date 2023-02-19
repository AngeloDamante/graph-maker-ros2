import unittest
from src.ENodeType import NodeType
from src.draw_elements import draw_node, draw_topic, compute_inner_bb, draw_connection
from src.Drawer import Drawer
import cv2


class TestDrawLib(unittest.TestCase):
    def test_create_node(self):
        img, _, _ = draw_node('/camera/img_sender', (50, 50))
        cv2.imwrite("image_node.png", img)

    def test_create_topic(self):
        img, _, _ = draw_topic('/camera/topic', (50, 50))
        cv2.imwrite("image_topic.png", img)

    def test_compute_bb(self):
        img, tl, br = compute_inner_bb('/camera/img_sender', (50, 50))
        cv2.imwrite("image_bb.png", img)

    def test_draw_connection(self):
        img = draw_connection((50, 50), (150, 100), action=NodeType.PUB)
        cv2.imwrite("image_pub.png", img)
        img = draw_connection((50, 50), (150, 100), action=NodeType.SUB)
        cv2.imwrite("image_sub.png", img)
        img = draw_connection((50, 50), (150, 100))
        cv2.imwrite("image_null.png", img)


class TestDrawer(unittest.TestCase):
    def test_make_drawer(self):
        o_drawer = Drawer(origin = (50,50), size = (1280,720,3))
        self.assertEqual(o_drawer.is_valid(), True)

    def test_make_drawer_failure(self):
        o_drawer = Drawer(origin = (50,50), size = (1280,72))
        self.assertEqual(o_drawer.is_valid(), False)


if __name__ == '__main__':
    unittest.main()
