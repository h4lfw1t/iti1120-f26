def sum_odd_while_v2(n: int) -> int:
    """
    Returns the sum of all odd integers between 5 and n

    :param n: The upper limit of the range to sum odd integers
    :type n: int
    :return: The sum of all odd integers between 5 and n
    :rtype: int
     """

    total = 0
    current = 5

    while current <= n:
        if current % 2 != 0:
            total += current
        current += 1

    return total