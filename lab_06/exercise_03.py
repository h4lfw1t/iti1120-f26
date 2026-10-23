def first_neg(l: list) -> int | None:
    """
    Returns the index of the first negative number in the list l. If there are no negative numbers, returns N one.

    :param l: List of numbers to search for the first negative number
    :type l: list
    :return: The index of the first negative number in the list, or None if there are no negative numbers
    :rtype: int | None
    """
    index = 0
    while True:
        if index == len(l):
            return None
        if l[index] < 0:
            return index
        index += 1