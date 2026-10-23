def sum_5_consecutive(l: list) -> bool:
    """
    Returns True if there are five consecutive numbers in the list l that sum to zero.

    :param l: List of numbers to check for five consecutive numbers that sum to zero
    :type l: list[int]
    :return: True if there are five consecutive numbers in the list that sum to zero, False otherwise
    :rtype: bool
    """
    # # for method
    # for index in range(len(l) - 4):
    #     if sum(l[index:index + 5]) == 0:
    #         return True

    # while method
    index = 0
    while index <= len(l) - 5:
        if sum(l[index:index + 5]) == 0:
            return True
        index += 1
    return False