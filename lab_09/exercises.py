# Exercise 0.1

def letter2number(lgrade: str) -> int:
    """Converts a letter grade to a number grade."""
    if lgrade == "A+":
        return 10
    elif lgrade == "A":
        return 9
    elif lgrade == "A-":
        return 8
    elif lgrade == "B+":
        return 7
    elif lgrade == "B":
        return 6
    elif lgrade == "C+":
        return 5
    elif lgrade == "C":
        return 4
    elif lgrade == "D+":
        return 3
    elif lgrade == "D":
        return 2
    elif lgrade == "E":
        return 1
    return 0

def letter2number_better(lgrade: str) -> int:
    schema = {
        "A+": 10,
        "A": 9,
        "A-": 8,
        "B+": 7,
        "B": 6,
        "C+": 5,
        "C": 4,
        "D+": 3,
        "D": 2,
        "E": 1,
    }
    return schema.get(lgrade, 0)


# Exercise 0.2

agencies = {
    "CCC": "Civilian Conservation Corps",
    "FCC": "Federal Communications Commission",
    "FDIC": "Federal Deposit Insurance Corporation",
    "SSB": "Social Security Board",
    "WPA": "Works Progress Administration",
}
agencies["SEC"] = "Securities and Exchange Commission"
agencies["SSB"] = "Social Security Administration"
agencies.pop("CCC")
agencies.pop("WPA")


# Exercise 0.3

def lookup(phonebook: dict[tuple, str | list[str]]):
    """
    Provides a simple command-line interface to a phonebook.

    :param phonebook: A dictionary of phone numbers, with the keys being names
        (tuples, (last, first)) and values being phone numbers (strings).
        Alternate values are lists of phone numbers.
    :type phonebook: dict(tuple, str | list[str])
    """
    while True:
        fname = input("Enter the first name: ").strip()
        lname = input("Enter the last name: ").strip()

        person = (lname, fname)

        if person in phonebook:
            print(phonebook[person])
        else:
            print("The name you entered is not known.")


# Exercise 0.4

def reverse(phonebook: dict[tuple, str]):
    """
    Reverses the keys and values of a phonebook.

    :param phonebook: A dictionary of phone numbers, with the keys being names
        (tuples, (last, first)) and values being phone numbers (strings).
    :type phonebook: dict(tuple, str)
    """
    return {v: k for k, v in phonebook.items()}

def reverse_but_we_like_trash(phonebook: dict[tuple, str]):
    """
    Reverses the keys and values of a phonebook, but we like trash.

    :param phonebook: A dictionary of phone numbers, with the keys being names
        (tuples, (last, first)) and values being phone numbers (strings).
    :type phonebook: dict(tuple, str)
    """
    reverse_phonebook = {}
    for key, value in phonebook.items():
        reverse_phonebook[value] = key
    return reverse_phonebook


# Exercise 0.5

def get_year():
    """
    Prompts the user for a year and returns it as an integer.
    :return: The year entered by the user.
    :rtype: int
    """
    while True:
        year = input("Enter a year: ").strip()
        if year.isdigit() and len(year) == 4:
            return int(year)
        else:
            print("Invalid input. Please enter a valid year.")


# Exercise 1

def linear_search_v1(lst, value):
    """
    Backwards linear search implementation using a while loop.
    """
    if not lst:
        return -1
    i = len(lst) - 1
    while i != 0 and lst[i] != value:
        i -= 1
    if i == 0 and lst[i] != value:
        return -1
    else:
        return i

def linear_search_v2(lst, value):
    """
    Backwards linear search implementation using a for loop.
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return -1

def linear_search_v3(lst, value):
    """
    Backwards linear search implementation using a sentinel.
    """
    if not lst:
        return -1
    lst.insert(0, value)
    i = len(lst) - 1
    while lst[i] != value:
        i -= 1
    lst.pop(0)
    if i == 0 and lst[i] != value:
        return -1
    else:
        return i - 1


# Exercise 2

def min_or_max_index(lst: list, is_min: bool) -> tuple[int, int] | None:
    """
    Returns the index and value of the minimum or maximum element in a list.

    :param lst: A list of numbers.
    :type lst: list
    :param is_min: If True, find the minimum; if False, find the maximum.
    :type is_min: bool
    :return: A tuple containing the index and value of the minimum or maximum element, or None if
        the list is empty.
    :rtype: tuple(int, int) | None
    """
    if not lst:
        return None

    index = 0
    for i in range(1, len(lst)):
        if (is_min and lst[i] < lst[index]) or (not is_min and lst[i] > lst[index]):
            index = i
    return index, lst[index]


# Exercise 3

def first_one(L: list[int]) -> int:
    """
    Returns the index of the first occurrence of 1 in a list, or -1 if 1 is not found.

    :param L: A list of integers.
    :type L: list[int]
    :return: The index of the first occurrence of 1, or -1 if not found.
    :rtype: int
    """
    left, right = 0, len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == 1:
            if mid == 0 or L[mid - 1] != 1:
                return mid
            right = mid - 1
        else:
            left = mid + 1
    return -1

def last_zero(L: list[int]) -> int:
    """
    Returns the index of the last occurrence of 0 in a list, or -1 if 0 is not found.

    :param L: A list of integers.
    :type L: list[int]
    :return: The index of the last occurrence of 0, or -1 if not found.
    :rtype: int
    """
    initial_one = first_one(L)
    if initial_one == -1:
        return len(L) - 1
    elif initial_one == 0:
        return -1
    else:
        return initial_one - 1