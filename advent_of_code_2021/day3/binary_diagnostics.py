import math
from typing import Callable, List, Union


def load_data() -> List[str]:
    with open("data.txt", "r") as file:
        data = file.read().splitlines()
    return data


def round_half_up(number: Union[str, float], decimals: int = 0) -> int:
    multiplier = 10 ** decimals
    return int(math.floor(number * multiplier + 0.5) / multiplier)


def round_half_down(number: Union[str, float]) -> int:
    return round(float(number))


def process_position_mean(data: List[str]) -> List[float]:
    sums = [0] * len(data[0])
    for line in data:
        for i, d in enumerate(map(int, line)):
            sums[i] += d

    return [x / len(data) for x in sums]


def most_common_value(data: List[str], rounding_function: Callable = round) -> str:
    return "".join([str(rounding_function(number=x)) for x in process_position_mean(data=data)])


def least_common_value(data: List[str], rounding_function: Callable = round) -> str:
    return "".join([str(rounding_function(number=(-1 * (x - 1)))) for x in process_position_mean(data=data)])


def part_one() -> float:
    data = load_data()

    gamma = int(most_common_value(data=data), 2)
    epsilon = int(least_common_value(data=data), 2)

    return gamma * epsilon


def part_two() -> float:
    oxygen_generator_rating = load_data()
    co2_scrubber_rating = load_data()

    idx = 0
    while len(oxygen_generator_rating) > 1:
        _most_common = most_common_value(data=oxygen_generator_rating, rounding_function=round_half_up)[idx]
        oxygen_generator_rating = list(filter(lambda x: x[idx] == _most_common, oxygen_generator_rating))
        idx += 1
    oxygen_rating = int(oxygen_generator_rating[0], 2)

    idx = 0
    while len(co2_scrubber_rating) > 1:
        _least_common = least_common_value(data=co2_scrubber_rating, rounding_function=round_half_down)[idx]
        co2_scrubber_rating = list(filter(lambda x: x[idx] == _least_common, co2_scrubber_rating))
        idx += 1

    co2_rating = int(co2_scrubber_rating[0], 2)

    return oxygen_rating * co2_rating


if __name__ == "__main__":
    print("Day 3: Binary Diagnostic")
    print("-" * 80)
    result_part_1 = part_one()
    print(f"Part 1: What is the power consumption of the submarine?: {result_part_1}")
    print("-" * 80)
    result_part_2 = part_two()
    print(f"Part 2: What is the life support rating of the submarine?: {result_part_2}")
    print("-" * 80)
