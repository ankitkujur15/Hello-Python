# Que 1 --> print the negative and positive element seperatly from the list


l = [3, -1, 8, 6, -4, 9, -9]

# l = list(map(int, input("Eneter number seperated by space: ").split()))        -> user input

pos = []
neg = []

for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(f"your positive elements are {pos}")
print(f"your negative elements are {neg}")


#-------------------------------------------------------------------------------------------
# Que 2 find (mean) average of all list elements

l = [10, 20, 30, 40, 50]
sum = 0
for i in l:
    sum = sum + i

print(f"your average is {sum/len(l)}")



#---------------------------------------------------------------
# Que 3 find the greatest element and print its index

l = [4, 8, 2, 9, 1]

largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"the largest value is : {largest}")
print(f"its index is : {index}")



#----------------------------------------------------------------------------------------------

# Que 4 find the second largest element

l = [84, 8, 62, 95, 20, 40, 33, 54, 91]

largest = l[0]
sec_largest = l[0]

for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(f"the second largest element in the list is {sec_largest}")



#-------------------------------------------------------------------------------------------------------

#Que 5 check is the list is already sorted

l = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(l) - 1):
   
    if l[i] > l[i+1]:
        print("Your list is not sorted")
        break
else:
    print("your list is sorted")