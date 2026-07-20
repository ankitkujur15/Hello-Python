# dictionary
"""
A dictionary stores data as key: value pairs — 
like a real dictionary where you look up a word (key) to find its meaning (value).
"""

d = {10:100, 20:200, 30:300, 40:400}

print(d[10])         # access the value of key 10 -> 100


d[50] = 500          # create a new key-value pair in dictionary (one way)
print(d[30])         # read the value of key 30 -> 300
d[10] = 1000         # update the value of key 10


print(d)

# method approach

dic = {10:100, 20:200, 30:300, 40:400}
dic.clear()          # empty the dictionary


# fromkeys() method  -> returns a  dictionary with the specific keys and values
dic = {10:100, 20:200, 30:300, 40:400}

q = dic.fromkeys([10,20], 50)
print(q)             # {10: 50, 20: 50}

# get() method  -> returns the value of the specific key
print(dic.get(10))   # 100


# items() method  -> returns the list of key-value pairs in a dictionary
print(dic.items())   # dict_items([(10, 100), (20, 200


# keys() method  -> returns the list of keys in a dictionary
print(dic.keys())    # dict_keys([10, 20, 30, 40])

# values() method  -> returns the list of values in a dictionary
print(dic.values())  # dict_values([100, 200, 300, 400])
 
# pop() method  -> removes the specific key-value pair from a dictionary
dic.pop(10)
print(dic)            # {20: 200, 30: 300, 40: 400}


# popitem() method  -> removes the last key-value pair from a dictionary

print(dic.popitem())   # (40, 400)


# setdefault() method  -> returns the value of the specific key. If the key does not exist, insert the key with the specified value

dic = {10:100, 20:200, 30:300, 40:400}
print(dic.setdefault(60, 500))   # 500

print(dic)                        # {10: 100, 20: 200, 30: 300, 40: 400, 60: 500}

# update() method  -> updates the dictionary with the specified key-value pairs
dic.update({10:1000, 80:800})

print(dic)                        # {10: 1000, 20: 200, 30: 300, 40: 400, 60: 500, 80: 800}

# values() method  -> returns the list of values in a dictionary
print(dic.values())  # dict_values([1000, 200, 300, 400, 500, 800])

# traversing in a dictionary

dic = {10:100, 20:200, 30:300, 40:400}

for i in dic:
    print(f"key {i} : value {dic[i]}")


#------------------------------------------------------------------------------------------------------------------------------------------------------

# que 1  merge 2 dictionaries into 1

d1 = {'a':10, 'b':20, 'c':30}
d2 = {'d':40, 'e':50, 'f':60}

# d1.update(d2)          # merge d2 into d1
# print(d1)              # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# or without using any method

for i in d2:
    d1[i] = d2[i]
print(d1)              # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# if there exists any commom key in both dictionary, it will automatically update the value of that key

#-------------------------------------------------------------------------------------------------------------------
# Que 2  sum of all values in a dictionary

dic = {'a':10, 'b':20, 'c':30}

sum = 0
for i in dic:
    sum = sum + dic[i]
print(sum)          # 60

#-------------------------------------------------------------------------------------------------------------------
# Que 3 Count the frequency of each element in a list using a dictionary. (important)

li = ["a","b","a","c","b","a","c","c","b","a"]

dic = {}

for i in li:
    if i in dic.keys():                              # check if key exis in the dict -> yes -> increase the count
        dic[i] = dic[i] + 1
    else:                                         # if not -> add the key in dict
        dic[i] = 1
    
print(dic)

#--------------------------------------------------------------------------------------------------------------------

#Que 4 combine two dicts, adding values for common keys

d1 = {"a":5, "b":3}
d2 = {"a":2, "b":4, "c":6}

for i in d2:
    if i in d1.keys():                      # check if exist in d1 -> sums up  the values of d1 + d2
        d1[i] = d1[i] + d2[i]
    else:                                   # create if dosent exist -> adds the key and its values
        d1[i] = d2[i]

print(d1)