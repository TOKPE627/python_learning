a=input("Enter the tuple element: ").split(" ")
element = input("Enter the element you want to search: ")
for i in range(len(a)):
    if(element==a[i]):
        print("Element found at position {}", format(i+1))