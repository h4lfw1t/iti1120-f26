# Name: Patrick Geraghty
# Student number: 300349204
# Course: IT1 1120
# Assignment: 3 Part 1
# Year: 2026

def is_up_monotone(X: str, d: str) -> bool:
    """
    Returns True if the sequence of independent d-digit numbers in X is a monotonically increasing
    sequence, and False otherwise.
    X must be positive, and divisible by d. The function assumes that the input is valid.

    :param X: A sequence of digits representing a number.
    :type X: str
    :param d: The size of the d-digit numbers in X.
    :type d: str
    :return: True if the sequence of d-digit numbers in X is a monotonically increasing sequence,
    and False otherwise.
    :rtype: bool
    """
    # Convert d to an int
    d = int(d)

    flag = True
    # Split the sequence of digits in X into d-digit numbers
    for i in range(0, len(X), d):
        # Check if the current d-digit number is less than or equal to the next d-digit number
        if i+d != len(X) and int(X[i:i+d]) >= int(X[i+d:i+2*d]):
            flag = False
        # if the current d-digit number is the last one, print it without a comma
        if i+d == len(X):
            print(X[i: i+d])
        else:
            print(X[i: i+d], end=", ")
    return flag

def header(name: str | None = None):
    """
    Prints the header for the program.

    :param name: The name of the user, if provided.
    :type name: str | None
    """
    header_str = "__Welcome to up-monotone inquiry__"
    if name:
        header_str = "__" + name + ", welcome to up-monotone inquiry.__"

    print("*" * (len(header_str) + 6))
    print("*" + " " * (len(header_str) + 4) + "*")
    print("*  " + header_str + "  *")
    print("*" + " " * (len(header_str) + 4) + "*")
    print("*" * (len(header_str) + 6))

def footer(name:str):
    """
    Prints the footer for the program.

    :param name: The name of the user.
    :type name: str
    """
    footer_str = "__Good bye " + name + "!__"
    print("*" * (len(footer_str) + 6))
    print("*" + " " * (len(footer_str) + 4) + "*")
    print("*  " + footer_str + "  *")
    print("*" + " " * (len(footer_str) + 4) + "*")
    print("*" * (len(footer_str) + 6))

# main
# Your code for the welcome message goes here, instead of name="Vida"
header()

name=input("What is your name? ").strip()

header(name)

flag=True
while flag:
    question=input(
        name+", would you like to test if a number admits an up-monotone split of given size? "
    )
    question=(question.strip()).lower()
    if question != 'yes' and question != 'no':
        print("Please enter yes or no. Try again")
    elif question=='no':
        flag=False
    else:
        print("Good choice!")
        monotonic_input = input("Enter a positive integer: ").strip()
        if not monotonic_input.isdigit():
            if len(monotonic_input) == 0:
                print("The input cannot be empty. Try again.")
            elif "." in monotonic_input or "," in monotonic_input:
                print("The input can only contain digits. Try again.")
            elif monotonic_input[0] == '-':
                print("The input has to be a positive integer.Try again.")
            else:
                print("The input can only contain digits. Try again.")
        elif monotonic_input == "0":
            print("The input has to be a positive integer. Try again.")
        else:
            split = input(
                "Input the split. The split has to divide the length of "
                + monotonic_input + " i.e. " + str(len(monotonic_input)) + "\n"
            ).strip()
            if not split.isdigit():
                print("The split can only contain digits. Try again. ")
            elif split == "0" or len(monotonic_input) % int(split) != 0:
                print(
                    split + " does not divide " + str(len(monotonic_input)) + ". Try again. "
            )
            else:
                result = is_up_monotone(monotonic_input, split)
                if result:
                    print("The sequence is up-monotone")
                else:
                    print("The sequence is not up-monotone")

print()
footer(name)