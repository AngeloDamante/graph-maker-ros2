from typing import Tuple
import math


def compute_min_distance_between_points(a: list, b: list) -> Tuple[tuple, tuple]:
    """Compute Minimum distance between list of points.

    Very useful to compute min distance between two bounding box.

    :param a: list of tuple
    :param b: list of tuple
    :return: two points that have minimum distance each other
    """
    point_a, point_b = a[0], b[0]
    min_distance = math.dist(point_a, point_b)
    for bx, by in b:
        for ax, ay in a:
            distance = math.dist([ax, ay], [bx, by])
            if min_distance > distance:
                min_distance = distance
                point_a, point_b = (ax, ay), (bx, by)
    return point_a, point_b
