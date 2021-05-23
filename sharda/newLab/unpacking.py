print("------Unpacking a tuple in python-------")

def newOPeration(a,b,c):
    return a*b*c
print(newOPeration(3,2,9))

#Creation of a new tuple
k=(3,2,9)
#Then tuple is passed
#Unpacking
print(newOPeration(*k))