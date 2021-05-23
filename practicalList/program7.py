#WAP in python to implement binary search  
def binarySearch(nbList, key):
    """Search key in nbListist[start... end - 1]."""
    start = 0
    end = len(nbList)
    while start < end:
        mid = (start + end)//2
        if nbList[mid] > key:
            end = mid
        elif nbList[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
 
 
nbList = input('Please enter the sorted list of numbers: ')
nbList = nbList.split()
nbList = [int(x) for x in nbList]
key = int(input('Please enter the number to search for: '))
 
index = binarySearch(nbList, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
