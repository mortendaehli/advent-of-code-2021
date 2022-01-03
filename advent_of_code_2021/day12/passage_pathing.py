from collections import defaultdict
from functools import lru_cache
from typing import Dict


def read_cave_maps() -> Dict[str, str]:
    with open("data.txt", "r") as file:
        data = file.readlines()

    # All possible paths from each location:
    cave_map = defaultdict(list)
    for line in data:
        a, b = line.strip().split("-")
        cave_map[a].append(b)
        cave_map[b].append(a)
    return dict(cave_map)


def count_distinct_paths(cave_map: Dict[str, str], visit_small_caves_twice: bool) -> int:
    """
    Recursive function to map out all distinct paths starting at start and ending at end.

    :param cave_map: dictionary giving all possible paths for a given origin.
    :param visit_small_caves_twice: Boolean indicating if it is possible to visit a small cave twice.
    :return:
    """

    @lru_cache
    def _count_next_paths(origin: str, visited_before_set: frozenset, visit_one_small_twice: bool):
        if origin.islower():
            visited_before_set = visited_before_set.union({origin})
        n_paths = 0
        for target in cave_map[origin]:
            if target == "end":
                n_paths += 1
            elif target not in visited_before_set:
                n_paths += _count_next_paths(
                    origin=target, visited_before_set=visited_before_set, visit_one_small_twice=visit_one_small_twice
                )
            elif target != "start" and visit_one_small_twice:
                n_paths += _count_next_paths(
                    origin=target, visited_before_set=visited_before_set, visit_one_small_twice=False
                )
        return n_paths

    visited_before = frozenset()
    return _count_next_paths(
        origin="start", visited_before_set=visited_before, visit_one_small_twice=visit_small_caves_twice
    )


def part_one() -> int:
    cave_map = read_cave_maps()
    return count_distinct_paths(cave_map=cave_map, visit_small_caves_twice=False)


def part_two() -> int:
    cave_map = read_cave_maps()
    return count_distinct_paths(cave_map=cave_map, visit_small_caves_twice=True)


if __name__ == "__main__":
    print("Day 12: Passage Pathing")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: How many paths through this cave system are "
        f"there that visit small caves at most once?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(f"Part 2: Given these new rules, how many paths through this cave system are there??: {result_part_2}")
    print("-" * 80)
