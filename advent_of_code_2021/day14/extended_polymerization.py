import string
from collections import Counter
from typing import Dict, Tuple


def read_data() -> Tuple[str, Dict[str, str]]:
    with open("data.txt", "r") as file:
        polymer_template, pair_insertions_data = file.read().split("\n\n")

    pair_insertions = {
        line.strip().split("->")[0].strip(): line.strip().split("->")[1].strip()
        for line in pair_insertions_data.split("\n")
    }
    pair_rules = {key: (key[0] + value, value + key[1]) for key, value in pair_insertions.items()}
    return polymer_template, pair_rules


def insert_pairs_in_counter(counter: Counter, pair_rules: dict) -> Counter:
    new_counter = {key: 0 for key in pair_rules.keys()}
    for key, value in counter.items():
        new_counter[pair_rules[key][0]] += value
        new_counter[pair_rules[key][1]] += value
    return Counter(new_counter)


def part_one() -> int:
    polymer_template, pair_rules = read_data()

    template_pairs = ["".join(p) for p in zip(polymer_template, polymer_template[1:])]
    template_pairs_counter = Counter(template_pairs)
    for t in range(10):
        template_pairs_counter = insert_pairs_in_counter(counter=template_pairs_counter, pair_rules=pair_rules)

    letter_counter = Counter({letter: 0 for letter in list(string.ascii_uppercase)})
    for key, value in template_pairs_counter.items():
        letter_counter[key[0]] += value

    letter_counter[polymer_template[-1]] += 1

    return max(letter_counter.values()) - min(filter(lambda x: x > 0, letter_counter.values()))


def part_two() -> int:
    polymer_template, pair_rules = read_data()

    template_pairs = ["".join(p) for p in zip(polymer_template, polymer_template[1:])]
    template_pairs_counter = Counter(template_pairs)
    for t in range(40):
        template_pairs_counter = insert_pairs_in_counter(counter=template_pairs_counter, pair_rules=pair_rules)

    letter_counter = Counter({letter: 0 for letter in list(string.ascii_uppercase)})
    for key, value in template_pairs_counter.items():
        letter_counter[key[0]] += value

    letter_counter[polymer_template[-1]] += 1

    return max(letter_counter.values()) - min(filter(lambda x: x > 0, letter_counter.values()))


if __name__ == "__main__":
    print("Day 14: Extended Polymerization")
    print("-" * 80)
    result_part_1 = part_one()
    print(
        f"Part 1: What do you get if you take the quantity of the most common element and subtract "
        f"the quantity of the least common element?: {result_part_1}"
    )
    print("-" * 80)
    result_part_2 = part_two()
    print(
        f"Part 2: What do you get if you take the quantity of the most common element and subtract "
        f"the quantity of the least common element?: {result_part_2}"
    )
    print("-" * 80)
