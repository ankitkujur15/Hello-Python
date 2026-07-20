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

# single set methods

s.add(60)             # add element in set
print(s)


s.clear()               # empty a set

s = {90, 20, 40, 50, 70, 80}

s.discard(40)           # removes the specific element from the set
print(s)

s.pop()              # removes the random element from a set
print(s)    

# multiple set methods

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

# difference  (-)

print(s1.difference(s2))      # returns the difference of two sets  or 
print(s1 - s2)



# differene_update ( -= )
s2 -= s1
print(s2)

# intersection ( & )

print(s1. intersection(s2)) # or ->  s1 & s2

# intersecton update ( &= )
s1 &= s1

#is subset ( <= )

s3 = {30, 40}

print(s3 <= s2)

# super set ( >= )

# symmetric difference ( ^ )

print(s1 ^ s2)

# symmetric_difference_update	( ^= )

# union

print(s1 | s2)