# Course: ITI 1120
# Assignment: 4
# Geraghty, Patrick
# 300349204

def longest_run(values: list[int | float]) -> int:
    """
    Determines the length of the longest run of consecutive equal values in the input list.

    :param values: The input list of values to check.
    :type values: list[int | float]
    :return: The length of the longest run of consecutive equal values in the list.
    :rtype: int
    """
    if not values:
        return 0

    longest = 1
    current = 1

    for i in range(1, len(values)):
        if values[i] == values[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest

# Main
raw_input = input("Please input a list of integers separated by spaces: ").strip().split()

# Assuming we can't use list comprehension
for i in range(len(raw_input)):
    raw_input[i] = float(raw_input[i])

print(longest_run(raw_input))
