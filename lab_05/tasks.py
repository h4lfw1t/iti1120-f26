# Task 1

s1 = "this is a string"
s2 = "this is a string"
s3 = s1
print(s1==s3)       # True
s1 = "aha"
print(s3==s1)       # False
print(s3==s2)       # True


# Task 2

s1 = "this is a string"
print("A variable s1, refers to an object of what type?")
print(type(s1))         # <class 'str'>

s4 = ["this is a string"]
print("A variable s4, refers to an object of what type?")
print(type(s4))         # <class 'list'>

print("A variable s4[0], refers to an object of what type?")
print(type(s4[0]))      # <class 'str'>


# Task 3
s5 = [2, 4, "oaxaca", True]
s6 = [2, 4, "oaxaca", True]
print(s5==s6)           # True
print(s5 is s6)         # False
s7 = s6
print(s7 is s6)         # True
s7[3] = False
print(s5)               # [2, 4, "oaxaca", True]
print(s6)               # [2, 4, "oaxaca", False]
print(s7)               # [2, 4, "oaxaca", False]


# Task 5

for i in range(-2, 14):
    print("*")
    print("**")
# prints 16 * 3 = 48 "*"


# Task 6

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:
    print(afruit, end = " ")        # prints "apple orange banana cherry "

fruits = ["apple", "orange", "banana", "cherry"]
for position in range(len(fruits)):
    print(fruits[position], end = " ")        # prints "apple orange banana cherry "

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi ", name, " Please come to my party on Saturday!")

    # "Hi  Joe  Please come to my party on Saturday!"
    # "Hi  Amy  Please come to my party on Saturday!"
    # "Hi  Brad  Please come to my party on Saturday!"
    # "Hi  Angelina  Please come to my party on Saturday!"
    # "Hi  Zuki  Please come to my party on Saturday!"
    # "Hi  Thandi  Please come to my party on Saturday!"
    # "Hi  Paris  Please come to my party on Saturday!"


# Task 7

for i in range(5, 0, -1):
    num = 1
    for j in range(1, i + 1):
        print(num, end = "l ")
        num=num * 2
    print()

    # 1l 2l 4l 8l 16l
    # 1l 2l 4l 8l
    # 1l 2l 4l
    # 1l 2l
    # 1l