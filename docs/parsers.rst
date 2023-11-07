Parsers
=======

The parsers module contains a collection of methods that can be used for parsing input 
data for the challenges, or as factories for parsers. The following parsers are 
available.

.. function:: parse_string(data: str)
    
    Parses the given string by splitting by newline characters and returning the first
    string.

    :param data: The data read from the input.txt file
    :type data: str

    :return: The data parsed into a single string.
    :rtype: str

    Example 1: Parsed result would be ``santa``::

        santa
        clause
    
    Example 2: Parsed result would be ``sleigh``::

        sleigh