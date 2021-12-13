from typing import Tuple, List

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    p1: Point
    p2: Point


def read_data() -> List[Line]:
    with open("data.txt", "r") as file:
        data = file.readlines()
    return [Line(*[Point(*point.split(",")) for point in line.strip().split("->")]) for line in data]


def calculate_points_in_line(line: Line) -> List[Point]:
    pass


def part_one() -> None:
    """
    To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
    In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
    """
    print("Part 1: At how many points do at least two lines overlap?")
    lines = read_data()
    for line in lines:
        calculate_points_in_line(line=line)
    print("Yes!")


def part_two() -> None:
    pass


if __name__ == "__main__":
    part_one()
    part_two()

