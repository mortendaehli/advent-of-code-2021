from typing import List, Tuple

fold_directions = {"fold along y": "y", "fold along x": "x"}


def read_data() -> Tuple[List[Tuple[int]], List[Tuple[str, int]]]:
    with open("data.txt", "r") as file:
        points_data, folds_data = file.read().split("\n\n")

    points = [tuple([int(point) for point in line.split(",")]) for line in points_data.split("\n")]
    folds = list(map(lambda x: (x.split("=")[0][-1], int(x.split("=")[1])), folds_data.split("\n")))

    return points, folds


def run_fold(points: List[Tuple[int]], direction: str, fold_point: int) -> List[Tuple[int]]:
    """
    Folding a set of points by turning them around the given axis direction.
    """
    if direction == "x":
        return [(x, y) if x < fold_point else (fold_point - abs(x - fold_point), y) for x, y in points]
    else:
        return [(x, y) if y < fold_point else (x, fold_point - abs(y - fold_point)) for x, y in points]


def part_one() -> int:
    points, folds = read_data()

    direction, fold_point = folds[0]
    folded_points = run_fold(points=points, direction=direction, fold_point=fold_point)

    return len(set(folded_points))


def part_two() -> List[List[str]]:
    points, folds = read_data()

    for direction, fold_point in folds:
        points = run_fold(points=points, direction=direction, fold_point=fold_point)

    # The result is letters when we print the the unique points in the coordinate system.
    unique_points = set(points)
    result_shape = max([x for x, y in unique_points]) + 1, max([y for x, y in unique_points]) + 1
    result_array = [[" "] * result_shape[0] for x in range(result_shape[1])]

    # Flipping the axis to get the print vertical.
    for y, x in unique_points:
        result_array[x][y] = "x"

    return result_array


if __name__ == "__main__":
    print("Day 13: Transparent Origami")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: How many dots are visible after completing just the "
        f"first fold instruction on your transparent paper?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print("Part 2: What code do you use to activate the infrared thermal imaging camera system?: \n")
    [print(line) for line in result_part_2]
    print("\n" + "-" * 80)
