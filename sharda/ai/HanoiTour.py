# Python program to implement Hanoi Tour Algorithm
#@Author TOKPE Kossi
#@Date 23 April 2021
#Student at School of Technology and Engineering
#Student Id 2020801137
#Sharda University

  
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
nDisks=int(input("Please enter the number of disks: "))
TowerOfHanoi(nDisks,'A','B','C') 
# A, C, B are the name of rods