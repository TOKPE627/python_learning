import os;

#Python program to manage file
#@Author TOKPE Kossi
#@Date 7-06-2021
#@Company Sharda University
#@School MSC
#@Student Id: 2020801137

print("\n********Welcome to our new program for management of File*******\n")
#Create a new file if it does not exit
print("\n---------Create a new file if it does not exit in directory:-----------\n")
f=open("myNewFile","a")
#read the path of the file

print(os.getcwd())

#Writing of content in the file created
print("\n------Writing of content in the file created-----------\n")
f.write("Python is really a good language.\n Everyone must learn python programming")
#Reading the content of the file
f=open("myNewFile","r")
print(f.read())

#Append mode in the file
print("\n-------Append mode in the file----\n")
with open("myNewFile","a") as myfile:
    myfile.write("\nLearning everyday makes strong person")

#Reading the new content of the file
f=open("myNewFile",'r')
print(f.read())

#Return the current file position after reading the first line:
print("\n-------tell() function: Return the current file position after reading the first line-----\n")
f=open("myNewFile","r")
print(f.readline())
print(f.tell())

#We want to move the file pointer to another position.
print("\n-------seek() function: We want to move the file pointer to another position.----\n")
f=open("myNewFile","r")
f.seek(4)
print(f.readline())

print("\n**********Thank your for using our program*******\n")
f.close()