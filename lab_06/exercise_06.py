def fib(n: int) -> list[int]:
    """
    Returns a list of the first n Fibonacci numbers.

    :param n: The number of Fibonacci numbers to generate
    :type n: int
    :return: A list of the first n Fibonacci numbers
    :rtype: list[int]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)

    return fib_list