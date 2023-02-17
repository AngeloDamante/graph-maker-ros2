import unittest
from src.distance import compute_min_distance_between_points


class TestDistance(unittest.TestCase):
    def test_compute_min_distance(self):
        points_a = [(1, 2), (3, 4)]
        points_b = [(5, 3), (7, 1)]
        pa, pb = compute_min_distance_between_points(points_a, points_b)
        self.assertEqual((pa, pb), ((3, 4), (5, 3)))


if __name__ == '__main__':
    unittest.main()
