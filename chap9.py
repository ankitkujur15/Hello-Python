# while loop

a = 1
while a != 20:
    print(a)
    a += 1

"""
The while loop keeps running as long as a condition is True. 
You use it when you don't know how many times you'll need to repeat.


*Infinite Loop Danger!
Always make sure your condition will eventually become False — otherwise your program runs forever!
"""

#----------------------------------------------------------

#Que 1 Separate each digit of a number and print on a new line.

# basic logic
a = 6789

print(a % 10)
a = a // 10
print(a % 10)
a = a // 10
print(a % 10)
a = a // 10
print(a % 10)

#better logic

b = int(input("enter a no. : "))
while b != 0:
    print(b % 10)
    b = b // 10

#----------------------------------------------------------------------------

# Que 2 accept a number and reverse

a = int(input("tell me your no : "))

rev = 0
while a != 0:
    rev = rev * 10 + a % 10
    a = a // 10

print(f"reversed no. is : {rev}")

#------------------------------------------------------------------------------------------
# Que3 palindrome or not

a = int(input("tell me your number: "))
copy = a
rev = 0
while a != 0:
    rev = rev * 10 + a % 10
    a = a // 10

if rev == copy:
    print(f"{rev} is a palindrome no!")
else:
    print(f"{rev} is not a palindrome no!")