#       01234567890123
parrot="Norwegian Blue"
print(parrot)
print(parrot[12])  #u
print()
print("Program using parrot array to display we win with each character per line") 
givenInput="we win"

print()
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[-1])
print(parrot[-14])


#        01234567890123
parrot1="Norwegian Blue"
#Slices             012345
print("Slices\n")  #Norweg
print(parrot1[0:6])
print(parrot1[3:5])
print(parrot1[0:9])
print(parrot1[:9])
print(parrot1[10:14])
print(parrot1[10:])
print(parrot1[:6])
print(parrot1[6:])
print(parrot1[:6] + parrot1[6:])
print(parrot1[:])

print(parrot1[-14:-8])
print(parrot1[-4:-2])
print(parrot1[-4:12]) #Nre
print(parrot1[0:6:3]) #Nw

number="9,223;372;036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else  " " for char in number).split()

print([int(val) for val in values])