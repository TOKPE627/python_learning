import math;
import random;


print("-------MATH Functions--------")
print("******SQRT*******")
print(math.sqrt(9))

print("******POW*******")
print(math.pow(3,2))

print("******LOG*******")
print(math.log(4))

print("******CEIL*******")
print(math.ceil(6.2))

print("******FLOOR*******")
print(math.floor(6.2))

print("-------RANDOM Functions----------")

print("******RANDRANGE*******")
print(random.randrange(3,9))

print("******SEED*******")
random.seed(10)
print(random.random())

print("******CHOICE*******")
new_list=["apple","banana","cherry"]
print(random.choice(new_list))

print("******UNIFORM*******")
print(random.uniform(20,60))

print("******TRIANGULAR*******")
print(random.triangular(20,60,30))