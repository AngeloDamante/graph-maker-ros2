import unittest
from src.utils import compute_min_distance_between_points, compute_bb_points


class TestUtils(unittest.TestCase):
    def test_compute_min_distance(self):
        points_a = [(1, 2), (3, 4)]
        points_b = [(5, 3), (7, 1)]
        pa, pb = compute_min_distance_between_points(points_a, points_b)
        self.assertEqual((pa, pb), ((3, 4), (5, 3)))

    def test_compute_bb_points(self):
        points = compute_bb_points((1, 1), (3, 3))
        self.assertEqual(len(points), 8)

        points = compute_bb_points((1, 1), (3, 3), border=(1, 1))
        self.assertEqual(len(points), 16)

    def test_compute_bb_failure(self):
        points = compute_bb_points((1, 1), (1, 1))
        self.assertEqual(len(points), 0)


if __name__ == '__main__':
    unittest.main()
