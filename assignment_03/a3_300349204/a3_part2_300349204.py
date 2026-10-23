# Name: Patrick Geraghty
# Student number: 300349204
# Course: IT1 1120
# Assignment: 3 Part 2
# Year: 2026

#########################
# 2.1
#########################

def sum_odd_divisors(n: int) -> int | None:
    """
    Returns the sum of all positive odd divisors of n.
    If n is zero, returns None.

    :param n: The integer to find the sum of positive odd divisors for.
    :type n: int
    :return: The sum of all odd divisors of n, or None if n is zero.
    :rtype: int | None
    """
    # Check if n is zero
    if n == 0:
        return None

    # Running sum
    total = 0
    for i in range(1, abs(n) + 1):
        # Condition for odd divisor
        if n % i == 0 and i % 2 != 0:
            total += i
    return total


##########################
# 2.2
##########################

def series_sum() -> float | None:
    """
    Returns the sum of the series 1000 + 1/(1^2) + 1/(2^2) + 1/(3^2) + ... + 1/(n^2).

    :return: The sum of the series as an integer, or None if n is not a positive integer.
    :rtype: float | None
    """
    n = input("Enter a non-negative integer: ").strip()

    # Validate input
    if not n.isdigit() or int(n) < 0:
        return None

    # Convert n to an integer
    n = int(n)
    total = 1000

    # Calculate the sum of the series
    for i in range(0, n + 1):
        total += 1 / (i ** 2) if i != 0 else 0
    return total


###########################
# 2.3
###########################

def pell(n: int) -> int | None:
    """
    Returns the nth Pell number, or None if n is negative.

    :param n: The index of the Pell number to compute.
    :type n: int
    :return: The nth Pell number, or None if n is negative.
    :rtype: int | None
    """
    # Base cases
    if n < 0:
        return None
    elif n <= 2:
        return n

    # Recursive calculation of Pell numbers using iteration
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            c = 2 * b + a
            a = b
            b = c
        return b


############################
# 2.4
############################

def countMembers(s: str) -> int:
    """
    Returns the number of members in string s that are 'extraordinary'.
    A character is considered extraordinary if it is one of the following:
    - A lowercase letter between e and j (inclusive).
    - An uppercase letter between F and X (inclusive).
    - A digit between 2 and 6 (inclusive).
    - An exclamation mark (!).
    - A comma (,).
    - A backslash (\\).

    :param s: A string to count extraordinary members from.
    :type s: str
    :return: The count of extraordinary members in the string.
    :rtype: int
    """
    # Running sum of extraordinary members
    count = 0
    for char in s:
        # Check if the character is extraordinary
        if (('e' <= char <= 'j') or
            ('F' <= char <= 'X') or
            ('2' <= char <= '6') or
            char in ['!', ',', '\\']
        ):
            count += 1
    return count


############################
# 2.5
############################

def casual_number(s: str) -> int | None:
    """
    Returns the integer represented by a string with all commas removed.

    :param s: A string representing a number with commas.
    :type s: str
    :return: The integer value of the string with commas removed, or None if the string is not a
        valid number.
    :rtype: int | None
    """
    int_str = ""
    # Guard against negative numbers
    if s.startswith('-'):
        int_str += '-'
        # Remove the negative sign for further processing
        s = s[1:]
    for char in s:
        # Reject any character that is not a digit or a comma
        if not (char.isdigit() or char == ','):
            return None
        # Build the integer string without commas
        if char != ',':
            int_str += char

    # Guard against empty string or just a negative sign
    if int_str == "" or int_str == "-":
        return None
    return int(int_str)


############################
# 2.6
############################

def alienNumbers(s: str) -> int:
    """
    Returns the running total of the alien characters represented by the string s.
    Assumes no character in s is outside the set {T, y, !, a, N, U}.
    T = 1024, y = 598, ! = 121, a = 42, N = 6, U = 1.

    :param s: The string containing alien characters to be summed.
    :type s: str
    :return: The total numerical value of the alien characters in the string.
    :rtype: int
    """
    return sum(
        1024 if c == 'T'
        else 598 if c == 'y'
        else 121 if c == '!'
        else 42 if c == 'a'
        else 6 if c == 'N'
        else 1 for c in s
    )


############################
# 2.7
############################

def alienNumbersAgain(s:str) -> int:
    """
    Same as alienNumbers, which never used string methods in the first place.
    """
    return alienNumbers(s)


############################
# 2.8
############################

def encrypt(s: str) -> str:
    """
    Reverses the string s and then pairs characters on either side of the unencrypted segment of
    the string.

    :param s: The string to be encrypted.
    :type s: str
    :return: The encrypted string after reversing and pairing characters.
    :rtype: str
    """
    # Reverse the string
    reversed_s = s[::-1]
    encrypted = ""
    while len(reversed_s) > 1:
        # Pair the first and last characters of the reversed string
        encrypted += reversed_s[0] + reversed_s[-1]
        # Remove the paired characters from the reversed string
        reversed_s = reversed_s[1:-1]

    # Handle the case where there's one character left in the reversed string
    if len(reversed_s) == 1:
        encrypted += reversed_s[0]
    return encrypted


#############################
# 2.9
#############################

def weaveop(s: str) -> str:
    """
    Inserts some variation of "op", "Op", "oP", or "OP" between every pair of characters in the
    string s. The case of "op" is dependent on the case of the first and second characters in the
    pair, respectively.

    :param s: The string to weave "op" variations into.
    :type s: str
    :return: The string with "op" variations woven between each pair of characters.
    :rtype: str
    """
    # Base case
    if len(s) < 2:
        return s

    result = ""
    for i in range(len(s) - 1):
        first_char = s[i]
        second_char = s[i + 1]
        # Check if both characters are alphabetic
        if not (first_char.isalpha() and second_char.isalpha()):
            result += s[i]
            continue
        op_variant = "op"
        if first_char.isupper():
            op_variant = "O" + op_variant[1]
        if second_char.isupper():
            op_variant = op_variant[0] + "P"
        result += first_char + op_variant
    result += s[-1]
    return result


#############################
# 2.10
#############################

def squarefree(s: str) -> bool:
    """
    Determines whether a string s is squarefree, meaning it does not contain any consecutive
    repeated subwords.

    :param s: The string to check for squarefreeness.
    :type s: str
    :return: True if the string is squarefree, False otherwise.
    :rtype: bool
    """
    length = len(s)
    # Iterate over possible lengths of subwords
    for subword_length in range(1, length // 2 + 1):        # Maximum length is half the length of the string since we need at least two repetitions
        # Slide a window of size 2 * subword_length across the string
        for start in range(length - 2 * subword_length + 1):
            # Compare consecutive subwords of length subword_length
            if s[start:start + subword_length] == s[start + subword_length:start + 2 * subword_length]:
                return False
    return True