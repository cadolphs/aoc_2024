import re
from dataclasses import dataclass
from typing import Iterable, TypeAlias

from aocd import get_data
from typing_extensions import assert_never


@dataclass
class MultExpr:
    a: int
    b: int

    def value(self) -> int:
        return self.a * self.b


@dataclass
class DontExpr:
    pass


@dataclass
class DoExpr:
    pass


Expression: TypeAlias = MultExpr | DontExpr | DoExpr


def get_expressions_from_input(input_data: str) -> Iterable[Expression]:
    pattern = r"(?P<mult>mul\((\d+),(\d+)\))|(?P<dont>don't\(\))|(?P<do>do\(\))"
    matches = re.finditer(pattern, input_data)
    for match in matches:
        if match.group("mult"):
            yield MultExpr(int(match.group(2)), int(match.group(3)))
        elif match.group("dont"):
            yield DontExpr()
        elif match.group("do"):
            yield DoExpr()


if __name__ == "__main__":
    data = get_data(day=3)

    # Part 1
    expressions = get_expressions_from_input(data)

    result = sum(expr.value() for expr in expressions if isinstance(expr, MultExpr))
    print(result)

    # Part 2
    expressions = get_expressions_from_input(data)

    acc = 0
    flag = 1
    for expr in expressions:
        if isinstance(expr, MultExpr):
            acc += expr.value() * flag
        elif isinstance(expr, DontExpr):
            flag = 0
        elif isinstance(expr, DoExpr):
            flag = 1
        else:
            assert_never(expr)
    print(acc)
