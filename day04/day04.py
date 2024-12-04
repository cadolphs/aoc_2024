import numpy as np

from aocd import get_data


def find_all_occurrences(word: str, puzzle: np.array) -> int:
    word = np.array(list(word))

    return (
        find_all_horizontal(word, puzzle)
        + find_all_vertical(word, puzzle)
        + find_all_diagonal(word, puzzle)
    )


def find_all_horizontal(word: np.array, puzzle: np.array) -> int:
    return sum(find_horizontal(word, line) for line in puzzle) + sum(
        find_horizontal(word[::-1], line) for line in puzzle
    )


def find_all_vertical(word: np.array, puzzle: np.array) -> int:
    return find_all_horizontal(word, puzzle.T)


def find_all_diagonal(word: np.array, puzzle: np.array) -> int:
    return (
        find_falling_diagonal(word, puzzle)
        + find_falling_diagonal(word, puzzle[::-1])
        + find_falling_diagonal(word[::-1], puzzle)
        + find_falling_diagonal(word[::-1], puzzle[::-1])
    )


def find_horizontal(word: np.array, line: np.array) -> int:
    word_length = len(word)
    line_length = len(line)

    if word_length > line_length:
        return 0

    count = 0
    for i in range(line_length - word_length + 1):
        if np.array_equal(word, line[i : i + word_length]):
            count += 1

    return count


def find_falling_diagonal(word: np.array, puzzle: np.array) -> int:
    word_length = len(word)
    puzzle_height, puzzle_width = puzzle.shape

    count = 0
    for i in range(puzzle_height - word_length + 1):
        for j in range(puzzle_width - word_length + 1):
            if np.array_equal(
                word, puzzle[i : i + word_length, j : j + word_length].diagonal()
            ):
                count += 1

    return count


# For part 2: Find 'A', then check around


def find_x_mas_in_puzzle(puzzle):
    # Find the 'A' in the middle, then check around
    count = 0
    for y in range(1, len(puzzle) - 1):
        for x in range(1, len(puzzle[0]) - 1):
            if puzzle[x, y] == "A":
                count += check_x_mas(puzzle, x, y)

    return count


def check_x_mas(puzzle, x, y):
    # Check if falling diagonal is MAS OR SAM, and rising diagonal is MAS OR SAM
    falling = (puzzle[x + 1, y + 1], puzzle[x - 1, y - 1])
    rising = (puzzle[x - 1, y + 1], puzzle[x + 1, y - 1])

    expected = {("M", "S"), ("S", "M")}
    return falling in expected and rising in expected


if __name__ == "__main__":
    data = get_data(day=4)
    data = np.array([list(line) for line in data.split("\n")])

    print(find_all_occurrences("XMAS", data))
    print(find_x_mas_in_puzzle(data))
