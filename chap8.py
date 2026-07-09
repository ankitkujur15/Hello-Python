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
