print("Hello, WORLD!")

#Indentation
print("-------Indentation------")
if 5> 2:
    print("Five is greater than two!")
    print("EE")

#types
print("-------Types---------")
x=5
y="Koss"
print(type(x))
print(type(y))


#Case-sensitive
print("-------Case-sensitive-------")
a=4
A="Amit"
print(a)
print(A)

#Assignment
print("------Assignment------")
x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("------Unpacking------")
fruits = ["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

print("---------Output----------")
x="easy"
print("Python is " + x)
y=5
z=4
print(y+z)

k="Kossi"

print("-------Data types-------")
print("---String---")
a1="Hello everyone"
print(a1)
print("----integer----")
a2=30
print(a2)

print("----Complex----")
a3=5j
print(a)

print("--List---")
b=["apple","banana","cherry"]
print(b)
print("---Tuple----")
c=("apple","banana","cherry")
print(c)
print("---Dictionaries---")
c={"name":"Amit","age":43}
print(c)
print("----Set---")
d={"apple","banana","cherry"}
print(d)
print("----Boolean---")
m=True
print(m)

print("---Type conversion---")
x = 1 # int
y = 2.8 # float
z = 1j # complex

a=float(x) #int to float
print(a)

b=int(y)  #float to int
print(b)
c=complex(x) #int to complex
print(c)
print(type(a))
print(type(b))
print(type(c))

print("-----Random numbers---")
import random
print(random.randrange(1,10))
 #         54321-
 # 012345678901 
a="Hello, World!"
print(a[1])
print(len(a))

print("-----Slicing--")
print(a[2:5]) #llo  #Get the characters from position 2 to position 5 (not included)

print(a[:5]) #Hello #Get the characters from the start to position 5 (not included).

print(a[2:]) #llo, World  #Get the characters from position 2, and all the way to the end.

print(a[-5:-2]) #orl # From: "o" in "World!" (position -5)
                      # but not included: "d" in "World!" (position -2)
print("-------Modify Strings--------")
a=" Hello,World!  Are you ok!"
print(a.upper())
print(a.lower())

print("------Remove space---")
print(a.strip())
print("-----Replace letters---")
print(a.replace("H","Koss"))
print("----String concatenation-----")
a="Hello"
b="World"
c=a+b
print(c)
print(a+ " " + b)
print("-----String format-----")
age=36
txt="My name is Kossi, and i am {}"
print(txt.format(age))

print("-----Break Statement:----")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
    #1 2 3
print("----Continue Statement:----")
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
    #1 2 4 5 6
print("-----Else Statement----")
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

print("----For Loops-----")
languages = ['english',"dutch","french","hindi"]
for l in languages:
    print(l)

print("------Looping Through a String-------")
for k in 'python':
    print(k)

print("-----The break Statement in for loop-----")
fruits = ["apple","banana","cherry","mango"]
for f in fruits:
    print(f)
    if f=='banana':
        break
    #apple, banana

print("-----------")
for fr in fruits:
    if fr=="banana":
        break
    print(fr)
print("------Continue--")
for ft in fruits:
    if ft=="banana":
        continue
    print(ft)

print("-----Range------")
for x in range(6):
    print(x)
    #0 1 2 3 4 5
print("-----Range but not include the end -------")
for i in range(2, 6):
    print(i)
    #2 3 4 5
print("------Range by Increment------")
for u in range(1,20,3):
    print(u)

for x in range(6):
    print(x)
else:
    print("Loop finished!")

print("------Range with Break Statement-------")
for k in range(6):
    print(k)
    if(k==3):
        break
else:
    print("Loop finished!")

print("------Nested For loops---")
color=["red","blue","green"]
fruits=["apple","banana","cherry"]
for x in color:
    for y in fruits:
        print(x,y)

print("----Pass Statement-----")
for x in [0,1,2]:
    pass

print("------Lists------")
x=[1,2,3,4,5]
print(x)
List=['Pascal','Thit','Goel','Amit','Pascal']
print(List)
print(len(List))
print(List[1])
if "Amite" in List:
    print("Yes, 'Amit' is found successfully in the list")
else:
    print("Not found!!")
List[2]="Voltaire"
print(List)
List[1:3]=["Kiri","Sheldon"]
print(List)
List2=['Pascal','Thit','Goel']
List2[1:2]=["blackeff","whiteeff"]
print(List2)
List3=['Pascal','Thit','Goel']
List3[1:3]=["Manisha"]
print(List3)

print("------Insert Item-------")
List4=['Pascal','Thit','Pascal']
List4.insert(2,"watermelon")
print(List4)

print("------Append Item--------")
List5=['Pascal','Thit','Pascal']
List5.append("orange")
print(List5)

print("-------Extend Current List--------")
LT=['Pascal','Thit','Pascal']
List6=["Israel","Palestine","India","Pakistan","NEPAL"]
LT.extend(List6)
print(LT)

newList=['Pascal','Thit','Pascal']
print("----------Add Any Iterable to the current List------")
newTuple=("Kizi","Roko","Nikil")
newList.extend(newTuple)
print(newList)

print("---------Remove item---------")
kl=["Kizi","Roko","Nikil"]
kl.remove("Roko")
print(kl)

zL=["Kizi","Roko","Nikil"]
zL.pop(2)
print(zL)

print("---------Loop a list with for loop--------")
listN = ["apple", "banana", "cherry"]
for l in range(len(listN)):
    print(listN[l])

print("-----Loop With while loop-------")
i=0
while i<len(listN):
    print(listN[i])
    i=i+1
print("-------List Comprehension-------")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newL=[]
for x in fruits:
    if 'c' in x:
        newL.append(x)
print(newL)
print("------------------")
newL2=[x for x in fruits if 'a' in x]
print(newL2)

print("----------Set Outcome in the list------")
nLp=['HiIndia' for x in fruits]
print(nLp)

print("---------Sort Descending--------")
listN = ["orange", "mango", "kiwi", "pineapple", "banana"]
listN.sort(reverse=True)
print(listN)

print("----------Sort List Alphanumerically------")
listN2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
listN2.sort()
print(listN2)

listN3=[100,50,65,82,23]
listN3.sort()
print(listN3)

print("----------Case Insensitive Sort---------")
listN4 = ["banana", "Orange", "Kiwi", "cherry"]
listN4.sort()
print(listN4)

print("--------Dictionaries--------")
dico1={
      "Name"  : "Amadou",   "Age"   :22, "Course":"MSC"}
dico={
    1:{"Name"  : "Amadou",   "Age"   :22, "Course":"MSC"},
    2:{"Name"  : "Natsigal", "Age"   :10, "Course":"MCA"}
}
print(dico1["Name"])
print(dico[2]["Name"])

dico2 = {
           "brand":"Ford",
           "model": "Mustang",
           "year": 1964,
           "year": 2020,
           "year":2021
}

print(dico2)
print(len(dico2))
print(dico2["model"])
print(dico2.get("model"))
print(dico2.keys())
print(dico2.values())
car = {"brand": "Ford","model": "Mustang","year": 1964}
x=car.keys()
print(x)
car["color"]="White"
print(x)
y=car.values()
print(y)
car["year"]=2021
print(y)
car["country"]="england"
print(y)
print("--------Get a list of the key:value pairs.")
car = {"brand": "Ford","model": "Mustang","year": 1964}
x=car.items()
print(x)
car["year"]=2030
print(x)
print("--------Remove items----------")
dico3 = {"brand": "Ford","model": "Mustang","year": 1964}
dico3.pop("brand")
print(dico3)
dico4 = {"brand": "Ford","model": "Mustang","year": 1964}
dico4.popitem()
print(dico4)
dico5 = {"brand": "Ford","model": "Mustang","year": 1964}
del dico5["model"]
print(dico5)
del dico5
#print(dico5)
dico6 = {"brand": "Ford","model": "Mustang","year": 1964}
dico6.clear()
print(dico6)
dico7 = {"brand": "Ford","model": "Mustang","year": 1964}

print("-------------Print all key names in the dictionary, one by one.----------------------------")
for x in dico7:
    print(x)

print("-------------Print all values in the dictionary, one by one.----------------------------")
for d in dico7:
    print(dico7[d])
print("------------------------")
for d in dico7.values():
    print(d)

print("---------Loop through both keys and values, by using the items() method.--------------")
for x,y in dico7.items():
    print(x,y)

print("------Copy of a dictionary---------")
dico8 = {"brand": "Ford","model": "Mustang","year": 1964}
mydict = dico8.copy()
print(mydict)

print("---------Nested dictionaries-----------")
myfamily = {
             "child1" : {"name" : "Amit","year": 2004},
             "child2" : {"name" :"Ram",   "year": 2007},
             "child3" : {"name" :"Sita",  "year": 2011}
}
print(myfamily)

child1 = {"name" : "AMIT","year" : 2004}
child2 = {"name" : "RAM","year" : 2007}
child3 = {"name" : "SITA","year" : 2011}

dicoFamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(dicoFamily)
print("--------Functions----------")
def my_function():
    print("Hello, World!")
my_function()
def sum():
    a=10
    b=30
    c=a+b
    return c
print("The sum is: ",sum())

def newSum():
    a=20
    b=23
    c=a+b
print(newSum())
print("-------Arguments-------")
def identifyYou(name):
    print("HI HI ", name)
identifyYou("Saley")

def sumNumbers(a, b):
    return a+b
x=int(input("Enter first value: "))
y=int(input("Enter second value:"))
print("Sum= ", sumNumbers(x,y))

print("----------Required-----------")
def func(name):
    message="Hi "+name
    return message
name=input("Enter the name: ")
print(func(name))

print("------Default-------")
def printme(name,age=22):
    print("My name is", name, " and age is", age)
printme(name="RAHIIILMP")

print("-------Variable length Arguments--------")

def my_function(*kids):
    for x in kids:
        print("The youngest child is " +x)
my_function("ARMEL","Pakam","Cedric")

print("---------Keywords arguments---------")
def func(name, message):
    print("printing the message with", name, " and", message)
func(name="Amit", message="Hello Everyone i am a Geek")

print("-------any arguments using Keyword argument----------")
def food(**kwargs):
    print(kwargs)
food(a="Apple")
food(fruits="Orange",Vagitables="Carrot")

def funct(name1, message, name2):
    print("printing the message with",name1,",",message,"and",name2)

funct("John",message="hello",name2="David")

def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))

