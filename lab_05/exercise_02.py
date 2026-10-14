import time

def is_perfect(num: int) -> bool:
    """
    Check if a number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    excluding itself. For example, 6 is a perfect number because its proper divisors are 1, 2, and 3,
    and their sum is 6 (1 + 2 + 3 = 6).

    :param num: The number to check.
    :type num: int
    :return: True if the number is perfect, False otherwise.
    :rtype: bool
    """
    if num < 1:
        return False

    # Calculate the sum of proper divisors
    proper_divisors_sum = sum(i for i in range(1, num) if num % i == 0)

    # Check if the sum of proper divisors equals the number
    return proper_divisors_sum == num

if __name__ == "__main__":

    # Print all perfect numbers between 1 and 10000
    t_start = time.time()
    print("Perfect numbers between 1 and 10000:")
    for i in range(1, 10001):
        if is_perfect(i):
            print(i)
    elapsed = time.time() - t_start
    print(f"Elapsed time: {elapsed:.6f} seconds")       # ~ 1.01 seconds

    # Print all perfect numbers between 1 and 35000000
    t_start  = time.time()
    print("Perfect numbers between 1 and 35000000:")
    for i in range(1, 35000001):
        if is_perfect(i):
            print(i)
    elapsed = time.time() - t_start
    print(f"Elapsed time: {elapsed:.6f} seconds")       # ~  seconds