#WAP to create a dictionary with 5 elements and the field 
#of the dictionary is name, age of student.
#1)First Find the keys of the dictionary
#2)Find the values of the dictionary
#3)Find 3td item key-pair

students =	{
  1: {'name':'Kossi',  'age':'24'},
  2: {'name':'Saley',  'age':'14'},
  3: {'name':'Lamine', 'age':'29'},
  4: {'name':'Pratick','age':'24'},
  5: {'name':'Armel',  'age':'34'}
}

print("All students of the dictionary:")
for p_id, p_info in students.items():
    print("\nStudent ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
print()
print("Keys of the dictionary:\n")
print(students.keys())

print()
print("Values of the dictionary:\n")
print(students.values())

print()
print("Search of Third student of the dictionary:\n")
print(students[3])
