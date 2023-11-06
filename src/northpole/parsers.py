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
