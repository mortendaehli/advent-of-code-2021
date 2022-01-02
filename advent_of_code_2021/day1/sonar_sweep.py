from typing import List


def load_array() -> List[float]:
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
    return list(map(float, data))


def calculate_measurements_larger_than_previous(array: List[float]) -> int:
    return sum(map(lambda i: array[i] - array[i - 1] > 0, range(1, len(array))))


def part_one() -> float:
    array = load_array()

    return calculate_measurements_larger_than_previous(array=array)


def part_two() -> float:
    array = load_array()

    sliding_window = 3
    # Need to consider the sum before index == sliding_window in a separate step in order to avoid wasted computation
    pre_sliding_array = [sum(array[:x]) / x for x in range(2, sliding_window)]

    sliding_array = pre_sliding_array + list(
        map(lambda i: sum(array[i - sliding_window : i]) / sliding_window, range(sliding_window, len(array)))
    )

    return calculate_measurements_larger_than_previous(array=sliding_array)


if __name__ == "__main__":
    print("Day 1: Sonar Sweep")
    print("-" * 80)
    result_part_1 = part_one()
    print(f"Part 1: How many measurements are larger than the previous measurement?: {result_part_1}")
    print("-" * 80)
    result_part_2 = part_two()
    print(f"Part 2: How many sums are larger than the previous sum?: {result_part_2}")
    print("-" * 80)
