from typing import Callable


def int_list_parser(seperator: str) -> Callable:
    """
    Create a parser instance that will parse strings into a list of integers based on a
    seperating character.

    Example:
        Providing ',' as the seperating character, the string '1,4,7' would be parsed as
        [1, 4, 7].

    Args:
        seperator (str): The character to split each string on.

    Returns:
        Callable: The parser function.
    """

    def parse(data: str) -> list[list[int]]:
        """
        Take the input data and parse each line into a list of integers.

        Args:
            data (str): The input data for the challenge.

        Returns:
            list[list[int]]: The list of parsed lists of integers.
        """
        return [[int(x) for x in line.split(seperator)] for line in data.splitlines()]

    return parse


def parse_string(data: str) -> str:
    """
    Take the input data and parse it into a single string. The result is everything
    before the first newline character.

    Args:
        data (str): The input data to parse

    Returns:
        str: The parsed string
    """
    return data.splitlines()[0]


def parse_string_list(data: str) -> list[str]:
    """
    Parse the input data by splitting it by line.

    Args:
        data (str): The input data to parse.

    Returns:
        list[str]: The input data split by the newline character.
    """
    return data.splitlines()
