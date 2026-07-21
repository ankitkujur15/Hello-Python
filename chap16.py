# EXCEPTION HANDLING in python

"""
Errors vs Exceptions
❌ Errors (unfixable)
SyntaxError — wrong syntax
IndentationError — bad spacing
TabError — mixing tabs/spaces

✅ Exceptions (handleable!)
ZeroDivisionError
TypeError
ValueError
FileNotFoundError

* Exceptions can be handled using > try / except / else / finally / raise
"""

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

try:                                                                # catches error and allows you to move forward with the remaing code
    print(a//b)
except Exception as err:
    print(f"Sorry an error occcured at {err}")
else:                                                               # have the least priority runs if except fails
    print("No errors occured")
finally:                                                                                    # run no matter what
    print(" if there are errors or not This block will for sure run")


name = input("Enter your name: ")
print(f"Hello my name is {name}")




# raise -> is used to generate manuel errors

age = int(input("enter your age : "))

if age < 18:
    raise TypeError("Sorry you are not eligible to vote")
else:
    print("You are eligible to vote")