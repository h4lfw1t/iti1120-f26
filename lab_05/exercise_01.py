def ah(l: list, x: int, y: int) -> tuple[int, int | None]:
    """
    Given a list l and two integers x and y, such that x <= y, return a tuple containing the number
    of elements in l that are between x and y (inclusive), and the minimum element of l that is
    between x and y (inclusive). If there are no elements in l that are between x and y
    (inclusive), return (0, None).

    :param l: List of numbers
    :type l: list[int | float]
    :param x: Boundary integer (upper or lower)
    :type x: int
    :param y: Boundary integer (upper or lower)
    :type y: int
    :return: Tuple containing the number of elements in l that are between x and y (inclusive),
        and the minimum element of l that is between x and y (inclusive).
    :rtype: tuple[int, int | None]
    """
    # Initialize filtered list
    filtered_list = []

    # Determine upper and lower bounds
    if x > y:
        x, y = y, x

    # Filter list
    filtered_list = [i for i in l if x <= i <= y]

    # Find the minimum element in the filtered list
    if filtered_list:
        min_element = min(filtered_list) or None
    else:
        min_element = None
    return len(filtered_list), min_element

if __name__ == "__main__":
    #  Test cases
    print(ah([1, 2, 3, 4, 5], 2, 4))  # (3, 2)
    print(ah([1, 2, 3, 4, 5], 6, 10)) # (0, None)
    print(ah([1, 2, 3, 4, 5], -1, 0)) # (0, None)
    print(ah([1, 2, 3, 4, 5], -1, 3)) # (3, 1)
    print(ah([1, 2, 3, 4, 5], -1, -10)) # (0, None)

    print(ah([5, 1, -2.5, 10, 13, 8], 2, 11)) # (3, 5)