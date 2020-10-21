'''
COLLECTIONS MODULE
- Collections in pythons are containers which are used to store collection of data - LIST, DICT, SET, TUPLE etc
- Several modules have been deveoped that provide additional data structures to store collection of data
- One such module is collections module - https://docs.python.org/3.7/library/collections.html

- This module implements specialized container datatypes providing alternatives to python's general purpose built-in containers - dict, list,set & tupule

namedtuple() - factory function for creating tuple subclasses with names fields
deque        - list-like container with fast appends and pops on either end
ChainMap     - dict-like class for creating a single view of multiple mappings
Counter      - dict subclass for counting hashtable objects
OrderedDict  - dict subclass that remembers the order entries were added
defaultdict  - dict subclass that calls a factory function to supply missing values
UserDict     - wrapper around dictionary objects for easier dict subclassing
UserList     - wrapper around list object for easier list subclassing
UserString   - wrapper around string objects for easier string subclassing
'''

############################################################################################################################
'''
COUNTER

- Counter is a subclass of dictionary object
- The Counter() fucntion in collections module takes an iterable or a mappings as the argument and returns a Dictionary.
- In this dictionary, a key is an element in the iterable or the mapping and value is the number of times that element exists in the iterable or the mapping

- Since cnt(below example) is an object of Counter, which is a subclass of dict
  - So, it has all the methods of dict class
  - Apart from that, Counter has 3 additional functions
  1. Elements
  2. Most_common([n])
  3.Subract([ iterable - or - mapping ])
'''

from collections import Counter
# Creating counter objects
cnt1 = Counter()                          # Simplest way to create counter object is the use Counter() without any args
cnt2 = Counter(['a','b','c','a','b','c']) # Passing an iterable(list) to create counter object
cnt3 = Counter({'a':11, 'b':22, 'c':33})  # Passing a dictionary to create counter object
                                          # However, count('key') simply gives the value
print(cnt1) # Counter()
print(cnt2) # Counter({'a':3, 'b':3, 'c':3})   <-- NOTE: list is converted to dict with the value of each key being the repeat count
print(cnt3) # Counter({'a':11, 'b':22, 'c':33) <-- no change if we direclty pass in a dict/mapping which creating counter object
  
print(cnt1['b']) # 0  - gives the repeatations of b
print(cnt2['b']) # 3  - gives repeatations of b
print(cnt3['b']) # 22 - gives value for key b

# The elements() fucntion
print(list(cnt2.elements())) #  [a,a,a,b,b,b,c,c,c]

# The most_common() function
# - returns a list, which is sorted based on the count of the elements
cnt4 = Counter(['a','b','c','d',  'a','b','c',  'a','b',  'a'])
print(cnt4.most_common())  # [ ('a', 4), ('b',3), ('c',2), ('d',1)]
print(cnt4.most_common(2)) # [ ('a', 4), ('b',3)]

# The Substract() function
# The subtract() takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count using that argument.
cnt5 = Counter({'a':10, 'b':20 })
deduct = {'a':5, 'b':5}
cnt5.substract(deduct) # Counter({'a':5, 'b':15})

############################################################################################################################

'''
DEFAULT DICT

The defaultdict
- Works exactly like python dictionary, except for it doesnot throw KeyError when you try to access a non-existent key
- Instead it initializes the key with the element of the data type that you  pass as an argument at the creation fo defaultdict
- The datatype is callled default_factory

- Usage
    - count of each name 
'''

from collections import defaultdict
nums = defaultdict(int)
print(nums)      # defaultdict(<class 'int'>, {})
nums['a'] = 10    
nums['b'] = 20
print(nums)      # defaultdict(<class 'int>, {'a':10, 'b':20})
print(nums['a']) # 10
print(nums['c']) # 0 <-- NOTE: the key 'c' doesnt exist. So, the key will now be created with value 0
print(nums)      # defaultdict(<class 'int'>, {'a':10, 'b':20, 'c':0})

############################################################################################################################

'''
ORDERED DICT

- It is a dictionary where keys maintain the order in which they are inserted
- that is - if we change the value of a key later, it will not change the position of the key
'''
from collection import OrderedDict
od = OrderedDict() # OrderedDict()
od['a'] = 1        # OrderedDict([('a', 1)])  
od['b'] = 2        # OrderedDict([('a', 1), ('b', 2)])
od['a'] = 4        # OrderedDict([('a', 4), ('b', 2)])

############################################################################################################################
'''
DEQUE
- deque is a list optimized for inserted and removing items from both ends
'''
from collections import deque
lst = ['a','b',' c'] # ['a', 'b', 'c']
deq = deque(lst)     # deque(['a', 'b', 'c'])
deq.append("d")      # deque(['a', 'b', 'c', 'd'])
deq.appendleft("z")  # deque(['z', 'a', 'b', 'c', 'd'])
deq.pop()            # deque(['z', 'a', 'b', 'c'])
deq.popleft()        # deque(['a', 'b', 'c'])
deq.clear()          # deque([])

############################################################################################################################
'''
CHAIN MAP ????????????
- chain many mappings
- Combines several dictionary or mappings. Returns a list of dictionaries
'''
from collections import ChainMap
dict1 = {'a':11, 'b':22}
dict2 = {'c':33, 'b':44}
dict3 = {'e':55, 'f':66}
chain_map = ChainMap(dict1, dict2) # ({'a':11, 'b':22}, {'c':33, 'd':44})
chain_map['b']             # 22
chain_map['b'] = 99        # ({'a':11, 'b':99}, {'c':33, 'd':44})
chain_map.new_child(dict3) # ({'e':55, 'f':66},{'a':11, 'b':22},{'c':33, 'd':44}) <-- the new dict is added at beginning

############################################################################################################################
'''
NAMED TUPLE ??
- namedtuple() returns a tuple with names for each position in the tuple
- One of the biggest problems with ordinary tuples is that you have to remember the index of each field of a tuple object - obviously difficult
- namedtuple was introduced to solve this problem
- 
'''
from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age') # <class '__main__.Student'>
s1 = Student('Soumya', 'Ranjan', 99)                 # Student(fname='Soumya', lname='Ranjan', age=99)  
s2 = Student._make('Mark', 'Thomas', 88)             # Student(fname='Mark',   lname='Thomas', age=88)  




