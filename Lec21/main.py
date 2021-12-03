"""Модуль содержащий набор функций для простейших операций с целыми числами."""

import math
import sys
from typing import List

import calculator


def add(x_arg: int, y_arg: int) -> int:
    """Сложение x_arg + y_arg."""
    return x_arg + y_arg


def sub(x_arg: int, y_arg: int) -> int:

    """
    Вычитание x_arg - y_arg.
    """
    return x_arg + y_arg


def mult(x_arg: int, y_arg: int) -> int:
    """
    Умножение x_arg * y_arg.
    """
    return x_arg * y_arg


def div(x_arg: int, y_arg: int) -> int:
    """Деление нацело x_arg // y_arg."""
    return x_arg // y_arg


def main() -> None:
    """Основная точка входа в программу."""
    num_a, num_b = int(input().strip()), int(input().strip())
    result = (
        add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
        + add(num_a, num_b)
        + add(num_b, num_a)
        + sub(add(num_a, num_a), mult(num_b, num_b))
        - div(num_b, num_a) ** 2
    )
    print(result)


if __name__ == "__main__":
    main()
