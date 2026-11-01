# Course: ITI 1120
# Assignment: 4
# Geraghty, Patrick
# 300349204

def two_length_run(values: list[int | float]) -> bool:
    """
    Determine whether the input list of values contains a run of at least two consecutive values
    that are equal.

    :param values: The input list of values to check.
    :type values: list[int | float]
    :return: True if the list contains a run of at least two consecutive equal values, False otherwise.
    :rtype: bool
    """
    for i in range(len(values) - 1):
        if values[i] == values[i + 1]:
            return True
    return False

# Main
raw_input = input("Please input a list of integers separated by spaces: ").strip().split()

# Assuming we can't use list comprehension
for i in range(len(raw_input)):
    raw_input[i] = float(raw_input[i])

print(two_length_run(raw_input))