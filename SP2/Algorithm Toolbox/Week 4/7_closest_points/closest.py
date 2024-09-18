import sys
import math
from typing import List, Tuple

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other: 'Point'):
        return (self.x, self.y) < (other.x, other.y)

def distance_squared(p1: Point, p2: Point) -> float:
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def closest_pair_rec(points: List[Point], sorted_by_y: List[Point]) -> float:
    n = len(points)
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, distance_squared(points[i], points[j]))
        return min_dist

    mid = n // 2
    mid_x = points[mid].x

    left_points = points[:mid]
    right_points = points[mid:]
    
    left_y_sorted = [p for p in sorted_by_y if p.x <= mid_x]
    right_y_sorted = [p for p in sorted_by_y if p.x > mid_x]

    left_min_dist = closest_pair_rec(left_points, left_y_sorted)
    right_min_dist = closest_pair_rec(right_points, right_y_sorted)
    
    min_dist = min(left_min_dist, right_min_dist)

    # Check the strip area
    strip = [p for p in sorted_by_y if abs(p.x - mid_x) < math.sqrt(min_dist)]
    
    min_dist_strip = min_dist
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j].y - strip[i].y) ** 2 >= min_dist:
                break
            min_dist_strip = min(min_dist_strip, distance_squared(strip[i], strip[j]))

    return min_dist_strip

def closest_pair(points: List[Point]) -> float:
    points_sorted_by_x = sorted(points)
    points_sorted_by_y = sorted(points, key=lambda p: p.y)
    return closest_pair_rec(points_sorted_by_x, points_sorted_by_y)

if __name__ == '__main__':
    input_n = int(sys.stdin.readline().strip())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, sys.stdin.readline().strip().split())
        input_points.append(Point(x, y))

    min_distance_squared = closest_pair(input_points)
    min_distance = math.sqrt(min_distance_squared)
    print(f"{min_distance:.9f}")
