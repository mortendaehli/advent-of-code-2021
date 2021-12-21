from typing import Dict, List


def read_fish() -> List[int]:
    with open("data.txt", "r") as file:
        data = file.readline()
    return list(map(int, data.split(",")))


def get_next_states(current_states: Dict[int, int]) -> Dict[int, int]:
    next_states = {i: current_states[i+1 if i < 8 else 0]for i in range(9)}

    # Reset adult fish to state 6.
    next_states[6] += current_states[0]

    return next_states


def get_initial_state(starting_fish: List[int]) -> Dict[int, int]:
    return {i: starting_fish.count(i) for i in range(9)}


def part_one() -> None:
    """
    Find a way to simulate lanternfish.

    How many lanternfish would there be after 80 days? 379114
    """
    print("Part 1: Find a way to simulate lanternfish.")
    initial_state = get_initial_state(starting_fish=read_fish())

    current_state = initial_state
    for i in range(80):
        current_state = get_next_states(current_states=current_state)
    final_count = sum([x for x in current_state.values()])

    print(f"How many lanternfish would there be after 80 days?: {final_count}")


def part_two() -> None:
    """
    Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
    """
    print("Part 2: Find a way to simulate lanternfish.")
    initial_state = get_initial_state(starting_fish=read_fish())

    current_state = initial_state
    for i in range(256):
        current_state = get_next_states(current_states=current_state)
    final_count = sum([x for x in current_state.values()])

    print(f"How many lanternfish would there be after 256 days?: {final_count}")


if __name__ == "__main__":
    part_one()
    part_two()

