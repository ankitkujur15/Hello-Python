# dictionary
"""
A dictionary stores data as key: value pairs — 
like a real dictionary where you look up a word (key) to find its meaning (value).
"""

# d = {10:100, 20:200, 30:300, 40:400}

# print(d[10])         # access the value of key 10 -> 100


# d[50] = 500          # create a new key-value pair in dictionary (one way)
# print(d[30])         # read the value of key 30 -> 300
# d[10] = 1000         # update the value of key 10


# print(d)

# # method approach

# dic = {10:100, 20:200, 30:300, 40:400}
# dic.clear()          # empty the dictionary


# # fromkeys() method  -> returns a  dictionary with the specific keys and values
# dic = {10:100, 20:200, 30:300, 40:400}

# q = dic.fromkeys([10,20], 50)
# print(q)             # {10: 50, 20: 50}

# # get() method  -> returns the value of the specific key
# print(dic.get(10))   # 100


# # items() method  -> returns the list of key-value pairs in a dictionary
# print(dic.items())   # dict_items([(10, 100), (20, 200


# # keys() method  -> returns the list of keys in a dictionary
# print(dic.keys())    # dict_keys([10, 20, 30, 40])

# # values() method  -> returns the list of values in a dictionary
# print(dic.values())  # dict_values([100, 200, 300, 400])
 
# # pop() method  -> removes the specific key-value pair from a dictionary
# dic.pop(10)
# print(dic)            # {20: 200, 30: 300, 40: 400}


# # popitem() method  -> removes the last key-value pair from a dictionary

# print(dic.popitem())   # (40, 400)


# # setdefault() method  -> returns the value of the specific key. If the key does not exist, insert the key with the specified value

# dic = {10:100, 20:200, 30:300, 40:400}
# print(dic.setdefault(60, 500))   # 500

# print(dic)                        # {10: 100, 20: 200, 30: 300, 40: 400, 60: 500}

# # update() method  -> updates the dictionary with the specified key-value pairs
# dic.update({10:1000, 80:800})

# print(dic)                        # {10: 1000, 20: 200, 30: 300, 40: 400, 60: 500, 80: 800}

# # values() method  -> returns the list of values in a dictionary
# print(dic.values())  # dict_values([1000, 200, 300, 400, 500, 800])

# traversing in a dictionary

# dic = {10:100, 20:200, 30:300, 40:400}

# for i in dic:
#     print(f"key {i} : value {dic[i]}")


#------------------------------------------------------------------------------------------------------------------------------------------------------

