from typing import Dict, List
import math

"""
A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!
"""


def read_data() -> List[int]:
    with open("data.txt", "r") as file:
        data = file.readline()
    return list(map(int, data.split(",")))


def calculate_fuel_cost(crabs: List[int], position: int) -> int:
    return sum([abs(position - crab) for crab in crabs])


def calculate_fuel_cost_part_2(crabs: List[int], position: int) -> int:
    return int(sum([abs(position - crab) * (abs(position - crab) + 1) / 2 for crab in crabs]))


def part_one() -> None:
    """
    Determine the horizontal position that the crabs can align to using the least fuel possible.

    Fixme: There are better ways to do this. We could probably use median or a numeric method of some kind.
    """
    print("Part 1:")
    crabs = read_data()
    min_position = min(crabs)
    max_position = max(crabs)

    fuel_costs = [
        calculate_fuel_cost(crabs=crabs, position=position) for position in range(min_position, max_position+1)
    ]

    print(f"How much fuel must they spend to align to that position?: {min(fuel_costs)}")


def part_two() -> None:
    """
    Determine the horizontal position that the crabs can align to using the
    least fuel possible so they can make you an escape route!
    """
    print("Part 2:")
    crabs = read_data()
    min_position = min(crabs)
    max_position = max(crabs)

    fuel_costs = [
        calculate_fuel_cost_part_2(crabs=crabs, position=position) for position in range(min_position, max_position+1)
    ]
    print(f"How much fuel must they spend to align to that position?: {min(fuel_costs)}")


if __name__ == "__main__":
    part_one()
    part_two()

