
k = input("Please input a key: ") 
v = input("Plesse input a value: ") 
classe_list={k:v} 
print(classe_list)

N = int(input())

Arr = [int(i) for i in input().strip().split(' ')]

D = {}

for i in range(len(Arr)):

D[i] = Arr[i]

print(D)