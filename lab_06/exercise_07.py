def inner_product(list1: list[int], list2: list[int]) -> int:
    """
    Returns the inner product of two lists of integers.

    :param list1: The first list of integers
    :type list1: list[int]
    :param list2: The second list of integers
    :type list2: list[int]
    :return: The inner product of the two lists
    :rtype: int
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")

    product_sum = 0
    for i in range(len(list1)):
        product_sum += list1[i] * list2[i]

    return product_sum