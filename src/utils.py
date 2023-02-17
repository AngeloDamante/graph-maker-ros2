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

def compute_bb_points(top_left: tuple, bottom_right: tuple, border:tuple=None) -> list:
    """Make Bounding Box Points.

    :param top_left:
    :param bottom_right:
    :param border:
    :return: points of bounding box
    """
    if border is None: border = (0, 0)
    if top_left == bottom_right: return []

    tl = max((top_left[0] - border[0], top_left[1] - border[1]), (0,0))
    br = max((bottom_right[0] + border[0], bottom_right[1] + border[1]), (0,0))

    points = []
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