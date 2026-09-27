# Name: Patrick Geraghty
# Student number: 500349204
# Course: IT1 1120
# Assignment: 1
# Year: 2026

########################
# Question 1
########################

import math
import turtle

def mh2kh(s: int | float) -> float:
    """
    Converts miles to kilometers (or miles per hour to kilometers per hour)

    :param s: The value in miles to be converted to kilometers
    :type s: int | float
    :return: The value in kilometers
    :rtype: float
    """
    return s * 1.60934

########################
# Question 2
########################

def pythagorean_pair(a: int, b: int) -> bool:
    """
    Determines if a pair of integers (a, b) is a pythagorean pair.
    A pythagorean pair is a pair of integers (a, b) such that a^2 + b^2 = c^2,
    where c is an integer.

    :param a: The first integer to be checked
    :type a: int
    :param b: The second integer to be checked
    :type b: int
    :return: True if a and b are a pythagorean pair, False otherwise
    :rtype: bool
    """
    return a**2 + b**2 == int((a**2 + b**2)**0.5)**2

########################
# Question 3
########################

def in_out(xs: int | float, ys: int | float, side: int | float) -> None:
    """
    Determines if an input point (query_x, query_y) is inside or outside of a square defined by its
    bottom-left corner (xs, ys) and its side length (side).
    Prints True if the point is inside the square, and False otherwise.

    :param xs: The x coordinate of the bottom-left corner of the square
    :type xs: int | float
    :param ys: The y coordinate of the bottom-left corner of the square
    :type ys: int | float
    :param side: The side length of the square
    :type side: int | float
    """
    query_x = float(input("Enter the x coordinate of the point: "))
    query_y = float(input("Enter the y coordinate of the point: "))

    cond_x = xs <= query_x <= xs + side
    cond_y = ys <= query_y <= ys + side

    print(cond_x and cond_y == True)

########################
# Question 4
########################

def safe(n: int) -> bool:
    """
    Determines if a given integer n is safe.
    A safe integer is defined as a non-negative integer less than 100 and that neither contains the
    digit 9 nor is divisible by 9.

    :param n: The integer to be checked
    :type n: int
    :return: True if n is safe, False otherwise
    :rtype: bool
    """
    size_cond = 0 <= n < 100
    digit_cond = '9' not in str(n)
    div_cond = n % 9 != 0

    return size_cond and digit_cond and div_cond

########################
# Question 5
########################

def quote_maker(quote: str, name: str, year: int | str) -> str:
    """
    Creates a formatted quote string.

    :param quote: The quote to be formatted
    :type quote: str
    :param name: The name of the person who said the quote
    :type name: str
    :param year: The year the quote was said
    :type year: int | str
    :return: A formatted string containing the quote, name, and year
    :rtype: str
    """
    return "In " + str(year) + ", a person called " + name + " said: \"" + quote + "\""

########################
# Question 6
########################

def quote_displayer() -> None:
    """
    Prompts the user for a quote, name, and year, and then displays the formatted quote using the
    quote_maker function.
    """
    quote = input("Give me a quote: ")
    name = input("Who said that? ")
    year = input("What year did she/he say that? ")

    print(quote_maker(quote, name, year))

########################
# Question 7
########################

