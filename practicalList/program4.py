#Python program to find largest number in a list
#creation of empty list
arr1= []
print()
print("---Welcome in largest number finder program----")
print()
arrSize=int(input("Enter the number of elements of the list: "))
for i in range(1,arrSize+1):
    element = int(input("Enter an element: "))
    arr1.append(element)
print()
print("The largest element of the list is:", max(arr1))
