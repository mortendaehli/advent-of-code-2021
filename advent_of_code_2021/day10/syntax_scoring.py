from typing import List


def read_data() -> List[str]:
    with open("data.txt", "r") as file:
        data = file.readlines()
    return data


def get_error_score(line: str) -> int:
    symbol_dict = {"]": "[", ")": "(", ">": "<", "}": "{"}
    symbol_values = {"]": 57, ")": 3, ">": 25137, "}": 1197}

    symbol_list = list()
    for char in line:
        if char in symbol_dict.values():
            symbol_list.append(char)
        elif char in symbol_dict.keys():
            if symbol_list[-1] == symbol_dict.get(char):
                symbol_list = symbol_list[:-1]
            else:
                return symbol_values.get(char)

    return 0


def get_incomplete_stub(line: str) -> str:
    symbol_dict_close = {"]": "[", ")": "(", ">": "<", "}": "{"}

    symbol_list = list()
    for char in line:
        if char in symbol_dict_close.values():
            symbol_list.append(char)
        elif char in symbol_dict_close.keys():
            if symbol_list[-1] == symbol_dict_close.get(char):
                symbol_list = symbol_list[:-1]
            else:
                break
    else:
        return line

    return ""


def score_incomplete_stub(stub: str) -> int:
    symbol_dict_close = {"]": "[", ")": "(", ">": "<", "}": "{"}
    symbol_dict_open = {"[": "]", "(": ")", "<": ">", "{": "}"}
    symbol_values = {"]": 2, ")": 1, ">": 4, "}": 3}

    score = 0
    symbol_list = list()
    for char in stub:
        if char in symbol_dict_close.values():
            symbol_list.append(char)
        elif char in symbol_dict_close.keys():
            if symbol_list[-1] == symbol_dict_close.get(char):
                symbol_list = symbol_list[:-1]

    while len(symbol_list) > 0:
        x = symbol_dict_open.get(symbol_list[-1])
        score = score * 5 + symbol_values.get(x)
        symbol_list = symbol_list[:-1]

    return score


def part_one() -> int:
    data = read_data()

    return sum(map(get_error_score, data))


def part_two() -> int:
    data = read_data()

    # Not possible to return None if stub is complete. There is probably a better way to do this...
    incomplete_stubs = [x for x in map(get_incomplete_stub, data) if x]
    stubs_score = list(map(score_incomplete_stub, incomplete_stubs))

    stubs_score.sort()
    middle_score = int((len(stubs_score) - 1) / 2)

    return stubs_score[int(middle_score)]


if __name__ == "__main__":
    print("Day 10: Syntax Scoring")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: Find all of the low points on your heightmap. "
        f"What is the sum of the risk levels of all low points on your heightmap?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: Find the completion string for each incomplete line, score the completion strings, "
        f"and sort the scores. What is the middle score?: {result_part_2}"
    )
    print("-" * 80)
