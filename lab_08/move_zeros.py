def move_zeros_v1(numbers: list) -> list:
    """
    Return a new list with all zeros moved to the end of numbers. The input
    list is unchanged.

    :param numbers: a list of integers
    :type numbers: list
    :return: a new list with all zeros moved to the end
    :rtype: list
    """
    result = []

    for number in numbers:
        if number != 0:
            result.append(number)

    for number in numbers:
        if number == 0:
            result.append(number)

    return result


def move_zeros_v2(numbers: list) -> None:
    """
    Move all zeros to the end of numbers, preserving the order of the other
    values.

    :param numbers: a list of integers
    :type numbers: list
    """
    result = move_zeros_v1(numbers)
    numbers[:] = result


def move_zeros_v3(numbers: list) -> None:
    """
    Move all zeros to the end of numbers in place without creating another
    list. The order of nonzero values is not guaranteed.

    :param numbers: a list of integers
    :type numbers: list
    """
    next_nonzero = 0

    for index in range(len(numbers)):
        if numbers[index] != 0:
            numbers[next_nonzero], numbers[index] = (
                numbers[index],
                numbers[next_nonzero],
            )
            next_nonzero += 1
