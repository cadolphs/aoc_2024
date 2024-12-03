from day03 import (
    get_expressions_from_input,
    MultExpr,
    DontExpr,
)


def test_works_for_single_expression_with_no_distractions():
    input_data = "mul(3,4)"
    expected = [MultExpr(3, 4)]

    assert list(get_expressions_from_input(input_data)) == expected


def test_works_for_single_expression_surrounded_by_garbage():
    input_data = "abcmul(3,4)defmulx(5,6)ghi"
    expected = [MultExpr(3, 4)]

    assert list(get_expressions_from_input(input_data)) == expected


def test_works_for_multiple_expressions():
    input_data = "mul(3,4)mul(5,6)"
    expected = [MultExpr(3, 4), MultExpr(5, 6)]

    assert list(get_expressions_from_input(input_data)) == expected


def test_works_for_multiple_expressions_with_garbage_in_between():
    input_data = "mul(3,4)abcmul(5,6)defmul(4*)"
    expected = [MultExpr(3, 4), MultExpr(5, 6)]

    assert list(get_expressions_from_input(input_data)) == expected


def test_works_for_single_dont_expression():
    input_data = "don't()"
    expected = [DontExpr()]

    assert list(get_expressions_from_input(input_data)) == expected


## Rest is straightforward enough :p
