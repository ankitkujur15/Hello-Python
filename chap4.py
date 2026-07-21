# STRINGS AND TYPE CONVERSION



# how string works in python
#each character stored in a string has its own uniqueCode -> point value

#example of a string

A = "65"
print(A)  # ord() function returns the Unicode code point for a given character

"""
ord("A")   # → 65  (Unicode of A)
chr(65)   # → "A" (Character from Unicode)

"""
#------------------------------------------------------------------
# String indexing
# each character in a string has an index value, starting from 0

str = "COLLEGE"
print(str[0])  # → C
print(str[5])  # → G

print(str[6], str[-1])  # → E E


# String have 2 types of indexing
"""
 a = "Hello"
   H  e  l  l  o
   0  1  2  3  4   ← positive
  -5 -4 -3 -2 -1   ← negative

print(a[0])   # H
print(a[-1])  # o
"""


#-----------------------------------------------------
# String slicing

# Slicing is used to take out some portion of a string from an original string 

# a[start : Stop : step]  →  start is inclusive, stop is exclusive, step is optional

a = "COLLEGE"
print(a[1:4:1])    # OLL  (index 1,2,3 — 4 excluded)
print(a[0:7:2])    # CLEE  (index 0,2,4 — 7 excluded)
print(a[::-1])   # EGGELLO  (reversed!)

"""
*task
b = 'Hello how are you'

*how
print(b[6:9])  # → how

*Hello
print(b[0:5])  # → Hello
"""

#--------------------------------------------------------
# Type Conversion
#used convert one data type to another using some built-in functions

"""
int() -> whole number

float() -> decimal number

str() -> string (text)

bool() -> boolean (True or False)
"""
a = '12'
b = int(a)  # str converted to int

print(type(a))  # → <class 'str'>
print(type(b))  # → <class 'int'>

"""
> you can reassign a variable to a different data type 
> you can convert string if it holds valid integers
> you can convert float values to int
"""

# boolean()

a = 12
b = 0
c = 12.4
d = 0.0
e = "" 
f = "hello"

print(bool(a))  # → True
print(bool(b))  # → False   
print(bool(c))  # → True
print(bool(d))  # → False
print(bool(e))  # → False
print(bool(f))  # → True

"""  Explanation:
 7 values (only) -> false (get converted to False)
    1. False
    2. 0
    3. 0.0
    4. ""
    5. []
    5. ()
    7. {}


    * rest every value is True (get converted to True)


"""



#Implicit (Automatic) Type Conversion
# python converts automatically when needed

a = 12
print(a/2) # → 6.0 (int converted to float)
# int + float = float

# Explicit (Manual) Type Conversion
# you tell python to convert

a = 12
a = str(a)  # int converted to string
print(a)  # → "12"