import time

# 5.16

def indexes(search_str: str, char: str) -> list[int]:
    """
    Searches an input string for `char` and returns a list of indexes of `char` in `search_str`.

    :param search_str: The string to search through
    :type search_str: str
    :param char: The character to search for in `search_str`
    :type char: str
    :return: A list of indexes where `char` is found in `search_str`
    :rtype: list[int]
    """
    indexes_list = []
    for i in range(len(search_str)):
        if search_str[i] == char:
            indexes_list.append(i)
    return indexes_list

# 5.17

def doubles(int_list: list[int]) -> None:
    """
    Takes a list of integers and prints each integer in the list that is double the value of the
    previous integer in the list.

    :param int_list: A list of integers to check for doubles
    :type int_list: list[int]
    :return: None
    """
    for i in range(1, len(int_list)):
        if int_list[i] == 2 * int_list[i - 1]:
            print(int_list[i])

# 5.18

def four_letter(words: list[str]) -> list[str]:
    """
    Takes a list of words and returns a new list containing the sublist of all four-letter words
    from the original list.

    :param words: A list of words to filter for four-letter words
    :type words: list[str]
    :return: A list of four-letter words from the input list
    :rtype: list[str]
    """
    four_letter_words = []
    for word in words:
        if len(word) == 4:
            four_letter_words.append(word)
    return four_letter_words

# 5.19

def inBoth(list1: list, list2: list) -> bool:
    """
    Takes two lists and returns True if they have at least one element in common, otherwise returns False.

    :param list1: A list to compare with list2
    :type list1: list
    :param list2: A list to compare with list1
    :type list2: list
    :return: True if the two lists have at least one element in common, otherwise False
    :rtype: bool
    """
    for item in list1:
        if item in list2:
            return True
    return False

# 5.20

def intersect(list1: list, list2: list) -> list:
    """
    Takes two lists of distinct values and returns the intersection of the two lists as a new list.

    :param list1: A list of distinct values
    :type list1: list
    :param list2: A list of distinct values
    :type list2: list
    :return: The intersection of the two input lists as a new list
    :rtype: list
    """
    intersection = []
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection

# 5.21

def pair(list1: list[int], list2: list[int], n: int) -> None:
    """
    Takes two lists of integers and an integer n, and prints all pairs of integers (one from each
    list) that sum to n.

    :param list1: A list of integers
    :type list1: list[int]
    :param list2: A list of integers
    :type list2: list[int]
    :param n: The target sum for the pairs
    :return: None
    """
    for num1 in list1:
        for num2 in list2:
            if num1 + num2 == n:
                print(f"({num1}, {num2})")

# 5.22

def pairSum(values: list[int], n: int) -> None:
    """
    Takes a list of integers and an integer n, and prints all pairs of integers from the list that
    sum to n.

    :param values: A list of integers
    :type values: list[int]
    :param n: The target sum for the pairs
    :return: None
    """
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == n:
                print(f"({values[i]}, {values[j]})")

# 5.29

def lastfirst(names: list[str]) -> list[list[str]]:
    """
    Takes a list of names in the format "Last, First" and returns a list containing the sublists
    ["First"] and ["Last"].

    :param names: A list of names in the format "Last, First"
    :type names: list[str]
    :return: A list containing two sublists: one with first names and one with last names
    :rtype: list[list[str]]
    """
    first_names = []
    last_names = []
    for name in names:
        last, first = name.split(", ")
        first_names.append(first)
        last_names.append(last)
    return [first_names, last_names]

# 5.31

def subsetSum(values: list[int], n: int) -> bool:
    """
    Takes a list of integers and an integer n, and returns True if any three of the integers in
    the list sums to n, otherwise returns False.

    :param values: A list of integers
    :type values: list[int]
    :param n: The target sum for the subset
    :type n: int
    :return: True if any three of the integers sums to n, otherwise False
    :rtype: bool
    """
    # Wildly inefficient brute-force solution, but it works for small lists.
    length = len(values)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if values[i] + values[j] + values[k] == n:
                    return True
    return False

