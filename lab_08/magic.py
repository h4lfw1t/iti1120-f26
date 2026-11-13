def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     (Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
    '''2D list->bool
    Returns True if m forms a magic square
    Precondition: m is a matrix with at least 2 rows and 2 columns '''

    # this tests the condition that is implied by the definition
   # i.e. that m has to be a square matrix
    if(not(is_square(m))): # if matrix is not square
         return False      # return False

    n = len(m)
    expected = n * (n * n + 1) // 2

    # Must contain every integer from 1 through n^2 exactly once
    values = {value for row in m for value in row}
    if values != set(range(1, n * n + 1)):
        return False

    # Check rows and columns
    if any(sum(row) != expected for row in m):
        return False

    if any(sum(m[i][j] for i in range(n)) != expected
           for j in range(n)):
        return False

    # Check diagonals
    diagonal1 = sum(m[i][i] for i in range(n))
    diagonal2 = sum(m[i][n - 1 - i] for i in range(n))

    return diagonal1 == expected and diagonal2 == expected

# Alternatively, if we're not allowed to use sets, `sum`, or `any`:
def magic_alternative(m):
    """Return True if m is a valid magic square."""

    if not is_square(m):
        return False

    n = len(m)
    expected = n * (n * n + 1) // 2
    values = []

    # Check that values are exactly 1 through n^2, with no duplicates
    for i in range(n):
        for j in range(n):
            value = m[i][j]

            if value < 1 or value > n * n:
                return False

            if value in values:
                return False

            values.append(value)

    # Check rows
    for i in range(n):
        row_total = 0

        for j in range(n):
            row_total += m[i][j]

        if row_total != expected:
            return False

    # Check columns
    for j in range(n):
        column_total = 0

        for i in range(n):
            column_total += m[i][j]

        if column_total != expected:
            return False

    # Check diagonals
    diagonal1 = 0
    diagonal2 = 0

    for i in range(n):
        diagonal1 += m[i][i]
        diagonal2 += m[i][n - 1 - i]

    if diagonal1 != expected or diagonal2 != expected:
        return False

    return True





# main
# TESTING OF magic functions

# this should print True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
# this should print True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not 
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
