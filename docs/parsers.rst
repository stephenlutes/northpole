Parsers
=======

The parsers module contains a collection of methods that can be used for parsing input 
data for the challenges, or as factories for parsers. The following parsers are 
available.

.. function:: int_list_parser(seperator: str)

    Returns a parser that will parse the data into a list of integer lists, splitting
    each line of the input on the given seperator.

    :param seperator: The character to split each line on.
    :type seperator: str

    :return: A method that will parse the input into a list of integer lists.
    :rtype: Callable

    Example::

        data = "1x2x3\n4x5x6"
        parser = int_list_parser("x")
        parser(data)

        Result: [[1, 2, 3], [4, 5, 6]] 

.. function:: parse_string(data: str)
    
    Parses the given string by splitting by newline characters and returning the first
    string.

    :param data: The input data for the challenge.
    :type data: str

    :return: The data parsed into a single string.
    :rtype: str

    Example 1: Parsed result would be ``santa``::

        santa
        clause
    
    Example 2: Parsed result would be ``sleigh``::

        sleigh
    
.. function:: parse_string_list(data: str)

    Parses the given string by splitting on the newline characters and returning the 
    resulting list.

    :param data: The input data for the challenge.
    :type data: str

    :return: The data split into a list of strings.
    :rtype: list[str]

    Example::

        data = "Rudolph\n\Comet\nBlitzen"
        parse_string_list(data)

        Result: ["Rudolph", "Comet", "Blitzen"]