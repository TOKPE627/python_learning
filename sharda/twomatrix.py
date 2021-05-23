K=[]
s=int(input("Enter the size of the first matrix:X*X: "))
print("Please enter the elements")
for i in range(s):
    z=[]
    for j in range(s):
        z.append(int(input()))
    K.append(z)
print(K)

print("The first Matrix is:")
for i in range(s):
    for j in range(s):
        print(K[i][j], end=" ")
    print()
L=[]

s=int(input("Enter the size of the second Matrix: Y*Y: "))
print("Please enter the elements")
for i in range(s):
    z=[]
    for j in range(s):
        z.append(int(input()))
    L.append(z)
print(L)

print("The second Matrix is:")
for i in range(s):
    for j in range(s):
        print(L[i][j], end=" ")
    print()
finalMat=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(s):
    for j in range(len(K[0])):
        finalMat[i][j] = K[i][j] + L[i][j]
print("The obtained final matrix is: ")
for f in finalMat:
  print("Sum of the two Matrix is:", f)

    

