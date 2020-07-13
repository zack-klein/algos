"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""

import math


# This times out, but works!
def kClosestBruteForce(self, points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    origin_x = 0
    origin_y = 0
    distances = {}

    # First build the hash table of distances
    for point in points:
        x = point[0]
        y = point[1]

        x_diff = (x - origin_x) ** 2
        y_diff = (y - origin_y) ** 2
        distance = math.sqrt(x_diff + y_diff)

        this_distance = distances.get(distance, [])
        this_distance.append(point)
        distances[distance] = this_distance

    # Then grab the bottom K distances
    top_k = []

    while len(top_k) < K:
        max_distance = min(distances.keys())  # $$$
        at_max_distance = distances[max_distance]  # list
        top_k += at_max_distance
        del distances[max_distance]

    return top_k


# Aaaaaand it can be done in two lines...
def kClosest(self, points, K):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
    return points[:K]
