from typing import List


def read_data() -> List[tuple]:
    """Return a list of tuples with digits and readouts."""
    with open("data.txt", "r") as file:
        data = file.readlines()
    return list(map(lambda x: (x[0].split(), x[1].split()), [line.strip().split(" | ") for line in data]))


def part_one() -> float:
    """
    In the output values, how many times do digits 1, 4, 7, or 8 appear?
    """
    data = read_data()
    readout_lengths = list(map(lambda x: [len(i) for i in x[1]], data))

    # Sum all readouts that are of length 2, 3, 4 and 7. These correspond to digits 1, 7, 4 and 8
    return len([item for sublist in readout_lengths for item in sublist if item in (2, 3, 4, 7)])


def part_two() -> float:
    """
    For each entry, determine all of the wire/segment connections and decode the four-digit output values.
    What do you get if you add up all of the output values?
    """
    counter = 0
    data = read_data()
    for line in data:
        digits, readouts = line

        digit_length_to_digit = {length: set(digit) for digit in digits if (length := len(digit)) in (2, 4)}

        number = ""
        for readout in readouts:
            length = len(readout)
            if length == 2:
                number += "1"
            elif length == 4:
                number += "4"
            elif length == 3:
                number += "7"
            elif length == 7:
                number += "8"
            elif length == 5:  # 3, 2 and 5
                read = set(readout)
                if len(read & digit_length_to_digit[2]) == 2:
                    number += "3"
                elif len(read & digit_length_to_digit[4]) == 2:
                    number += "2"
                else:
                    number += "5"
            elif length == 6:  # 6, 9 and 0
                read = set(readout)
                if len(read & digit_length_to_digit[2]) == 1:
                    number += "6"
                elif len(read & digit_length_to_digit[4]) == 4:
                    number += "9"
                else:
                    number += "0"
            else:
                raise ValueError("We don't expect lengths above 6")
        counter += int(number)
    return counter


if __name__ == "__main__":
    print("Day 8: Seven Segment Search")
    print("-" * 80)
    result_part_1 = part_one()
    print(f"Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?: {result_part_1}")
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: For each entry, determine all of the wire/segment connections and decode the four-digit output "
        f" values. What do you get if you add up all of the output values?: {result_part_2}"
    )
    print("-" * 80)
