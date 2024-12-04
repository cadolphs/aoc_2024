import numpy as np

from day04 import find_horizontal, find_falling_diagonal, find_all_occurrences


def test_find_horizontal_1():
    assert (
        find_horizontal(np.array(["w", "o", "r", "d"]), np.array(["w", "o", "r", "d"]))
        == 1
    )


def test_find_horizontal_2():
    assert (
        find_horizontal(
            np.array(["w", "o", "r", "d"]),
            np.array(["w", "o", "r", "d", "w", "o", "r", "d"]),
        )
        == 2
    )


def test_find_falling_diagonal():
    puzzle = np.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
    word = np.array(["a", "e", "i"])

    assert find_falling_diagonal(word, puzzle) == 1


def test_find_falling_diagonal_big():
    puzzle = np.array(
        [
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "j"],
            ["k", "l", "m", "n", "o"],
            ["p", "q", "r", "s", "t"],
            ["u", "v", "w", "x", "y"],
        ]
    )
    word = np.array(["a", "g", "m", "s"])

    assert find_falling_diagonal(word, puzzle) == 1


def test_puzzle_test():
    puzzle_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    puzzle = np.array([list(line) for line in puzzle_input.split("\n")])
    word = "XMAS"

    assert find_all_occurrences(word, puzzle) == 18
