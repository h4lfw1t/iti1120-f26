def input_sum():
    """
    Prompts the user to input two numbers and prints their sum.
    """
    flag = True

    while flag:
        try:
            num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
            print(f"The sum of {num1} and {num2} is: {num1 + num2}")

            repeat = input("Do you want to continue? (yes/no): ").lower()
            if repeat != "yes":
                flag = False
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
