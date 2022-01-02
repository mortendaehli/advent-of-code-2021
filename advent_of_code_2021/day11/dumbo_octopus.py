from typing import List

Array = List[List[int]]


def read_data() -> Array:
    with open("data.txt", "r") as file:
        data = file.readlines()
    return [list(map(int, line.strip())) for line in data]


def add_padding(array: Array, value: int = 9) -> Array:
    for row in array:
        row.insert(0, value)
        row.append(value)

    array.insert(0, [value] * len(array[0]))
    array.append([value] * len(array[0]))

    return array


def remove_padding(array: Array) -> Array:
    for row in array:
        row.pop(0)
        row.pop(-1)
    return array[1:-1]


def increment_neighbors_energy(array: Array, i: int, j: int) -> Array:
    """
    Adding padding then increment and remove padding.
    """
    array = add_padding(array)
    i += 1
    j += 1

    neighbors = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]

    for neighbor in neighbors:
        if array[neighbor[0]][neighbor[1]] != 0:
            array[neighbor[0]][neighbor[1]] += 1

    return remove_padding(array)


def part_one() -> int:

    array = read_data()
    total_flashes = 0
    n_timesteps = 100
    for t in range(n_timesteps):
        array = [[val + 1 for val in row] for row in array]
        while [val for row in array for val in row if val > 9]:
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if array[i][j] > 9:
                        total_flashes += 1
                        array[i][j] = 0
                        array = increment_neighbors_energy(array=array, i=i, j=j)

    return total_flashes


def part_two() -> int:
    array = read_data()
    t = 0

    while True:
        t += 1
        flash_at_step_counter = 0
        array = [[val + 1 for val in row] for row in array]
        while [val for row in array for val in row if val > 9]:
            for i in range(len(array)):
                for j in range(len(array[i])):
                    if array[i][j] > 9:
                        flash_at_step_counter += 1
                        array[i][j] = 0
                        array = increment_neighbors_energy(array=array, i=i, j=j)

        if flash_at_step_counter == 100:
            return t


if __name__ == "__main__":
    print("Day 11: Dumbo Octopus")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. "
        f"How many total flashes are there after 100 steps?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: If you can calculate the exact moments when the octopuses will all flash simultaneously, "
        f"you should be able to navigate through the cavern. "
        f"What is the first step during which all octopuses flash?: {result_part_2}"
    )
    print("-" * 80)
