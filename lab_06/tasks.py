# Task 3
def task_3():
    """
    Prints 'apple is' and the largest integer entered by the user. Does not print until the user enters 0.
    :return:
    """
    number=int(input("Enter an integer: "))
    apple=number

    while (number!=0):
        number=int(input("Enter an integer: "))
        if number>apple:
            apple=number
    print("apple is",apple)

    # For inputs of 1, 5, -3, 0, the output will be: apple is 5

# Task 4

def task_4():
    x = 10
    y = 100 % 90
    i = 0
    while i < 10000:
        if (x!=y):
            print("aha")
        i=i+1

    # Does literally not print anything

# Task 5

def task_5():
    def is_apple(x):
        if x % 4 == 0:
            appleFlag = True;
        else:
            appleFlag = False

        appleFlag = appleFlag and is_pear(-200)
        return appleFlag

    def is_pear(x):
        if (x < -101):
            pearFlag = True
        else:
            pearFlag = False
        return pearFlag

    flag1 = is_apple(44)
    flag2 = is_pear(-101)
    print(str(flag1)+" "+str(flag2))
    if (flag1 and flag2):
        print("ding!")
    if (flag1 or flag2):
        print("dong!")

    # Prints 'dong!'

# Task 6

def is_prime(n):
    for divisor in range (2, n//2 + 1):
        if n % divisor == 0:
            return False
        else:
            return True
    return True

    # Wrong for first odd non-prime (9) since it will return True after checking 2 (9 % 2 != 0)
    # To fix, remove else statement