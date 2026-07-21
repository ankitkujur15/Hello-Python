# CONDITIONAL STATEMENTS

# they make decisions based on certain conditions.


#if condition:      -> you have one condition to check


if True:
    print("This is true")  # → This is true

#take input of age from user and check if the user is eligible to vote or not

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

  #---------------------------------------------------------------------------  

# if-while-else statement 

rupees = int(input('give  money -'))
if rupees  == 10:
    print('you can buy a chocolate')
elif rupees == 20:
    print('you can buy a burger')
else:
    print('bukha marega ga tu')

#--------------------------------------------------------------
#que 1

num1 = int(input('1st no - '))
num2 =int(input('2nd no - '))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

#-------------------------------------------------
#Que2 


print('hello' == 'hello')  # → True

gen = input('please tell me your gender in (M or F) : ')
if gen == 'M' or gen == 'm':
    print('good morning sir')
elif gen == 'F' or gen == 'f':
    print('good morning maam')
else:
    print('invalid input')

#----------------------------------------------------
#que3

a = int(input('tell me your number - '))

if a % 2 == 0:
    print(f"{a} is even number")
else:
    print(f"{a} is odd number")

#-------------------------------------------
# Que4

name = input('tell me your name - ')
age = int(input('tell me your age - '))

if age >= 18:
    print(f'hello {name} you are a valid voter')
else:
    print(f'hello {name} you can vote after {18 - age} years')

#---------------------------------------------------------------
# Que 5

year = int(input('enter the year - '))

if year % 100 == 0 and year % 400 == 0:            # for century year it should be divisible by 400 to be a leap year
    print(f'{year} is a leap year')
elif year % 100 != 0 and year % 4 == 0:            # for non-century years, it should be divisible by 4
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
    
#----------------------------------------------------------------------------
# Que 6

temp = int(input('enter the temperature - '))

if temp >= -5 and temp <= 5:
    print('it is very cold')
elif temp >= 6 and temp <= 18:
    print('it is moderate')
elif temp >= 19 and temp <= 30:
    print('it is hot')
else:
    print('it is very hot')
