# Tuple  - immutable
"""
A tuple is exactly like a list, except you cannot change it once created. 
Use tuples for data that should stay constant — 
like days of the week, coordinates, or config values.

"""

a = ()
print(type(a))


# we can convert a list into tuple

b =["monday", "tuesday", 123 , 244, 123, 124, 123, 123, 45, 53, 123, 123, 9975, 89, 79, 67, 40, 123]

tup = tuple(b)
print(type(tup))

# it has immutable nature - you cannot change any values inside your tuple

# Methods --

# index

print(tup.index("tuesday"))          # 1 -> returns the index value for tuesday

# count

print(tup.count(123))         # 7 -> returns the number of occurance

# use case - pack and unpack

def students():
    return "ankit", 26, "ankit7903@gmail.com"

info = students()
name, age, email = info                        # unpacking a tuple

print(name)
print(age)
print(email)