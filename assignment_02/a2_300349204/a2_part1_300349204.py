import math
import random


def elementary_school_quiz(flag: int, n: int) -> int:
    """
    This function generates n random exponential/logarithmic questions for elementary school
    students and checks their answers.

    :param flag: Integer flag to determine the type of questions (0 for logarithmic, 1 for exponential)
    :type flag: int
    :param n: The number of problems to generate (1 or 2)
    :type n: int
    :return: The number of correct answers
    :rtype: int
    """
    correct_answers = 0
    base = 2

    for i in range(n):
        print("Question " + str(i+1) + ":")
        exponent = random.randint(0, 10)
        log_arg = base ** exponent
        if flag == 0:
            prompt = (
                "2 to what is "
                + str(log_arg)
                + ", i.e., what is the result of log_2 ("
                + str(log_arg)
                + ")? "
            )
            expected_answer = exponent
        elif flag == 1:
            prompt = (
                "What is the result of 2^" + str(exponent) + "? "
            )
            expected_answer = log_arg
        else:
            continue

        if float(input(prompt)) == expected_answer:
            correct_answers += 1

    return correct_answers



def high_school_quiz(a: int | float, b: int | float, c: int | float) -> None:
    """
    Solves the quadratic equation of the form ax^2 + bx + c = 0 and prints the solutions.

    :param a: The coefficient of x^2
    :type a: int | float
    :param b: The coefficient of x
    :type b: int | float
    :param c: The constant term
    :type c: int | float
    :return: None
    """

    equation = str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0"

    if a == 0:
        if  b == 0:
            if c == 0:
                print(
                    "The quadratic equation " + equation + "\n"
                    "is satisfied for all numbers x"
                )
            else:
                print(
                    "The quadratic equation " + equation + "\n"
                    "is satisfied for no number x"
                )
        else:
            root = str(-c / b)
            print(
                "The linear equation " + equation[7:] + "\n"
                "has the following root/solution: " + root
            )
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = str((-b + math.sqrt(discriminant)) / (2 * a))
        root2 = str((-b - math.sqrt(discriminant)) / (2 * a))
        print(
            "The quadratic equation " + equation + "\n"
            "has the following real roots:\n"
            + root1 + " and " + root2
        )
    elif discriminant == 0:
        root1 = str(-b / (2 * a))
        print(
            "The quadratic equation " + equation + "\n"
            "has only one solution, a real root:\n"
            + root1
        )
    else:
        real_part = str(-b / (2 * a))
        imaginary_part = str(math.sqrt(-discriminant) / (2 * a))
        root1 = real_part + " + i" + imaginary_part
        root2 = real_part + " - i" + imaginary_part
        print(
            "The quadratic equation " + equation + "\n"
            "has the following two complex roots:\n"
            + root1 + "\n and \n" + root2
        )



# main
if __name__ == "__main__":
    print(
        "*******************************************\n"
        "*                                         *\n"
        "*  __Welcome to my math quiz-generator__  *\n"
        "*                                         *\n"
        "*******************************************\n"
    )

    name=input("What is your name? ")

    status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

    if status=='1':
        block_text = (
            "  __" + name + ", welcome to my quiz-generator for elementary school students.__  "
        )
        print(
            "*" + len(block_text) * "*" + "*\n"
            "*" + len(block_text) * " " + "*\n"
            "*" + block_text + "*\n"
            "*" + len(block_text) * " " + "*\n"
            "*" + len(block_text) * "*" + "*\n"
        )

        flag = int(
            input(
                name + ", what would you like to practice? Enter\n"
                "0 for inverse of exponentiation\n"
                "1 for exponentiation\n"
            )
        )

        if flag not in [0, 1]:
            print("Invalid choice. Only 0 or 1 is accepted.")
        else:
            n = int(
                input(
                    "How many practice questions would you like to do? Enter 0, 1, or 2: "
                )
            )
            if n == 0:
                print("Zero questions. OK. Good bye")
            elif n > 2:
                print("Only 0,1, or 2 are valid choices for the number of questions.")
            else:
                print(name + ", here is your " + str(n) + " questions:")
                score = elementary_school_quiz(flag, n)

                if score == n:
                    print("Congratulations " + name + "! You'll probably get an A tomorrow.")
                elif score == 0:
                    print("I think you need some more practice, " + name + ".")
                else:
                    print("You did ok, " + name + ", but I know you can do better.")


    elif status=='2':
        block_text = (
            "  __quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "__  "
        )
        print(
            "*" + len(block_text) * "*" + "*\n"
            "*" + len(block_text) * " " + "*\n"
            "*" + block_text + "*\n"
            "*" + len(block_text) * " " + "*\n"
            "*" + len(block_text) * "*" + "*\n"
        )
        flag=True
        while flag:
            question=input(name+", would you like a quadratic equation solved? ").lower().strip()

            if question!="yes":
                flag=False
            else:
                print("Good choice!")
                a = float(input("Enter a number the coefficient a: "))
                b = float(input("Enter a number the coefficient b: "))
                c = float(input("Enter a number the coefficient c: "))
                high_school_quiz(a, b, c)

    else:
        print(name + ", you are not a target audience for this software.")

    print("Good bye "+name+"!")
