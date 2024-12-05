from aocd import get_data
from collections import defaultdict


def is_correct_update(must_not_sees: dict[int, set[int]], update: list[int]) -> bool:
    must_not_see = set()

    for page in update:
        if page in must_not_see:
            return False
        must_not_see |= must_not_sees[page]

    return True


def find_median_of_unsorted_update(
    must_not_sees: dict[int, set[int]], update: list[int]
) -> int:
    target = len(update) // 2
    pageset = set(update)
    for page in update:
        if len(must_not_sees[page] & pageset) == target:
            return page

    raise ValueError("No median found")


def parse_input(data: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    must_not_sees = defaultdict(set)
    [rules, updates] = data.split("\n\n")

    for rule in rules.split("\n"):
        [x, y] = map(int, rule.split("|"))
        must_not_sees[y].add(x)

    return must_not_sees, [
        [int(page) for page in update.split(",")] for update in updates.splitlines()
    ]


def middle_item(items: list[int]) -> int:
    return items[len(items) // 2]


if __name__ == "__main__":
    data = get_data(day=5, year=2024)

    must_not_sees, updates = parse_input(data)

    answer = sum(
        middle_item(update)
        for update in updates
        if is_correct_update(must_not_sees, update)
    )

    print(answer)

    answer = sum(
        find_median_of_unsorted_update(must_not_sees, update)
        for update in updates
        if not is_correct_update(must_not_sees, update)
    )

    print(answer)
