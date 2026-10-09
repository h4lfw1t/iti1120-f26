# Task 1

s1 = "good"
s2 = "bad"
s3 = "silly"

# a)
'll' in s3

# b)
' ' not in s1

# c)
s1 + s2 + s3

# d)
' ' in s1 + s2 + s3

# e)
s3 * 10

# f)
len(s1 + s2 + s3)


# Task 2

aha = "abcdefgh"

# a)
aha[0:4]

# b)
aha[3:6]

# c)
aha[-1]

# d)
aha[-3:-1]

# e)
aha[4:]

# f)
aha[-3:]

# g)
aha[::3]

# h)
aha[1:5:3]


# Task 3

s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...'''

# a)
newS = s.replace(",", " ").replace(";", " ").replace(".", " ").replace("\n", " ")

# alt
newS_alt = ''.join(char if char.isalnum() else ' ' for char in s)

# b)
newS = newS.strip()

# c)
newS = newS.lower()

# d)
newS.count("it was")

# e)
newS = newS.replace("was", "is")


# Task 6

# a)
for i in range(11):
    if i != 10:
        print(i, end=", ")
    else:
        print(i)

# b)
for i in range(1, 10):
    if i != 9:
        print(i, end=", ")
    else:
        print(i)

# c)
for i in range(0, 9, 2):
    if i != 8:
        print(i, end=", ")
    else:
        print(i)

# d)
for i in range(1, 10, 2):
    if i != 9:
        print(i, end=", ")
    else:
        print(i)

# e)
for i in range(2, 7):
    if i != 6:
        print(i*10, end=", ")
    else:
        print(i*10)

# f)
for i in range(10, 0, -1):
    if i != 1:
        print(i, end=", ")
    else:
        print(i)
