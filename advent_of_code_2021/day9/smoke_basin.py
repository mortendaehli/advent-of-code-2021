from typing import List, Tuple


def read_data() -> List[List[int]]:
    """
    Reading a matrix of data.
    """
    with open("data.txt", "r") as file:
        data = file.readlines()
    return [list(map(int, line.strip())) for line in data]


def find_low_points(array: List[List[int]]) -> List[Tuple[int, int]]:
    """Looking at each point in the array to check if it is the lowest compared to adjacent points."""
    array_width = len(array[0])
    array_height = len(array)

    lowest = list()
    for i in range(array_height):
        for j in range(array_width):
            adjacent_is_higher = list()
            current = array[i][j]

            # Check up unless top row
            if i > 0:
                up = array[i - 1][j]
                adjacent_is_higher.append(current < up)

            # Check down unless bottom row
            if i + 1 < array_height:
                down = array[i + 1][j]
                adjacent_is_higher.append(current < down)

            # Check left unless left most column
            if j - 0 > 0:
                left = array[i][j - 1]
                adjacent_is_higher.append(current < left)

            # Check right unless right most column
            if j + 1 < array_width:
                right = array[i][j + 1]
                adjacent_is_higher.append(current < right)

            # If current is less than all adjacent observations, then the sum equals the length.
            if sum(adjacent_is_higher) == len(adjacent_is_higher):
                lowest.append((i, j))

    return lowest


def calculate_basin_size(x, y, array) -> int:
    """Calculating the basin size and marking visited points with x."""
    size = 0
    array_width = len(array[0])
    array_height = len(array)

    if array[x][y] == "x" or array[x][y] == 9:
        return size

    array[x][y] = "x"
    size += 1
    if y + 1 < array_width:
        size += calculate_basin_size(x, y + 1, array)
    if y - 1 >= 0:
        size += calculate_basin_size(x, y - 1, array)
    if x + 1 < array_height:
        size += calculate_basin_size(x + 1, y, array)
    if x - 1 >= 0:
        size += calculate_basin_size(x - 1, y, array)
    return size


def part_one() -> int:
    data = read_data()
    low_points = find_low_points(array=data)

    # Sum risk level is the height of itself + 1.
    return sum([int(data[r[0]][r[1]]) + 1 for r in low_points])


def part_two() -> int:
    data = read_data()

    low_points = find_low_points(array=data)

    basin_sizes_sorted = sorted(
        [calculate_basin_size(x=low_point[0], y=low_point[1], array=data) for low_point in low_points]
    )

    return basin_sizes_sorted[-1] * basin_sizes_sorted[-2] * basin_sizes_sorted[-3]


if __name__ == "__main__":
    print("Day 9: Smoke Basin")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: Find all of the low points on your heightmap. "
        f"What is the sum of the risk levels of all low points on your heightmap?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(f"Part 2: What do you get if you multiply together the sizes of the three largest basins?: {result_part_2}")
    print("-" * 80)
