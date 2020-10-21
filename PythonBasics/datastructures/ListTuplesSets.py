########
# LIST #
########
# - Lists are MUTABLES
courses = ['Math', 'Physics', 'CompSci']
print(courses) # ['Math', 'Physics', 'CompSci']
print(type(courses)) # <class 'list'>
print(dir(courses))  # [..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(len(courses))  # 3
print(courses.count("Math")) # 1
print(courses.count("What")) # 0

# Append - inserts at the end. If we want to insert at particular loc, use .insert()
print(courses.append("Chem")) # None
print(courses) # ['Math', 'Physics', 'CompSci', 'Chem']
courses.append([1,2,3]) # List gets added a list 
print(courses) # ['Math', 'Physics', 'CompSci', 'Chem', [1, 2, 3]]
# Extend
courses.extend(['India', 'Pak', 'Nepal']) # List gets flattened out
print(courses) #['Math', 'Physics', 'CompSci', 'Chem', [1, 2, 3], 'India', 'Pak', 'Nepal']

print(courses.clear)
print(courses)

courses = []
print(courses) # []

# print(courses.remove('z')) # None
# print(courses.remove('whatever')) # ValueError Exception
print(courses) # ['y', 'x']

print(courses.reverse()) # None - same as courses.sort(reverse=True)
print(courses) # ['x', 'y']

print(courses.insert(0, 'w')) # None
print(courses.insert(len(courses), 'z')) # None 
print(courses) # ['w', 'x', 'y', 'z']

print(courses.pop(1)) # x - removes and returns the element as index=1
print(courses.pop())  # z - if no index is porvided, it index=last(default)

#########
# TUPLE #
#########
# Similar to lists but tuples are IMMUTABLES
#- which means we cant change the content of a tuple
#- so, we don't have methods like append, insert, extend etc

#######
# SET #
#######
courses = {'Math', 'Phy', 'Chem', 'Phy'} # note the curly braces    
print(courses) 
    # {'Chem', 'Math', 'Phy'} - As we see, the order is not retained
    # also the duplicate Phy is removed


#####################
# sort() vs sorted()#
#####################
# [1,3,2].sort() is a METHOD which works only on lists
# sorted(itertable) is a FUNCTION which works on any iterable
[1,4,5,2,3].sort() 
# (1,4,5,2,3).sort() # 'tuple' object has no attribute 'sort 
                     # sort() works only on lists

tup = (1,4,5,2,3)
s_tup = sorted(tup) 
print(s_tup) # [1,2,3,4,5] NOTE: Even if we use sorted() on tuple, sorted always returns a LIST


# sort the numbers in a list based on absolute value
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li) # [1, 2, 3, -4, -5, -6]

# sort a list of class objects
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "{} {}".format(self.name, self.age)

s1 = Student("abc", 10)
s2 = Student("pqr", 50)
s3 = Student("xyz", 30)

students = [s1, s2, s3]
s_students = sorted(students, key=lambda e:e.age)
print(s_students)
# using operator module
from operator import attrgetter
ss_students = sorted(students, key=attrgetter('age'))
print(ss_students)

#####################
# SET               #
#####################
s1 = set([1,2,3,1,2,3])
s2 = {1, 2, 3, 1, 2, 3}
print(s1)       # {1, 2, 3}
print(type(s1)) # <class 'set>
# print(dir(s1))  # ['intersection', 'union', 'difference', 'issubset', 'issuperset' ...]

# Creating an empty set
s3 = {}    # This will create an empty DICT
s4 = set() # This will create an empty SET
print(s4) #set()

# Adding elements - add & update
s5 = {1, 2, 3}
s5.add(4)
s5.update([5, 6, 7], [6, 7, 8], (8, 9, 10))

# DELETE ELEMENTS - REMOVE & DISCARD
# The only diff between remove & discard 
# - discard doesn't throw error if we try to delete an element which doesn't exist
# - remove will throw KeyError exception
s5.remove(9)  # Deletes the element 9
# s5.remove(99) # Keyerror as element doesn't exist.
s5.discard(8) # Deletes element 8
s5.discard(88)# NO ERROR - even if the element doesn't exist 

# INTERSECTION/DIFFERENCE/SYMMETRIC_DIFFERENCE
s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

s4 = s1.intersection(s2, s3) # {3}
s5 = s1.difference(s2)     # {1} - value in s1 which are not in s2
s6 = s1.difference(s2, s3) # {1} - value which is in s1 but not in s2 or s3
s7 = s1.symmetric_difference(s2) # {1, 4} - value which is in s1 and not in s2 and vice versa

# Practical usage
# If we are searching for an element
#   in a list - 0(n)
#   in a set  - 0(1) - faster
developers = ['a', 'b', 'c' , 'b', 'a']
if 'a' in set(developers):
    print('Found')

