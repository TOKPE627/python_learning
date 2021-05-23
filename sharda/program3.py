x=[int(x) for x in input("Enter the digits for list one: ").split(",")]
y=[int(y) for y in input("Enter the digits for list two: ").split(",")]

z=x+y


print("List one: ", x)
print("List two: ", y)
print("Combined list is: ", z)
print("Second largest value is: ",z[-2])