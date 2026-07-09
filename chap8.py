# For Loop - for Numbers (always have to use range() fun)
"""
* The range() Function
range() generates a sequence of numbers. Think of it as saying "count from here to there".

range(stop)             # 0 up to stop-1
range(start, stop)      # start up to stop-1
range(start, stop, step)# start, jumping by step

"""

#range 10 - 100
range(10, 101, 1)

#range 23 - 56
range(23, 57, 1)

#range 0 - 45
range(46)


# syntax of for loop
"""
* for variable in range(start, stop, step): 
    # code block to be executed
"""

# for i in range(10,21,1):
#     print(i)


# table
n = int(input("Enter a number to print its table: "))

for i in range(n, (n*10)+1, n):
    print(i)

#---------------------------------------------------------------
# for loop for string (2 ways)

# 1st way
a = 'python'
for i in a:
    print(i)

# # 2nd way using indexing

b = 'studora'
for i in range(len(b)):
    print(f"Index {i} = {b[i]}")
    """
        Index 0 = s
        Index 1 = t
        Index 2 = u
        Index 3 = d
        Index 4 = o
        Index 5 = r
        Index 6 = a
 
       """
#--------------------------------------------------
# break, continue & else 

for i in range(1, 11):
    if i == 4:
        break
    print(i)

print("********************************************")

for i in range(1, 11):
    if i == 4 or i == 7 or i == 9:
        continue   # is used to breaking one iteration in the loop, not the entire loop
    print(i)

print("********************************************")

for i in range(1, 11):
    if i == 45:
        print(i)
else:
    print("no break was encountered in the loop")  # else block will be executed if no break is encountered in the loop


#---------------------------------------------------------------

#que 1

n = int(input("tell me your no : "))

for i in range(n):
    print("hello world")

#----------------------------------------------------

#que 2 Print natural numbers from 1 to n.

n = int(input("enter a no. : "))

for i in range(1, n+1):
    print(i, end=" ")
        
# -----------------------------------------------------

# Que 3 reverse natural numbers from n to 1.

n = int(input("enter a no. : "))

for i in range(n , 0, -1):
    print(i, end=" ")

#-------------------------------------

#Que 4

n = int(input("enter a no. : "))

for i in range(n, n*10+1, n):
    print(f"{n} x {i//n} = {i}")

#----------------------------------------------------------

#que 5 sum of n natural numbers

n = int(input("enter a no. : "))
sum = 0

for i in range(1, n+1):
    sum += i

print(f"sum of {n} natural numbers is : {sum}")

#----------------------------------------------------------

#que 6 factorial of a number

n = int(input("enter a no. : "))
fact = 1

for i in range(1, n+1):
    fact *= i

print(f"factorial of {n} is : {fact}")


#-----------------------------------------------------------------
# que 7

start = int(input("enter starting no. : "))
end = int(input("enter ending no. : "))

start_sum = 0
end_sum = 0

for i in range(start, end+1, 1):
    if i % 2 == 0:
        start_sum += i
    else:
        end_sum += i

print(f"Even sum = {start_sum}")
print(f"Odd sum = {end_sum}")

#-----------------------------------------------------------------------------------

#que 8 all factorial of a number

num = int(input("enter a no. : "))
print("factors are: ")

for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")


#---------------------------------------------------------------------------------

#Que 9 prime number or not