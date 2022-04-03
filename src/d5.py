import math
from collections import defaultdict

file1 = open('d5.txt', 'r')
task_input = [line.strip() for line in file1.readlines()]


def create_point(str_tuple: str):
    parts = str_tuple.split(",")
    return Point(int(parts[0]), int(parts[1]))


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return hasattr(other, "x") and hasattr(other, "y") and other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash(self.x) * hash(self.y)

    def moved_by(self, x_offset, y_offset):
        return Point(self.x + x_offset, self.y + y_offset)


def create_segment(str_line_def):
    parts = str_line_def.split(" -> ")
    return Segment(create_point(parts[0]), create_point(parts[1]))


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_covered_points(self):
        points = []

        y_diff = self.end.y - self.start.y
        x_diff = self.end.x - self.start.x

        for step in range(max(abs(x_diff), abs(y_diff)) + 1):
            points.append(
                self.start.moved_by(
                    step * min(math.copysign(1, x_diff), abs(x_diff)),
                    step * min(math.copysign(1, y_diff), abs(y_diff))
                )
            )

        return points


segments = [create_segment(line) for line in task_input]

counts = defaultdict(int)
for segment in segments:
    for segment_point in segment.get_covered_points():
        counts[segment_point] += 1

print(sum([1 for v in counts.values() if v > 1]))
# 20196
