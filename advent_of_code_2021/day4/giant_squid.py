from typing import List, Optional
import re
from dataclasses import dataclass
import itertools


@dataclass
class PlayBoard:
    numbers: List[List[Optional[int]]]


def read_numbers() -> List[int]:
    with open("data.txt", "r") as file:
        data = file.readline()
    return list(map(int, data.split(",")))


def read_boards() -> List[PlayBoard]:
    """
    Reading each board defined by a new line then 5 lists of 5 ints.
    Given the data format, this divides equally by 6 for possible performant mapping.
    """
    with open("data.txt", "r") as file:
        data = file.readlines()[2:]

    cleaned_data = list(map(lambda x: re.split('\s+', x.strip()), data))

    play_boards: List[PlayBoard] = list()
    for i in range(0, len(data), 6):
        play_boards.append(PlayBoard(numbers=[list(map(int, x)) for x in cleaned_data[i: i+5]]))

    return play_boards


def calculate_final_score(play_board: PlayBoard, number: int) -> int:
    """ Sum remaining values on the play board. """
    return sum([sum([val for val in row if val]) for row in play_board.numbers]) * number


def check_board_and_return_optional_score(play_board: PlayBoard, number: int) -> Optional[int]:
    # Check rows
    for row_num, row in enumerate(play_board.numbers):
        if number in row:
            row[row.index(number)] = None
            if row == [None] * 5:
                final_score = calculate_final_score(play_board=play_board, number=number)
                return final_score

    # check cols
    for n in range(5):
        col = [x[n] for x in play_board.numbers]
        if col == [None] * 5:
            final_score = calculate_final_score(play_board=play_board, number=number)
            return final_score

    else:
        return None


def part_one() -> None:
    """
    To guarantee victory against the giant squid, figure out which board will win first.
    """
    print("Part 1: What will your final score be if you choose that board?")
    numbers, play_boards = read_numbers(), read_boards()

    game_results = list()
    for number in numbers:
        for play_board in play_boards:
            score = check_board_and_return_optional_score(play_board=play_board, number=number)
            if score:
                game_results.append(score)


    print(f"The value of the remaining values multiplied with last number: is: {game_results[0]}")


def part_two() -> None:
    """
    Let the giant squid win.
    """
    print("Part 2: Figure out which board will win last. Once it wins, what would its final score be?")
    numbers, play_boards = read_numbers(), read_boards()

    game_results = list()
    for number in numbers:
        for play_board in play_boards:
            score = check_board_and_return_optional_score(play_board=play_board, number=number)
            if score:
                game_results.append(score)

    print(f"The value of the remaining values multiplied with last number is: {game_results[-1]}")


if __name__ == "__main__":
    part_one()
    part_two()

