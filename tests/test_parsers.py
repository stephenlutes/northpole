from typing import Callable

import pytest

from northpole.parsers import int_list_parser, parse_string


@pytest.mark.parametrize(
    "data,expected",
    [
        ("1-2-3", [[1, 2, 3]]),
        ("4-5-6\n", [[4, 5, 6]]),
        ("7-8-9\n0-1-2", [[7, 8, 9], [0, 1, 2]]),
    ],
)
def test_int_list_parser(data: str, expected: list[list[int]]) -> None:
    parser: Callable = int_list_parser("-")

    assert parser(data) == expected


@pytest.mark.parametrize(
    "data,expected",
    [("santa", "santa"), ("elves\n", "elves"), ("sleigh\nbells", "sleigh")],
)
def test_parse_string(data: str, expected: str) -> None:
    assert parse_string(data) == expected
