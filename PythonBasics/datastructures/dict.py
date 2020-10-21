student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name']) # John
# print(student['phone']) # KeyError

print(student.get('phone')) # None <-- note that there is no exception thrown
print(student.get('phone', 'Not Found')) # Not found

print(len(student))     # 3 - gives the number of keys
print(student.keys())   # dict_keys(['name', 'age', 'courses'])
print(student.values()) # dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items())  # dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# Iterating over items
for key, value in student.items():
    print (f"{key}-{value}")

# update - this method takes in a dict and ADDS/UPDATES the existing dict
student.update({'name':'Ranjan', 'Addr':'PNagar'})
print(student) # {'name': 'Ranjan', 'age': 25, 'courses': ['Math', 'CompSci'], 'Addr': 'PNagar'}

del student['Addr']      # It removes the element. But we cant capture the deleted element
age = student.pop('age') # It removes the element - and returns the value
print(student) # {'name': 'Ranjan', 'courses': ['Math', 'CompSci']}
