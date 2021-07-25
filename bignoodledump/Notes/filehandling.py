# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# append mode
open("filename.txt", "a")

# binary modes
open("filename.txt", "wb")
open("filename.txt", "rb")
open("filename.txt", "ab")

file = open("filename.txt", "r")
file.read()     # optional argument allows to specify how many bytes to read
file.readlines()    # list of lines

for i in file:  # iterate over each line
    print(i)
file.close()

file = open("filename.txt", "w")  # opening in write mode deletes the contents
file.write("Hello World")     # writes the file, returns the number of bytes
file.close()

file = open("filename.txt", "a")
file.write("\nGame of Thrones")
file.close()

# It can be good practice to setup file handling like so:

try:
    file = open("filename.txt", "r")
    print(file.read())
finally:
    file.close()

# or like so:

with open('filename.txt', 'r') as f:    # after the indentation f is deleted
    for i in f:
        me = ''
        for u in i.split(' '):
            me = me + u[0]
        print(me)



