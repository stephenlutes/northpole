import pytest

from northpole.parsers import parse_string


@pytest.mark.parametrize(
    "data,expected",
    [("santa", "santa"), ("elves\n", "elves"), ("sleigh\nbells", "sleigh")],
)
def test_parse_string(data: str, expected: str) -> None:
    assert parse_string(data) == expected
