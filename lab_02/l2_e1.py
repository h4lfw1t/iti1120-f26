"""
Course: ITI 1120
Assignment: Lab 1 Exercises
Geraghty, Patrick
300349204
"""
from typing import Any


# Exercise 1
def repeater(s1: str, s2: str, n: int) -> str:
    """
    Build a string of the form "_s1_s2_s1_s2_..." with n repetitions of s1 and s2.

    :param s1: The first string to be repeated.
    :param s2: The second string to be repeated.
    :param n: The number of times s1 and s2 should be repeated.
    :return: The resulting string after repeating s1 and s2 n times.
    """
    initial = "_" + s1 + "_" + s2
    final = "_"
    return initial * n + final

# Exercise 2
def roots(a: float, b: float, c: float) -> tuple[Any, Any] | None:
    """
    Calculate the roots of a quadratic equation of the form ax^2 + bx + c = 0.

    :param a: Coefficient of x^2.
    :param b: Coefficient of x.
    :param c: Constant term.
    :return: A tuple containing the two roots of the equation.
    """
    discriminant = b**2 - 4*a*c
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print(
        "The quadratic equation with coefficients a = " + str(a) + ", b = " + str(b) + ", and c = "
        + str(c) + " has the following solutions (i.e., roots): " + str(root1) + " and "
        + str(root2)
    )

# Exercise 3
def real_roots(a: float, b: float, c: float) -> bool:
    """
    Determine whether a quadratic equation has real roots.

    :param a: Coefficient of x^2.
    :param b: Coefficient of x.
    :param c: Constant term.
    :return: True if the equation has real roots, False otherwise.
    """
    discriminant = b**2 - 4*a*c
    return discriminant >= 0

# Exercise 4
def reverse(x: int) -> int:
    """
    Reverse the digits of a two-digit positive integer.

    :param x: The integer to be reversed.
    :return: The integer with its digits reversed.
    """
    first = x // 10
    second = x % 10
    return second * 10 + first

# Test suite
if __name__ == "__main__":
    # Test repeater function
    print(repeater("AAA", "x", 3))
    print(repeater("+", "--", 30))
    print(repeater("T", "I_I", 100))

    # Test roots function
    roots(-1, 4, 1.5)
    roots(1, 2, 1)

    # Test real_roots function
    print(real_roots(-1, 4, 1.5))
    print(real_roots(1, 2, 1))
    print(real_roots(1, 1, 1))

    # Test reverse function
    print(reverse(72))
    print(reverse(44))
    print(reverse(19))