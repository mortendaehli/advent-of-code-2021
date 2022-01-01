from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Line:
    p1: Tuple[int, int]
    p2: Tuple[int, int]

    @property
    def is_horizontal(self) -> bool:
        return (self.p1[0] != self.p2[0]) & (self.p1[1] == self.p2[1])

    @property
    def is_vertical(self) -> bool:
        return (self.p1[1] != self.p2[1]) & (self.p1[0] == self.p2[0])

    @property
    def is_diagonal(self) -> bool:
        return abs(self.p1[0] - self.p2[0]) == abs(self.p1[1] - self.p2[1])


def read_data() -> List[Line]:
    with open("data.txt", "r") as file:
        data = file.readlines()
    return [Line(*[tuple([int(i) for i in point.split(",")]) for point in line.strip().split("->")]) for line in data]


def calculate_points_in_line(line: Line, include_diagonal: bool) -> List[Tuple[int, int]]:

    (x1, y1), (x2, y2) = sorted([line.p1, line.p2])

    if line.is_horizontal or line.is_vertical:
        return [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
    elif line.is_diagonal & include_diagonal:
        if y1 < y2:
            return [(x, y1 + i) for i, x in enumerate(range(x1, x2 + 1))]
        else:
            return [(x, y1 - i) for i, x in enumerate(range(x1, x2 + 1))]
    else:
        return []


def part_one() -> int:
    lines = read_data()
    point_list = list()
    for line in lines:
        point_list += calculate_points_in_line(line=line, include_diagonal=False)

    return sum([1 for x in Counter(point_list).items() if x[1] >= 2])


def part_two() -> int:
    lines = read_data()
    point_list = list()
    for line in lines:
        point_list += calculate_points_in_line(line=line, include_diagonal=True)

    return len([i for i in Counter(point_list).values() if i > 1])


if __name__ == "__main__":
    print("Day 5: Hydrothermal Venture")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: Consider only horizontal and vertical lines."
        f"At how many points do at least two lines overlap?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(f"Part 2: Consider all of the lines." f"At how many points do at least two lines overlap?: {result_part_2}")
    print("-" * 80)
