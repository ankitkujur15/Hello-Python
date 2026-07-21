# FILE HANDLING in python

open("hello.txt", "x")  # → creates a new file named hello.txt

file = open("superman.txt", "w") # → creates a new file named superman.txt and opens it in write mode

data = input("what you want to write in the file? : ")
file.write(data)  # → writes the data in the file

file = open("chap15.py", "r")  # → opens the file in read mode

print(file.read()) # → reads the data from the file

file = open("superman.txt", "a")  # → opens the file in append mode  --   append meaning -> Add new data to the end of an existing file without deleting its current contents.
file.write("\nI am superman")  # → appends the data in the file
file.close()  # → closes the file


# ------------ Note : always use "with" statement while working with files in python. 
# With - is a statement ---- it automatically closes the file for you, even if an error occurs            e.g -

with open("superman.txt", "a") as file:
    file.write("\n who the hell is superman?")  # → appends the data in the file


# Note i have deleted the files hello.txt and superman.txt from my directory after running this code
# so if you run this code again it will give an error because the files are not present in the directory.
# if you want the file run above code again sequentially.