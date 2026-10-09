def foo1(a, b):
     '''type contract looks like this:
          (number,number)->None'''
     print(a+b)

def foo2(a, b):
     '''type contract looks like this:
          (number,number)->number'''
     return a+b

def foo3(a,b):
     ''' type contract looks like this:
          (number,number)->number'''
     print("Welcome to my silly function")
     print("First I will print a +b:")
     print("a+b=", a+b)
     print("Now I will also return that value")
     return a+b

def foo4(a, b):
     '''type contract looks like this:
          (number,number)->None'''
     print(a+b)
     return

# 1st uncomment the next line and save. What will the program print when you press Run Module
foo1(5,5)      # 10

# 2nd uncomment the next line and save. What will the program print when you press Run Module 
foo2(5,5)      # None


# 3rd uncomment the next line and save. What will the program print when you press Run Module 

x1=foo1(5,5)        # 10
x2=foo2(5,5)        # None
x3=foo3(5,5)        # Welcome to my silly function\nFirst I will print a +b:\na+b= 10\nNow I will also return that value\n
x4=foo4(5,5)        # 5

# 4th uncomment the following 8 lines, and save. What will the program print when you press Run Module 

print("x1=", x1)                        # x1= None
print("type of x1 is ", type(x1))       # type of x1 is  <class 'NoneType'>
print("x2=", x2)                        # x2= 10
print("type of x2 is ", type(x2))       # type of x2 is  <class 'int'>
print("x3=", x3)                        # x3= 10
print("type of x3 is ", type(x3))       # type of x3 is  <class 'int'>
print("x4=", x4)                        # x4= None
print("type of x4 is ", type(x4))       # type of x4 is  <class 'NoneType'>

# 5th uncomment the following 2 lines, and save. What will the program print when you press Run Module 

num1=x2*x3                    #
print("x2*x3=", num1)         # x2*x3= 100

# 6th uncomment the following 2 lines, and save. What will the program print when you press Run Module 
num2=x1*x2                    #
print("x1*x2=", num2)         # Error: unsupported operand type(s) for *: 'NoneType' and 'int'
