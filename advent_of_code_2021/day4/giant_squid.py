from typing import List, Tuple, Dict, Optional
import re


class PlayBoard:
    def __init__(self, numbers: List[List[int]]) -> None:
        """
        Possible alternative structure: https://github.com/yatima1460/Bingo

        :param numbers:
        """

        if not len(numbers) == 5 and [len(row) for row in numbers] == [5]*5:
            raise ValueError(f"The PlayBoard needs to be of size 5x5 integers.")
        self.play_board: List[List[Optional[int]]] = numbers
        self.position: Dict[int, Tuple[int, int]] = dict()
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0],
            "diagonal": [0, 0]
        }

        self._init_board(play_board=self.play_board)

    def __repr__(self) -> str:
        return str(self.play_board)

    @property
    def sum_of_remaining_values(self) -> int:
        """ Sum remaining values on the play board. """
        return sum([sum([val for val in row if val]) for row in self.play_board])

    def _init_board(self, play_board: List[List[int]]) -> None:
        for i in range(len(play_board)):
            for j in range(len(play_board[i])):
                self.position[play_board[i][j]] = (i, j)

    def update_board(self, val: int) -> bool:
        if val in self.position:
            x, y = self.position[val]
            self.play_board[x][y] = None  # Removing the number
            self.update_bingo(x, y)
            return self.check_bingo()

    def update_bingo(self, x: int, y: int) -> None:
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1
        """
                if x == y == 2:
            self.bingo["diagonal"][0] += 1
            self.bingo["diagonal"][1] += 1
        elif x == y:
            self.bingo["diagonal"][0] += 1
        elif x + y == 4:
            self.bingo["diagonal"][1] += 1
        """

    def check_bingo(self) -> bool:
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]   # or 5 in self.bingo["diagonal"]


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
        data = file.readlines()[1:]

    cleaned_data = list(map(lambda x: re.split('\s+', x.strip()), data))

    play_boards: List[PlayBoard] = list()
    for i in range(1, len(data), 6):
        play_boards.append(PlayBoard(numbers=[list(map(int, x)) for x in cleaned_data[i: i+5]]))

    return play_boards


def load_data() -> Tuple[List[int], List[PlayBoard]]:
    """
    Loading the input data.
    """
    numbers, boards = read_numbers(), read_boards()
    return read_numbers(), read_boards()


def part_one() -> None:
    """
    To guarantee victory against the giant squid, figure out which board will win first.
    """
    print("Part 1: What will your final score be if you choose that board?")
    numbers, play_boards = load_data()

    winner = False
    while not winner:
        number = numbers.pop(0)
        for play_board in play_boards:
            if play_board.update_board(number):
                sum_of_remaining_values = play_board.sum_of_remaining_values
                print(f"The value of the remaining values: {sum_of_remaining_values} multiplied with last number:"
                      f" {number} is: {sum_of_remaining_values * number}")
                winner = True


def part_two() -> None:
    """
    Let the giant squid win.
    """
    print("Part 2: Figure out which board will win last. Once it wins, what would its final score be?")
    numbers, play_boards = load_data()

    number = numbers[0]
    play_board = play_boards[0]

    while play_boards:
        number = numbers.pop(0)
        for play_board in play_boards:
            if play_board.update_board(number):
                play_boards.remove(play_board)

    print(f"The value of the remaining values: {play_board.sum_of_remaining_values} multiplied with last number:"
          f" {number} is: {play_board.sum_of_remaining_values * number}")


if __name__ == "__main__":
    part_one()
    part_two()

