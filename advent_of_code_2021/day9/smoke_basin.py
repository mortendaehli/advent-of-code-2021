from typing import List


def read_data() -> List[List[int]]:
    """
    Reading a matrix of data.
    """
    with open("data.txt", "r") as file:
        data = file.readlines()
    return [list(map(int, line.strip())) for line in data]


def part_one() -> float:
    """
    Find all of the low points on your heightmap.
    What is the sum of the risk levels of all low points on your heightmap?
    """
    data = read_data()  # noqa
    return 1


def part_two() -> float:
    """ """
    data = read_data()  # noqa
    return 1


if __name__ == "__main__":
    result1 = part_one()
    print(f"What is the sum of the risk levels of all low points on your heightmap?: {result1}")

    result2 = part_two()
    print(f"What do you get if you add up all of the output values?: {result2}")
