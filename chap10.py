# Function  reusable block of code


# implicit (pre-defined) function

print()
input()
len()
int()
float()
str()

# explicit (user-defined) function
def hello():
    print("hello world")
    print("hello python")

hello()

# parameter functions --
# the variable name in the function definition. like a placeholder

def addition(a, b):
    print(a + b)

addition(5, 6)

#------------------------------------------------------------------------------------------
# argument functions --
# the actual value passed to the function when calling it

addition(10, 20)  # -> (a=10, b=20) is argument function


def palidrome_checker(num):
    copy = num
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num =  num // 10
    
    if rev == copy:
            print(f"{copy} is a palindrome")
    else:
            print(f"{copy} is not a palindrome")

palidrome_checker(986)
palidrome_checker(121)
palidrome_checker(12321)

"""
parameters are the values you accept while 
calling the function
* and
arguments are the values you pass while calling the function
"""

#------------------------------------------------------------------------------------
# types of arguments
# 1. positional  arguments


def multiply(a,b,c,d):
      print(a*b*c*d)

multiply(8,7,3,2)


# 2. default arguments

def add(a, b, c = 7):
      print( a + b + c)

add(5,5)

# 3. keyword argument

def substraction(a, b):
      print(b - a)

substraction(b = 30, a = 50)  #order dosen't matter















