# Name: Patrick Geraghty
# Student number: 500349204
# Course: IT1 1120
# Assignment: 2 Part 2
# Year: 2026

########################
# 2.1
########################

def min_enclosing_rectangle(radius: int | float, x: int | float, y: int | float) -> tuple | None:
    """
    Calculate the smallest (axis-aligned) rectangle that encloses a circle with a given radius and
    center coordinates (x, y).

    :param radius: The radius of the circle.
    :type radius: int | float
    :param x: The x-coordinate of the center of the circle.
    :type x: int | float
    :param y: The y-coordinate of the center of the circle.
    :type y: int | float
    :return: The x- and y-coordinates of the bottom-left corner of the rectangle as a tuple,
        None if the radius is negative.
    :rtype: tuple | None
    """
    # Check radius is non-negative
    if radius < 0:
        return None

    # Calculate the bottom-left corner of the rectangle
    x_rect = x - radius
    y_rect = y-radius

    return x_rect, y_rect

########################
# 2.2
########################

def vote_percentage(results: str) -> float:
    """
    Calculate the percentage of votes for a candidate based on the election results.

    :param results: A string representing the election results, consisting of 'yes', 'no', and
        'abstain' votes.
    :type results: str
    :return: The percentage of 'yes' votes as a float.
    :rtype: float
    """
    # Count the number of 'yes' and 'no' votes
    yes_count = results.count('yes')
    no_count = results.count('no')

    # Calculate the total number of votes, disregarding those who abstained
    total_votes = yes_count + no_count

    # Avoid division by zero
    if total_votes == 0:
        return 0.0

    return yes_count / total_votes

########################
# 2.3
########################

def vote() -> None:
    """
    Prompt the user to enter the election results and determine the outcome of the proposal based
    on the percentage of 'yes' votes.
    """
    results = input("Enter the yes, no, abstained votes one by one and then press enter:\n   ")
    percentage = vote_percentage(results)

    if percentage == 1.0:
        print("proposal passes unanimously")
    elif percentage >= 2/3:
        print("proposal passes with super majority")
    elif percentage >= 0.5:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")

########################
# 2.3
########################

def l2lo(w: int | float) -> tuple:
    """
    Takes a non-negative number w and returns a tuple (l, o) such that w = l + o/16, where l is a
    non-negative integer and o is a non-negative number smaller than 16.

    :param w: A non-negative number.
    :type w: int | float
    :return: A tuple (l, o) such that w = l + o/16, where l is a non-negative integer and o is a non-negative
        number smaller than 16.
    :rtype: tuple
    """
    l = int(w)
    o = (w - l) * 16
    return l, o