def subsetSumFaster(values: list[int], n: int) -> bool:
    """
    A more efficient implementation of the subsetSum function that uses a set to track seen values
    and checks for pairs that sum to n - current value.

    :param values: A list of integers
    :type values: list[int]
    :param n: The target sum for the subset
    :type n: int
    :return: True if any three of the integers sums to n, otherwise False
    :rtype: bool
    """
    length = len(values)

    for i in range(length):
        seen = set()

        for j in range(i + 1, length):
            complement = n - values[i] - values[j]
            if complement in seen:
                return True
            seen.add(values[j])
    return False

def timer_stub(func, *args) -> float:
    """
    A simple timer function that measures the execution time of a given function with provided arguments.

    :param func: The function to be timed
    :param args: The arguments to be passed to the function
    :return: The execution time of the function in seconds
    :rtype: float
    """
    start_time = time.time()
    print(func(*args))
    end_time = time.time()
    return end_time - start_time

# For shits and giggles:
# >>> timer_stub(subsetSum, [5, 4, 10, 20, 15, 19, 32, 12, 59, 54, 63, 2, 5, 98, 32, 54, 2, 8, 64, 31, 94 ,31 ,654 ,6541, 54, 32, 12, 32, 65, 48, 32, 12, 85, 65, 32, 12], 711)
# False
# 0.0002014636993408203
# >>> timer_stub(subsetSumFaster, [5, 4, 10, 20, 15, 19, 32, 12, 59, 54, 63, 2, 5, 98, 32, 54, 2, 8, 64, 31, 94 ,31 ,654 ,6541, 54, 32, 12, 32, 65, 48, 32, 12, 85, 65, 32, 12], 711)
# False
# 6.580352783203125e-05

# 5.33

def mystery(n: int) -> int:
    """
    Determines how many times n can be divided by 2 before it becomes less than or equal to 1,
    i.e., it calculates the floor of the base-2 logarithm of n.

    :param n: An integer to be divided by 2 repeatedly
    :type n: int
    :return: The number of times n can be divided by 2 before it becomes less than or equal to 1
    :rtype: int
    """
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count    # Alternatively: return int(math.log2(n)) if n > 0 else 0

# 5.46

def inversions(sequence: str) -> int:
    """
    Counts the number of inversions in a given sequence. An inversion is defined as a pair of
    indices (i, j) such that i < j and sequence[i] > sequence[j].

    :param sequence: A string representing the sequence to analyze
    :type sequence: str
    :return: The number of inversions in the sequence
    :rtype: int
    """
    count = 0
    length = len(sequence)
    for i in range(length):
        for j in range(i + 1, length):
            if sequence[i] > sequence[j]:
                count += 1
    return count

# 5.48

def sublist(list1: list, list2: list) -> bool:
    """
    Determines if `list1` is a sublist of `list2`.

    :param list1: An arbitrary list to check if it is a sublist of `list2`
    :type list1: list
    :param list2: A list to check against for sublist status
    :type list2: list
    :return: True if `list1` is a sublist of `list2`, otherwise False
    :rtype: bool
    """
    len1 = len(list1)
    len2 = len(list2)

    if len1 == 0:
        return True  # An empty list is a sublist of any list

    for i in range(len2 - len1 + 1):    # Loop through possible starting positions where list1 could fit in list2
        if list2[i:i + len1] == list1:  # Slice from i to i + len1 (length of list1) and compare with list1
            return True
    return False

# 5.37

def mssl(values: list[int]) -> int:
    """
    Find the maximum sum of a contiguous sublist in a list of integers. The maximum sum is at least
    zero (empty sublist) if all integers are negative or the list is empty.

    :param values: A list of integers to analyze for maximum contiguous sublist sum
    :type values: list[int]
    :return: The maximum sum of a contiguous sublist within the input list
    :rtype: int
    """
    max_sum = 0
    current_sum = 0

    for value in values:
        current_sum += value
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum