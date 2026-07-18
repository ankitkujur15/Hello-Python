# set

"""  Set — Unique Values Only
A set automatically removes duplicates and has no guaranteed order. 
Great for checking membership and performing math-style set operations.
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

s = set(l)
print(s)                 # print only unique values


s = {1 , "hello", (1,2,3)}

s = {10, 20, 30, 40}

for i in s:
    print(i)             # print the values unordered

# methods

s.add(60)             # add element in set
print(s)


s.clear()               # empty a set

s = {90, 20, 40, 50, 70, 80}

s.discard(40)           # removes the specific element from the set
print(s)

s.pop()              # removes the random element from a set
print(s)    
