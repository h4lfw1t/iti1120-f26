def is_divisible(n,m):
     '''(int, int)->bool
     returns True if n is divisible by n, and False otherwise.'''
     return n%m==0

def is_divisible23n8(n):
     '''(int)->bool
     returns string "yes" if n is divisible by 2 or 3 but not 8, and "no" otherwise.'''
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not(is_divisible(n,8))):
          return True
     else:
          return False

def print_all_23n8(num: int) -> None:
     for i in range(1, num+1):
          if is_divisible23n8(i):
               print(i)

user_num = int(input("Enter a non-negative integer: "))
print_all_23n8(user_num)