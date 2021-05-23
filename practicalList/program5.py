#WAP in python to find the Armstrong Number.
  #153 = 1*1*1 + 5*5*5 + 3*3*3.
print()
print("----Welcome in Armstrong Number Program----")
element=int(input("Enter a number:"))
sum=0
temp=element

while temp>0:
    digit=temp%10
    sum+=digit **3
    temp//=10

if element==sum:
    print(element,"is an armstrong number")
else:
    print(element,"is not an Armstrong number")
