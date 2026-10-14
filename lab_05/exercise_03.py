def arithmetic(input: list) -> bool:
    """
    Returns True of the input list is an arithmetic sequence, False otherwise.

    :param input: A list of numbers
    :type input: list
    :return: True if the input list is an arithmetic sequence, False otherwise
    :rtype: bool
    """
    if len(input) < 2:
        return True

    difference = input[1] - input[0]

    for i in range(1, len(input)):
        if input[i] - input[i - 1] != difference:
            return False

    return True

def is_sorted(input: list) -> bool:
    """
    Returns True if the input list is sorted in ascending order, False otherwise.

    :param input: A list of numbers
    :type input: list
    :return: True if the input list is sorted in ascending order, False otherwise
    :rtype: bool
    """
    for i in range(1, len(input)):
        if input[i] < input[i - 1]:
            return False

    return True