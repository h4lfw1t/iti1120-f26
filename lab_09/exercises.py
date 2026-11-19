# Exercise 1

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


# Exercise 2

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


# Exercise 3

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


# Exercise 4

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
