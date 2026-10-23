n=int(input("Enter a positive even integer for the size of the list?" ))

# 1. List a of length n filled with zeroes
# For accumulator patter
a = []
for i in range(n):
    a += [0]

# int*list pattern
a = [0] * n

# 2. list b of length n filled with random integers between 1 and 100
import random
b = [random.randint(1, 100) for i in range(n)]

# 3. c = alias of b
c = b

# 4. set first half of c to zeroes, print b, c
c[:n//2] = [0] * (n//2)
print(b)
print(c)

# 5. d = copy of b
d = []
for i in range(n):
    d += [b[i]]
d = b.copy()
d = b[:]

# 6. e = every 2nd element of b
e = b[::2]