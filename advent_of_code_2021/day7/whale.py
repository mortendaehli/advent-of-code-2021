from typing import List


def read_data() -> List[int]:
    with open("data.txt", "r") as file:
        data = file.readline()
    return list(map(int, data.split(",")))


def calculate_fuel_cost(crabs: List[int], position: int) -> int:
    return sum([abs(position - crab) for crab in crabs])


def calculate_fuel_cost_part_2(crabs: List[int], position: int) -> int:
    return int(sum([abs(position - crab) * (abs(position - crab) + 1) / 2 for crab in crabs]))


def part_one() -> int:
    crabs = read_data()
    min_position = min(crabs)
    max_position = max(crabs)

    fuel_costs = [
        calculate_fuel_cost(crabs=crabs, position=position) for position in range(min_position, max_position + 1)
    ]

    return min(fuel_costs)


def part_two() -> int:
    crabs = read_data()
    min_position = min(crabs)
    max_position = max(crabs)

    return min(
        [
            calculate_fuel_cost_part_2(crabs=crabs, position=position)
            for position in range(min_position, max_position + 1)
        ]
    )


if __name__ == "__main__":
    print("Day 7: The Treachery of Whales")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: Determine the horizontal position that the crabs can align to using the least fuel possible. "
        f"How much fuel must they spend to align to that position?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: Determine the horizontal position that the crabs can align to using the least fuel possible so "
        f"they can make you an escape route! How much fuel must they spend to align to that position?: {result_part_2}"
    )
    print("-" * 80)
