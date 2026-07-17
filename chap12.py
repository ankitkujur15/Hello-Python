# List

# ordered nature  ---- you can access any element at any point of time 

a = [12,57,78,88,90]
print(a[1])

#---------------------------------------------------------------------------------------
# mutale natute -- you can change any value of your list

# a = "HELLQ"    # immutable nature (string)
# a[-1] = "0"    # TypeError: 'str' object does not support item assignment

b = [10,22, 30, 40, 50]

b[1] = 20
print(b)

#---------------------------------------------------------------------------------
# duplicates are allowed in list

t = [1,1,1,1,2,2,2,2,2,3,3,3,3,3]

#--------------------------------------------------------------------
# traversing in list (using loop)
a = [10, 20, 30, 40, 50]

#traversing on values

for i in a:
    print(i)


#traversing on index

for i in range(0,len(a)):
    print(f"{i} : {a[i]}")




#-----------------------------------------------------------------------------------------
# Methods of list

a = [10, 20, 30, 40, 50]

# append 
a.append(60)  #add the value to the last spot

print(a)

#insert

a.insert(2,25) # add values whenever you want
print(a)

#delete

l = [10,20,30,40,55,60]

b = l.pop(5)     # pop

l.remove(55)  # removes only the first occurance

l.clear()    # removes the entire elements on a list
print(l)


#  sort()
li = [84,62,95,20,40,33,54]

li.sort()    # ascending 
print(li)

li.sort(reverse= True) # decending
print(li)

# list reverse

li = [1,2,3,4,5,6,7,8]

li.reverse()     # reverse list
print(li)