nDisks=int(input("Please enter the number of disks: "))

def hanoiTour(nDiks, begin, interm, end):  
    if(nDisks == 1):  
        print('Move disk 1 from rod {} to rod {}'.format(begin, end))  
        return
    hanoiTour(nDisks - 1, begin, end, interm)  
    print('Move disk {} from rod {} to rod {}'.format(nDisks, begin, end))  
    hanoiTour(nDisks - 1, interm, begin, end)  
   
hanoiTour(nDisks, 'A', 'B', 'C')