def rps_winner() -> None:
    """
    Prompts the user for two players' choices in a game of rock-paper-scissors.
    Displays the result for the first player's choice.
    """
    choice1 = input("What choice did player 1 make?\nType one of the following options: rock, paper, scissors: ")
    choice2 = input("What choice did player 2 make?\nType one of the following options: rock, paper, scissors: ")

    tie = choice1 == choice2
    win = (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (choice1 == "scissors" and choice2 == "paper")

    print("Player 1 wins. That is " + str(win))
    print("It is a tie. That is not " + str(not tie))

########################
# Question 8
########################

def fun(x: int | float) -> float:
    """
    Returns the value of y for the equation 10^(4y) = x + 3

    :param x: The value of x in the equation
    :type x: int | float
    :return: The value of y for the given x
    :rtype: float
    """
    return (1 / 4) * (math.log10(x + 3))

########################
# Question 9
########################

def ascii_name_plaque(name: str) -> None:
    """
    Print an ASCII name plaque for the given name.

    :param name: The name to be displayed in the ASCII plaque
    :type name: str
    :return: None
    """
    print("*****" + "*" * len(name) + "*****")
    print("*" + " " * (len(name) + 8) + "*")
    print("*  __" + name + "__  *")
    print("*" + " " * (len(name) + 8) + "*")
    print("*****" + "*" * len(name) + "*****")

########################
# Question 10
########################

def draw_house() -> None:
    """
    Draw a house using Turtle

    :return: None
    """
    s = turtle.Screen()
    t = turtle.Turtle()

    s.bgcolor("white")
    t.pencolor("black")

    # Draw base layer
    t.pensize(10)
    t.pendown()
    t.goto(100, 0)
    t.penup()

    # Draw wall segments
    t.pensize(3)
    t.goto(10, 0)
    t.pendown()
    t.goto(10, 50)
    t.penup()

    t.goto(60, 0)
    t.pendown()
    t.goto(60, 50)
    t.penup()

    t.goto(91, 0)
    t.pendown()
    t.goto(91, 50)
    t.penup()

    # Draw right roof parallelogram
    t.goto(35, 110)
    t.pendown()
    t.goto(80, 110)
    t.goto(100, 50)
    t.goto(55, 50)
    t.goto(35, 110)

    # Draw left roof line
    t.goto(0, 50)
    t.goto(10, 50)
    t.penup()

    # Draw door
    t.goto(25, 0)
    t.pendown()
    t.goto(25, 50)
    t.goto(45, 50)
    t.goto(45, 0)
    t.penup()

    # Door handle
    t.goto(25, 25)
    t.pendown()
    t.goto(30, 25)
    t.goto(30, 20)
    t.penup()

    # Draw window
    t.begin_fill()
    t.fillcolor("yellow")
    t.goto(66, 16)
    t.pendown()
    t.goto(85, 16)
    t.goto(85, 35)
    t.goto(66, 35)
    t.goto(66, 16)
    t.end_fill()
    t.penup()
    t.goto(76, 16)
    t.pendown()
    t.goto(76, 35)
    t.penup()
    t.goto(66, 26)
    t.pendown()
    t.goto(85, 26)
    t.penup()

    # Draw skylight
    t.begin_fill()
    t.goto(67, 70)
    t.circle(11)
    t.end_fill()
    t.penup()

    # Draw chimney
    t.goto(75, 110)
    t.pendown()
    t.goto(75, 120)
    t.goto(65, 120)
    t.goto(65, 110)
    t.penup()

########################
# Question 11
########################
def alogical(n: float | int) -> int:
    """
    Returns the value of m for the equation x = n / 2^(n) such that x <= 1
    In other words, it solves for m in the equation n / (m * 2) < 1, which simplifies to m => log2(n).

    :param n: The value of n in the equation
    :type n: float | int
    :return: The value of m for the given n
    :rtype: int
    """
    return math.ceil(math.log2(n))

########################
# Question 12
########################
def cad_cashier(price: float | int, payment: float | int) -> float:
    """
    Calculates the change to be returned to a customer in Canadian dollars,
    rounded to the nearest 0.05.

    :param price: The price of the item purchased
    :type price: float | int
    :param payment: The amount paid by the customer
    :type payment: float | int
    :return: The change to be returned to the customer, rounded to two decimal places
    :rtype: float
    """
    change = payment - price
    return round(round(change / 0.05) * 0.05, 2)

########################
# Question 13
########################

def min_CAD_coins(price: int | float, payment: int | float) -> tuple[int, int, int, int, int]:
    """
    Calculates the minimum number of Canadian coins (toonies, loonies, quarters, dimes, nickels)
    needed to make change for a given price and payment.

    :param price: The price of the item purchased
    :type price: int | float
    :param payment: The amount paid by the customer
    :type payment: int | float
    :return: A tuple containing the number of toonies, loonies, quarters, dimes, and nickels needed for change
    :rtype: tuple[int, int, int, int, int]
    """
    change = cad_cashier(price, payment)
    toonies = int(change // 2)
    change -= toonies * 2
    loonies = int(change // 1)
    change -= loonies * 1
    quarters = int(change // 0.25)
    change -= quarters * 0.25
    dimes = int(change // 0.10)
    change -= dimes * 0.10
    nickels = int(change // 0.05)

    return toonies, loonies, quarters, dimes, nickels