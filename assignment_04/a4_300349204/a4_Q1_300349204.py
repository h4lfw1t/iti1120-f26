# Course: ITI 1120
# Assignment: 4
# Geraghty, Patrick
# 300349204

def number_divisible(numbers: list[int], divisor: int) -> int:
    """
    Takes a list of numbers and a divisor and returns the number of elements in the list that are
    divisible by the divisor.

    :param numbers: List of numbers to check for divisibility
    :type numbers: list[int]
    :param divisor: Integer to divide the numbers by
    :type divisor: int
    :return: The count of numbers in the list that are divisible by the divisor
    :rtype: int
    """
    count = 0
    for number in numbers:
        if number % divisor == 0:
            count += 1
    return count

# Main
raw_input = input("Please input a list of integers separated by spaces: ").strip().split()
divisor = int(input("Please input an integer: ").strip())       # Assume divisor is not zero (based on provided test cases)

# Assuming we can't use list comprehension
for i in range(len(raw_input)):
    raw_input[i] = int(raw_input[i])

num_elements = number_divisible(raw_input, divisor)
print("The number of elements divisible by", divisor, "is", num_elements)