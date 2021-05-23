print("------Update a tuple in python------")
a=("Anana","Mango","Orange","Apple")
b=list(a)
b[1]="Banana"
a=tuple(b)
print(a)