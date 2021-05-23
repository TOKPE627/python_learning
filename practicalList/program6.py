#WAP in python to implement linear search.	

def linearSearch(listElements, keyS):
    """Return index of key in listElements. Return -1 if key not present."""
    for i in range(len(listElements)):
        if listElements[i] == key:
            return i
    return -1
 
 
listElements = input('Please enter the list of numbers: ')
listElements = listElements.split()
listElements = [int(x) for x in listElements]
key = int(input('Please enter the number to search for: '))
 
index = linearSearch(listElements, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