print("-----------Anonymous function-----------")
x=lambda a : a + 10
print(x(5))

x=lambda a,b : a*b
print(x(5,6))

def myfunct(n):
    return lambda a : a*n
mydoubler=myfunct(2)
print(mydoubler(11))

print("-----------Scope of variable---------")
x="awesome"
def myfunct():
    x="fantastic"
    print("Python is " + x)
myfunct()
print("Python is " +x)

print("-----------------")
def globalScope():
    global x
    x="interesting"
globalScope()
print("Python is " + x)

print("-------------------")
k="easy"
def otherGlobalScope():
    global k
    k="amazing"
otherGlobalScope()
print("Python is " +k)

print("-----------------Exception Handling--------------")
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
except:
    print("Can't divide with zero")

print("-----------tttt-----------------")
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b=%d"%c)
except Exception as e:
    print("Can't divide by zero")
    print(e)
else:
    print("Hi I am else block")

print("-----------Multiple Exceptions--------------")
try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

print("-----------------FINALLY----------------------")
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b=%d"%c)
except:
    print("can't divide by zero")
else:
    print("Hi i am else block")
finally:
    print("Must executed")


print("----------------------------")
try:
    age=int(input("Enter the age:"))
    if(age < 18):
        raise ValueError
    else:
        print("Tha age is valid")
except ValueError:
    print("The age is invalid!")

print("--------Raise with Messaga----------")
try:
    num=int(input("Enter a positive Integer:"))
    if(num <= 0):
        raise ValueError("That is a Negative Number!")
except ValueError as e:
    print(e)

print("-------------------------------")
try:
    a=int(input("Enter a:"))        
    b=int(input("Enter b:"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b=", a/b)
except ArithmeticError:
    print("The value of b can't be 0")


print("------------Raise an Exception--------")
x=-1
if x < 0:
    raise Exception("Sorry, no numbers below zero!")
