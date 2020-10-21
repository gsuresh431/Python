# MAP
# map(function, list/tuple/iterable)
#  - each element of the iterable is subjected to the function
#  - The value as returned from the function is stored in the map object
#  - The map() returns a map object - NOT A LIST
#  - we need to convert it into list

#1: Convert stringified numbers to integers
list1 = ['1', '2', '3']
map_obj = map(int, list1) # Converting string to integer for each element
print(map_obj)            # map() returns a map object - <map object at 0x000002E23019D148>
list1 = list(map_obj)     # Converting map to list
print(list1)              # [1, 2, 3]

#2 lambda with map
def square(x):
    return x*x
cube = lambda x: x*x*x
print(square(3))
print(list(map(square, [2,3,4,5,6] )))
print(list(map(cube, [2,3,4,5,6] )))
print(list(map(lambda x: 1/x , [1,2,3,4])))

#3 Convert to farenheit
a = [('Delhi', 30), ('Kolkata', 32), ('Mumbai', 28)]
c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
print(list(map(c_to_f, a)))

# FILTER
# filter(function, list/tuple/iterator)
# - returns filter object
# - we need to convert it into a list

# Find age greater than 18
age = [10, 25, 12, 23, 11]
print(list(filter(lambda data: data > 18, age)))

# Remove empty values from a list
print(list(filter(None, ['India', '', '', 'Nepal', '', 'Bhutan', '', 'Singapore'])))

# REDUCE
# - Confusing
# - Deprecated
# - no longer a built in function
# - moved to functools module 