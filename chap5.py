# INPUT, OUTPUT & OPERATORS


print("Input , Output & operators")

# output -> print() function is used to display output on the screen

# name = 'Alice'
# age = 26

# print(name)             # basic   → Alice
# print(f"My name is {name} and My age is {age}")  # formatted → My name is Alice and My age is 26

# #we are able to use variable inside a string with the help of f-string (formatted string)

# #use of multiple data types in print() function

# print("Hi my name is", name, "and my age is", age) 


#--------------------------------------------------------------

#input -> input() function is used to take input from the user

# name = input("what is your name? ")  

# print('hello my name is', name)  # → hello my name is Alice

# age = int(input("what is my age? "))

# print('my age is', age)  # → my age is 26

#--------------------------------------------------------------
# Arithmetic Operators
# (+ , - , * , / , // , % , ** )

a = 10
b = 5
print(a + b)  # → 15
print(a - b)  # → 5
print(a * b)  # → 50
print(a / b)  # → 2.0   * all division in python 3 is float division  -> if required you need to type cast to int
print(a // b) # → 2     * so the floor division operator  automatically converts the result to int
print(a % b)  # → 0
print(a ** b) # → 1048576

""" precidance of operators

() - Brackets
** - Exponant (right to left: 2**3**2 = 2**(3**2) = 2**9 = 512)
* / // % - Multiplication, Division, Floor Division, Modulus (left to right)
+ - Addition, Subtraction (left to right)
"""

print(3 + 4 * 5)  # → 23
print(15 // 4 + 15 % 4)  # → 3 + 3 = 6
print(3 + 2 ** 2 * 5 - 1)  # → 3 + 4 * 5 - 1 = 3 + 20 - 1 = 22

#--------------------------------------------------------------

#comparison Operators
#Always return True or False.

# (== , != , > , < , >= , <= )

print(10 == 10)  # → True
print(12 > 14)  # → False
print(12 < 45)  # → True
print(12 >= 12)  # → True
print( 45 <= 56) # → True

print(12 != 12)  # → False

#--------------------------------------------------------------

#Logical Operators (compare multiple values together)
# and , or , not    

print(12 > 10 and 34 == 34)  # → True
print(12 > 10 and 87 >56 and 34 == 45)  # → False

print(12 > 10 or 34 == 34 or 56 < 45)   # → True

print(not (12 > 10))          # → False
# not operator reverses the boolean value of the expression



#--------------------------------------------------------------

#Assignment Operators
# used to assign values to variables

# = , += , -= , *= , /= , //= , %= , **=

a = 10

a = a + 10  
a = a + 10
a = a + 10
print(a)  # → 40 

# for shoertcut we can use assignment operators

b = 20
b += 10  # equivalent to b = b + 10
b += 10
b += 10

print(b)  # → 50


# and so on for other assignment operators