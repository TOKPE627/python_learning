data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
flower = "blue violet" 
print('blue' in flower)
flower = "rose"
colour = "red"
print("The {0} is {1}".format(flower,colour))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])   #The slice starts at the first character, and includes every 5th character.
letters="abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]  
b2= letters[25:-1:-1]
b3=letters[25::-1]
b4=letters[::-1]
print(b3)
print(b4)

#      -23              -15 -14 -13 -12 -11 -10 -9  -8  -7 -6  -5  -4   -3  -2  -1
# 0 1 2 3 4 5 6 7 8 9 10 11 12   13 14  15  16  17  18  19  20  21  22   23  24  25
# a b c d e f g h i j k  l  m     n  o  p   q   r   s  t    u  v    w   x    y  z  

letters2="abcdefghijklmnopqrstuvwxyz"

print(letters2[-10:-13:-1])  #qpo
print(letters2[16:13:-1])    #qpo
print(letters2[-22:-27:-1])  #edcba
print(letters2[4::-1])       #edcba 
print(letters2[:-9:-1])  #last 8 characters in reverse order
print(letters2[-4:])
print(letters2[-1:])
print(letters2[1:])
print(letters2[:1])
print(letters2[0])
print(letters2[::-1])

