#Remove a specific element in a tuple
a=("Anana","Mango","Orange","Apple")
b=list(a)
b.remove("Orange")
a_final=tuple(b)
print(a_final)

#Remove all the tuple completely
new_tuple = ("India", "Senegal", "Nigeria","South Africa")
del new_tuple
print(newtuple) #this will raise an error because the tuple no longer exists 