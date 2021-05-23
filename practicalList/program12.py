#WAP in python to append a empty list and display the items using for loop.
tab=[]
arraySize=int(input("Enter the size of the list:"))
for i in range(arraySize):
    print("Enter element at position: ", i+1)
    element=input()
    tab.append(element)
print("Final array is:\n")
for i in tab:
    print(i,' ')
