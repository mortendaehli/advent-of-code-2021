from typing import List


def load_array() -> List[float]:
    """
    Loading the input data and converting each line into int.
    """
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
    return [float(x) for x in data]


def calculate_measurements_larger_than_previous(array: List[float]) -> int:
    return sum(map(lambda i: array[i] - array[i - 1] > 0, range(1, len(array))))


def part_one() -> None:
    """
    Calculating many measurements are larger than the previous measurement.
    """
    print("Part 1: How many measurements are larger than the previous measurement?")
    array = load_array()

    result = calculate_measurements_larger_than_previous(array=array)
    print(f"Answer: {result}")


def part_two() -> None:
    """
    Calculating many measurements are larger than the previous measurement given sliding windows of 3.
    """
    print(
        "Part 2: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?"
    )
    sliding_window = 3
    array = load_array()

    # Need to consider the sum before index == sliding_window in a separate step in order to avoid wasted computation
    pre_sliding_array = [sum(array[:x]) / x for x in range(2, sliding_window)]
    sliding_array = pre_sliding_array + list(
        map(lambda i: sum(array[i-sliding_window: i]) / sliding_window, range(sliding_window, len(array)))
    )

    # Same function
    result = calculate_measurements_larger_than_previous(array=sliding_array)
    print(f"Answer: {result}")


if __name__ == "__main__":
    part_one()
    part_two()
