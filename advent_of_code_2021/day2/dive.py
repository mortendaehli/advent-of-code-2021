from typing import List, Tuple


def load_data() -> List[Tuple[str, int]]:
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
    data = list(map(lambda x: (x[0], int(x[1])), [line.split() for line in data]))
    return data


def part_one() -> float:
    data = load_data()

    position_depth = 0
    position_length = 0

    for command, length in data:
        if command == "forward":
            position_length += length
        elif command == "up":
            position_depth -= length
        elif command == "down":
            position_depth += length

    return position_depth * position_length


def part_two() -> float:
    data = load_data()

    position_depth = 0
    position_length = 0
    aim = 0

    for command, units in data:
        if command == "forward":
            position_length += units
            position_depth += aim * units
        elif command == "up":
            aim -= units
        elif command == "down":
            aim += units

    return position_depth * position_length


if __name__ == "__main__":
    print("Day 2: Dive!")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: What do you get if you multiply your final horizontal position by your final depth?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: What do you get if you multiply your final horizontal position by your final depth?: {result_part_2}"
    )
    print("-" * 80)
