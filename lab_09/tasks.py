# Task 1

# O(log n)
def foo1(n):
    i = 1
    while i < n:
        i = i * 2
        count = count + 1

# O(log n)
def foo2(n):
    i = n
    while i >= 1:
        i = i // 2

# O(n)
def foo3(n):
    for i in range(n):
        print(i)

# O(n)
def foo4(n):
    for i in range(-n, n, 3):
        print("*")

# O(n^2)
def foo5(n):
    for i in range(n):
        for j in range(i + 1, n):
            print("*")

# O(n^3)
def foo6(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print("*")

# O(n log n)
def foo7(n):
    for i in range(n):
        j = n
        while j >= 1:
            j = j // 2


# Task 2

def annona(L):
    count = 0
    for i in range(len(L)):
        flag = True
        for j in range(len(L)):
            if L[i] == L[j] and i != j:
                flag = False
        if flag:
            count = count + 1
    return count

lst = [1, 0, 2, 0, 3]
result = annona(lst)
print(result)

# 1. 3
# 2. Counts the number of unique elements in the list.
# 3. O(n^2), for n=1000, the function will perform 1,000,000 comparisons in the worst case.


# Task 4
# Returns last duplicate value index

# Task 5
# Linear O(n)

# Task 7
# [6, 5, 4, 3, 7, 1, 2]
# [1, 5, 4, 3, 7, 6, 2]
# [1, 2, 4, 3, 7, 6, 5]
# [1, 2, 3, 4, 7, 6, 5]
# [1, 2, 3, 4, 5, 6, 7]


# Task 8

# O(n^2) in the best case, O(n^3) in the worst case.
# The function has a nested loop structure, where the outer loop iterates over the list and the
# inner loop iterates over the remaining elements to find the minimum value.
# In the best case, when the list is already sorted, the inner loop will only run once for each
# iteration of the outer loop, resulting in O(n^2) time complexity.
# In the worst case, when the list is sorted in reverse order, the inner loop will run for all
# remaining elements for each iteration of the outer loop, resulting in O(n^3) time complexity.
def some_sort(L):
    sorted_list = []
    while L != []:
        if L[0] == min(L):
            sorted_list.append(L[0])
            L.pop(0)
        else:
            L.append(L[0])
            L.pop(0)
    return sorted_list