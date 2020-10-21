
# PythonLearning
https://stackoverflow.com/questions/58888088/python-subprocess-run-not-able-to-handle-large-argument-string

## TOUGH NUT

- [Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U)

## PIP - Python package manager

<details>
  <summary> PIP - Python Package Manager </summary>

- [Video](https://www.youtube.com/watch?v=U2ZN104hIcc)
- helps to install/uninstall packages
- helps creating virtual env as well
- `pip` - commands and help available with pip command
- `pip search <package>` - gives name/description of all matching packages
- `pip install <package>` - identifies reqs > resolve dependancies > build wheels > installs package
- `pip uninstall <package>`
- `pip list` - returns the list/version of packages in the current environment.
- `pip list -o` or `pip list --outdated` - gives the list of outdated packages
- `pip list -u` or `pip list -uptodate` - gives the list of up-to-date packages
- `pip freeze > requirements.txt` - writes the list/versions of packages
- `pip install -r requirements.txt` - installs the list/version of packages as specified in file reqirements.txt. Used to recreate virtual envs
 </details>

<details>
  <summary> Virtual Environments </summary>

- All the modules that we install are stored globally (use `site module` to list them)
- The main purpose of virtual environments is to **create an isolated environment** for projects
- By default, this will not include any of your existing site packages
- virtualenv is a module which needs to be installed for creation of new virtual environments
- ```virtualenv envname```
- How to create virtualenv_new from virtualenv_existing
  - goto virtualenv_existing
  - ```pip freeze --local > req.txt``` - exports the list of modules to a file
  - goto virtualenv_new
  - ```pip install -r req.txt``` - installs the list of module

```python
> import site
> site.getsitepackages()
[
  '/System/Library/Frameworks/Python.framework/Versions/3.5/Extras/lib/python',
  '/Library/Python/3.5/site-packages'
]
```

```python
pip install virtualenv # we need to install the module virtualenv
$ mkdir python-virtual-environments # create a new directory for virtual env
$ cd python-virtual-environments # cd into the virtual env dir
$ virtualenv env # create the virtual env
$ source env/bin/activate # activate the virtual env
(env) $  # now we see (env) - we are now in the virtual env
(env) $ deactivate # deactivates/exits from the virtual env
```

</details>

<details>
  <summary>Errors & Exceptions</summary>

  ```python

'''
BUILT-IN EXCEPTIONS
- In Python, all exceptions must be instances of a call that device from - BaseException
- In a try statement with an except clause that mentions a particular class,
  that clause also handles any exception classes derived from that class
- User code can raise built-in exceptions
- Build-in exception classes can be subclassed to define new exceptions
- Programmers are encourangeD to define new exceptions from Exception class or one of it subclasses
  rather than from BaseException class - refer User-defined Exceptions

- When raising/re-raisning an exception,
    - __context__ is automatially set to the last exception caught
    - if the new exception is not handled,
      the traceback that is eventually displayed will inlude originating exception and final exception

EXCEPTION HEIRARCHY
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning


    Exception       - Base class for all exceptions
    StopIteration   - Raised when the next() method of an iterator does not point to any object
    SystemExit      - Raised by sys.exit() function
    StandardError   - Base class for all built-in exceptions except StopeIteration and SystemExit
    LookupError            - Base class for all lookup errors
        IndexError         - index not found in a sequemce
        KeyError           - key not found in a dictionary
    ArithmeticError        - Base class for all errors that occur numeric calculation
        OverflowError      - Raised when a calculation exceeds maximum limit for a numeric type
        ZeroDivisionError  - Raised when division or module by 0 takes place
        FloatingPointError - Raised when a floating point calculation fails
    EnvironmentError       - Base class for all exceptions that occur outside the python env
    AssertionError         - Raised when assert statement fails
    EOFError               - Raised when there is no input from raw_input() or input() and the end of file is reached
    ImportError            - Raised when an import statement fails
    KeyboardInterrupt      - Raised when the user interrupts the execution - usually by pressing CTRL+C
    UnboundLocalError      - Raised when trying to access a local variable in a fucntion or method but no value has been assigned
    IOError                - Raised when an input/ouput operation fails, such as the print statement or open() on a file
    IOError                - Raised for operating system-related errors
    SyntaxError            - error in python syntax
    SystemError            - Raised when the interpreter finds an internal problem, BUT when this error is encountered, the interpreter doesnot exit
    TypeError              - Raised when an operation/function is attempted that is invalid for the specified data type
    ValueError             - Raised when the built-in functions for a data type has valid type of args, but the args have invalid values specified
    RuntimeError           - Raised when the generated error doesnt fall into any category
        NonImplementedError- Raised when an abstract method that needs to be implemented in an inherited class in not actually implemented
- use 'raise' to throw an exception if a condition occurs
- The statement can be complemented with a custom exception
'''
x = 10
y = 0
if x > 5:
    # manually raising a built in exception
    raise ValueException('{} is greater than 5'.format(x))

# Traceback (most recent call last):
#   File "<input>", line 4, in <module>
# Exception: 10 is greater than 5


###################################################################################################
'''
THE AssertionError EXCEPTION
- Instead of waiting for a program to creash midway, you can start by "making a assertion" in Python.
  Details on assert stamement towards end section
- We assert that a condition is met
    - If condition = True, then we are good
    - If condition = False, throw an AssertionError exception
'''
import sys
assert('Linux' in sys.platform), 'The code is designed for Linux platforms only'
# Lets run this in windows platform
# Traceback (most recent call last):
#  File "<input>", line 2, in <module>
# AssertionError: This code runs on Linux only.


###################################################################################################
'''
TRY-EXCEPT-ELSE-FINALLY BLOCKS
- raise allows you to throw an exception at any time.
- assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
- In the try clause, all statements are executed until an exception is encountered.
- except is used to catch and handle the exception(s) that are encountered in the try clause.
- else lets you code sections that should run only when no exceptions are encountered in the try clause.
- finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.
try:
   Run this code
except:
    Execute this code when there is an exception
else:
    No exceptions? Run this code
finally:
    always run this code
'''
try:
    assert( 100 in range(10))
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as assertion_err:
    print(assertion_err)
except (IOError, ValueError) as e: # Single except for mulitple exceptions
    print(e)
except Exception as e:
    print(e)
else:
    print('This is executed if no exceptions are thrown from try block')
finally:
    print('This is always executed')


###################################################################################################
'''
CUSTOM EXCEPTIONS - EXCEPTION CLASS - revisit
- you may need to write custom exceptions with custom messages
- we can do so by creating a NEW CLASS - which will be derived from the pre-defined Exception class
'''
class CustomError(Exception):
    def __init__ (self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

try:
    if(2>1):
        raise CustomError('Custom error message')
except CustomError as ce:
    print(ce.data)




# Example2
# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")


###################################################################################################
'''
ASSERT STATEMENTS
- AssertionError Exception
- assert statementis a debugging aid that tests a condition.
- It is not a mechanism to handle run-time error
    - they are not intended for expected error conditions like ' file not found'
- It aids developers to find root cause of a bug quickly
- If the condition is TRUE,
    - It does nothing and your program just continues to execute
- If the condition is FALSE,
    - it raises an AssertionError exception with an optional error message
    - example below

- CAVEAT#1
    - Asserts can be trurned off globally in the python interpreter
        - with the -0 and -00 command line switches as well as with
        - PYTHONOPTIMIZE environment variable in CPython
'''
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

# Lets run this in windows platform
# Traceback (most recent call last):
#  File "<input>", line 2, in <module>
# AssertionError: This code runs on Linux only.

###################################################################################################



  ```

</details>

<details>
  <summary>Variables scope</summary>

- Scope heirarchy - **LEGB** - Local, Enclosing, Global, BuiltIns

```python

x = 'global x'

def outer():
    x = 'outer x'
    def inner():
        # global x; print(x) # -> global x
        nonlocal x; print(x) # outer x
        x = 'inner x'; print(x) # inner x
    print(x) # -> outer x
    inner()

print(x) # -> global x
outer()
print(x) # -> global x

```

</details>

## DataStructures


- [Python Tutorial: Sets - Set Methods and Operations to Solve Common Problems](https://www.youtube.com/watch?v=r3R3h5ly_8g)
- [Corey:  Lists, Tuples, and Sets](https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4)
- [Corey: Sorting Lists, Tuples, and Objects](https://www.youtube.com/watch?v=D3JvDWO-BY4)
- [Corey: Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5)

<details>
    <summary>Lists, Sets</summary>


```python

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


```

</details>

<details>
    <summary>Dictionaries</summary>

```python
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


```

</details>


<details>
  <summary> Collections Module - COUNTER/DEFAULT DICT/ORDERED DICT/DEQUE/CHAIN MAP/NAMED TUPLE </summary>

  ```python
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


  ```

</details>

## Loops

<details>
  <summary>Enumerate</summary>
- Built in function
- Adds a counter to an iterable
- Returns a tuple like so (counter, value)

```python
dummy = ['Once', 'upon', 'a', 'time']
enum_obj = enumerate(dummy)
print(type(enum_obj)) #<class 'enumerate'>
for index, value in enumerate(dummy):
    print(f"{index}:{value}")

```
</details>

## Functions

<details>
  <summary> Functions > *args and **kwargs </summary>

  - [Corey: *args and **kwargs In Python](https://youtu.be/9Os0o3wzS_I?t=631)

```python
    '''
*args, **kwargs allow us to accept an arbitrary number of arguments

'''

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Maths', 'Art', name="Jon", age=45 )
# ('Maths', 'Art')
# {'name': 'Jon', 'age': 45}
# SO, we see that
# - args is a tuple with all positional arguments
# - kwargs is a dictionary with all keyword value


# * and ** have different meaning when used while invoking functions 
courses = ['Maths', 'Art']
info = {'name':'Jon', 'age':45}
student_info(*courses, **info)
# ('Maths', 'Art')
# {'name': 'Jon', 'age': 45}
# So, we see that
# - *courses actually UNPACKS the list
# - **info also UNPACKS the dict
# So, essentially the call becomes student_info('Maths', 'Art', name='Jon', age='45')

```

</details>

<details>
  <summary> Functions - Lambda functions </summary>

- [video](https://www.youtube.com/watch?v=25ovCm9jKfA)
- <details>
  <summary>Code</summary>

  ```python
    #1 - Basic example
    sum = lambda x,y: x+y
    print(sum)       #<function <lambda> at 0x000001ADB20D03A8>
    print(type(sum)) #<class 'function'>
    print(sum(2,3))  #5

    #2 Sort names alphabetically using lambda functions
    names = ['Soumya','Rohan','Vani']
    # we will use sort method
    #   sort(*, key=None, reverse=False) method of builtins.list instance
    names.sort(key = lambda names:names)
    print(names)

    #3 Sort names using the last names
    full_names = ['Soumya Ranjan Das','Rohan Ram', 'Vani Mummiji']
    full_names.sort(key = lambda name:name.split()[-1])
    print(full_names)

    #4 Using lambda functions to generate functions - OUCH
    def build_quadratic_functions(a, b, c):
        return lambda x: a*x*x + b*x + c

    f = build_quadratic_functions(2, 3, -5)
    print(f(3))
    print(f(13))
  ```
</details>
</details>

<details>
  <summary>Functions > First Class Functions</summary>

- [Programming Terms: First-Class Functions](https://www.youtube.com/watch?v=kr0mpwqttM0)
- A programming language is said to have First-class functions WHEN FUNCTIONS ARE TREATED LIKE ANY OTHER VARIABLE.
- In such a language, a function
  <details>
  <summary>can be assigned as a value to a variable</summary>

  ```python
    def show():
        print("Hello World")

    func_var = show
    print(type(show))     #<class 'function'>
    print(type(func_var)) #<class 'function'>
    print(show)     #<function show at 0x000001C48B7203A8>
    print(func_var) #<function show at 0x000001C48B7203A8>
    show()     #Hello World
    func_var() #Hello World

  ```

  </details>

  <details>
  <summary>can be passed as an argument to other functions</summary>

  ```python
    def square(x):
        return x*x

    def my_map(func, args_list):
        result = []
        for x in args_list:
            result.append(square(x))
        return result

    print(square(3)) # normal function invocation
    print(my_map(square, [1,2,3,4,5])) # func as argument

  ```
  </details>

  <details>
  <summary>can be returned by another function</summary>

  ```python
    def logger(msg):

        def local_logger():
            print('Log:', msg)

        return local_logger

    log_hi = logger('Hi')
    print(log_hi)
    log_hi()

    log_hello = logger('Hello')
    print(log_hello)
    log_hello()

    # Example#2

    def html_tag(tag):

        def wrap_text(msg):
            print('<{0}>{1}</{0}>'.format(tag, msg))

        return wrap_text

    print_h1 = html_tag('h1')
    print(print_h1)
    print(print_h1('wonderful'))

  ```

  </details>
</details>



<details>
  <summary>Functions > First Class Functions > Closures </summary>

- [Programming Terms: Closures - How to Use Them and Why They Are Useful](https://www.youtube.com/watch?v=swU3c34d2NQ)
- Closure closes in the free variables aka variables from the outer function scope
  <details>
  <summary>FirstClassFunctions_Closures.py</summary>

  ```python
    def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

    hi_func = outer_func('hi')
    hello_func = outer_func('hello')

    print(hi_func)    #<function outer_func.<locals>.inner_func at 0x000002346827B3A8>
    print(hello_func) #<function outer_func.<locals>.inner_func at 0x0000024E99B9BC18>

    print(hi_func.__name__)    #inner_func
    print(hello_func.__name__) #inner_func
    hi_func()    #hi
    hello_func() #hello


  ```

  </details>
</details>

<details>
  <summary> Functions > First Class Functions > Decorators </summary>

- [Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions](https://www.youtube.com/watch?v=FsAPt_9Bf3U)
- `@decorator_function`
- Examples:
    `@functools.lru_cache`

  <details>
  <summary>FirstClassFunctions_Decorators.py</summary>

  ```python
    def decorator_function(original_func):

    def wrapper_function():
        print ("wrapper function executed this before original function")
        return original_func()

    return wrapper_function

    # def display():
    #     print("Hello")
    # decorated_display = decorator_function(display)
    # decorated_display()

    # the above is the equivalent of the below code snippet - more pythonic way of decorator things
    @decorator_function
    def display():
        print("Hello")
    display()

  ```

  </details>
</details>

<details>
    <summary> Functions > map/filter/reduce</summary>

```python

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
print(list(map(cube,   [2,3,4,5,6] )))
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

```

</details>

<details>
    <summary> Function caching / MEMOIzation </summary>

- [Correy: Memoization](https://www.youtube.com/watch?v=a7EjmdQzPqY)

```python

'''
Memoization is an optimization technique used primarily
to speed up computer programs by storing the results expensive function calls
and returning the cached results when the same inputs occur again


Memoization = Function caching
'''

import time
ef_cache = {}
def expensive_function(num):
    if(num in ef_cache):
        print(f"Fetched from cache..{num}")
        return ef_cache[num]

    print(f"Computing {num}..")
    time.sleep(num)
    result = num * num
    ef_cache[num] = result
    return result

expensive_function(2) # Computing 2..
expensive_function(3) # Computing 3..
expensive_function(2) # Fetched from cache..2
expensive_function(4) # Computing 4..

```

</details>



<details>
  <summary>Date Time</summary>


### Aware and Naive Objects

Date and time objects may be categorized as **aware** or **naive**

#### aware (contains timezone information)

- An aware object represents a specific moment in time that is not open to interpretation

#### naive (doesn't contain timezone information)

- [Video: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones - ADVANCED](https://www.youtube.com/watch?v=eirjjyP2qcQ)
- A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects.
- Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.

- To add timezone info, use an optional time zone information attribute, **tzinfo**
- These tzinfo objects capture information about
  - the offset from UTC time,
  - the time zone name, and
  - whether daylight saving time is in effect.

<details>
  <summary>Code</summary>

  ```python
    import datetime
    import pytz
    '''
    datetime.date - Y/M/D    - rarely used alone
    datetime.time - H/m/s/ms - rarely used alone
    datetime.datetime Y/M/D H/m/s/ms - most commonly used
    '''

    #Date manipulation
    today = datetime.date.today()
    birth_day = datetime.date(1985, 3, 24)
    print(type(birth_day))   #<class 'datetime.date'>
    print(birth_day)         #1985-03-24
    print(today)             #2019-10-29
    print(today - birth_day) #12637 days, 0:00:00

    #Time manipulation
    t = datetime.time(8, 8, 8)
    print(type(t)) #<class 'datetime.time'>
    print(t)       #08:08:08
    print(t.hour, t.minute, t.second, t.microsecond) # 8 8 8 0

    #DateTime manipulation
    dt = datetime.datetime(1985, 3, 24, 8, 9, 10)
    tdelta = datetime.timedelta(days=3, hours=4, minutes=5, seconds=12)
    print(type(dt))     #<class 'datetime.datetime'>
    print(type(tdelta)) #<class 'datetime.timedelta'>
    print(dt)           #1985-03-24 08:09:10
    print(dt+tdelta)    #1985-03-27 12:14:22

    #Important constructs of datetime
    dt_today = datetime.datetime.today()  # returns current local datetime with timezone=None
    dt_now = datetime.datetime.now()      # gives the option to pass in a timezone.
                                          # If nothing is provided, timezone=none - behaves same as above
    dt_utcnow = datetime.datetime.utcnow()# Even though the method contains UTC in the name,
                                          # it just gives the current time of UTC. However, TZINFO is still set to none

    print(dt_today) #2019-10-29 01:16:35.186688
    print(dt_now)   #2019-10-29 01:16:35.186688
    print(dt_utcnow)#2019-10-28 19:46:35.186688

    #Handling timezones - pytz - Timezone aware objects
    dt = datetime.datetime(1985, 3, 24, 8, 9 ,10, tzinfo=pytz.UTC)
    print(type(dt)) #<class 'datetime.datetime'>
    print(dt)       #1985-03-24 08:09:10+00:00
                    # 00:00 is the UTC offset

  ```

</details>
</details>

<details>
  <summary> Import libraries </summary>

- Importing custom libraries

- Whenever we import a module, the module actually gets executed
- In the example below, when the interpreter see `import my_module`, it actually **executes** it
- This explains why 'Hello World from my_module' was printed just by importing the module

```python

  # my_module.py
  print ("Hello World from my_module")
  test = "Imported from my_module"

  def dummy_function():
    return "Tiu from dummy_function"

  # import.py
  import my_module
  print("wow")
  '''
  output
  Hello World from my_module
  wow
  '''

```

- Different ways to import libraries

```python

    import my_module       # imports all variable and methods
    print(my_module.test)  # we need to access variables/methods using module name
    print(my_module.dummy_function())

    import my_module as mm # alias
    print(mm.dummy_function())

    from my_module import dummy_function
    print(dummy_function()) # no need to write my_module.dummy_function()
    # cons - we don't have access my_module.test -> we need specify each element separately

    from my_module import dummy_function, test
    print(dummy_function())
    print(test)

    from my_module import * # big NO NO
    print(dummy_function())
    print(test)
    # Though we have access to all variables/methods directly, it is difficult to debug
    # as we don't know test/dummy_function came from which module


```

- Where does the interpreter look for the libraries

```python
    import sys
    print(sys.path)

    '''
    [
    'f:\\GitHubRepo\\PythonBasics',  - first it looks for the current directory
    'C:\\ProgramData\\Anaconda3\\python37.zip',
    'C:\\ProgramData\\Anaconda3\\DLLs',
    'C:\\ProgramData\\Anaconda3\\lib',
    'C:\\ProgramData\\Anaconda3',
    'C:\\ProgramData\\Anaconda3\\lib\\site-packages', - lastly, it looks for 3rd party libraries
    'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32',
    'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\win32\\lib',
    'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\Pythonwin',
    ]'''
```

- Add custom path to sys.path
- We need to add custom path so that interpreter searches in those dirs as well
  - sys.append('F:/Github/libraries')
  - using **PYTHONPATH** environment variable(in unix)
    - edit `bash_profile`
    - add `export PYTHON_PATH='/path/to/libraries/dir'`
  - using **PYTHONPATH** environment variable(in windows)
    - computer > properties > addtional .. > environment variables > add > PYTHONPATH / /path/to/libraries/dir

</details>

<details>
  <summary> if __name__ == 'main' </summary>

- [SO](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
- [Corey](https://www.youtube.com/watch?v=sugvnHA7ElY)
- `__main__` is the name of the scope in which top-level code executes.
- A module's `__name__` is set equal to `__main__` when read from standard input, a script, or from an interactive prompt.
- A module can discover whether or not it is running in the main scope by checking its own `__name__`,
  which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:

```python
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

- For a package, the same effect can be achieved by including a `__main__.py` module,
  the contents of which will be executed when the module is run with -m.

</details>

<details>
  <summary> Regex </summary>

  ```python

  '''
Module: re
- The re module raises exception re.error
- returns match object on success, None on failure
'''


'''
THE match FUNCTION
- re.match( pattern, string, flags = 0)
  - pattern: The regex to be matched
  - string : This is the string which would be searched
  - flags  : we can specify different flags using bitwise OR |
     - re.I: case insensitive matching
     - re.L: Interprets words according to the current locale.
             This interpretation affects the alphabetic group (\w and \W),
             as well as word boundary behavior(\b and \B).
     - re.M: Makes $ match the end of a line (not just the end of the string) and
             makes ^ match the start of any line (not just the start of the string).
     - re.S: Makes a period (dot) match any character, including a newline.
     - re.U: Interprets letters according to the Unicode character set.
             This flag affects the behavior of \w, \W, \b, \B.
     - re.X: Permits "cuter" regular expression syntax.
             It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
- The re.match function returns match object on success, None on failure
- Functions of match object
  - group(num=0)
    - This method returns entire match (or specific subgroup number)
  - groups()
    - This method returns all matching subgroups in a tuple(empty if there weren't any)
'''

import re

match = re.match(
    r'(.*) are (.*) than (.*)',
    'cats are smarter than dogs',
    re.M|re.I
)
print(match) # <re.Match object; span=(0, 26), match='cats are smarter than dogs'>
if (match):
    print('Match successfull')
    print(match.groups())  # ('cats', 'smarter', 'dogs')
    print(match.group())   # cats are smarter than dogs
    print(match.group(0))  # cats are smarter than dogs
    print(match.group(1))  # cats
else:
    print('Match unsuccessfull')




#####################################################################################################
'''
PERFORMING MATCHES
match()    : Determine if the RE matches at the beginnnig of the string
             Returns MATCH OBJECT instance if successfull
             Returns NONE if no matches
search()   : Scan through the string, looking for any location where this RE matches
             Returns MATCH OBJECT instance if successfull
             Returns NONE if no matches
findall()  : Find all substrings where the RE matches, and
             returns them as a LIST
finditer() : Find all substrings where the RE matches, and
             returns them as an iterator
'''
import re
p = re.compile('ab*')
q = re.compile('ab*', re.IGNORECASE)
p.match("") #None
p.match("Tempo") # <re.Match object; span=(0,3), match='Tempo'>

#####################################################################################################
'''
QUERYING MATCH OBJECTS
group() : Return the string matched by RE
start() : return the starting position of the match
end()   : return the ending position of the match
span()  : return a tuple containig the (start, end) positions of the match
'''
m = p.match('tempo')
m.group() # 'tempo'
m.start(), m.end() # (0, 5)
m.span() # (0, 5)

# since match() method only checks if the Re matches at the start of a string, m.start() will always be 0
n = p.search('tempo')
n.span() # (4, 11)

  ```

</details>


## todo

- getattr
- map
- context managers

<!-- # A collapsible section with code
<details>
  <summary>Click to expand!</summary>

  ```javascript
    function whatIsLove() {
      console.log('Baby Don't hurt me. Don't hurt me');
      return 'No more';
    }
  ```
</details> -->

### STRINGS
- [Corey: Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2)
<details>
    <summary>Strings</summary>

```python
single_quoted_string = 'Hello'
double_quoted_string = "Hello"
multi_line_string    = """Hello 
How are you"""
multi_line_string = "Hello\n\
How are you\n\
Howdy!"

# Common string methods
msg = "Hello World"
len(msg) # 11
msg = msg.lower()
msg = msg.upper()
msg.count("Hello") # 1
msg.find("World")  # 6 - returns the index of the first match. Else -1
msg = msg.replace("World", "Universe")

msg[0]  # H
msg[10] # d

# CONCATENATION/STRING FORMATTING #
a = 'Hello' + ' ' + 'World'
a = 'Hello ' 'World'         # two string literals next to each other are automatically concatenated
# a = 'Hello'.strip() 'World' # Invalid

person = {'name': 'Jenn', 'age': 23}
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

# old school 
sentence = 'My name is %s and I am %s years old' %(person['name'], person['age'])
# str.format
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.' # Using + 
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])      # Using empty {}
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])    # Using numbered {} 
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)                # reuse same arg
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)                      # Accessing class elements using . notation
sentence = 'My name is {name} and I am {age} years old.'.format(**person)                    # Using dict unpacking **
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')       # Using keywords
sentence = f'My name is {person["name"]} and I am {person["age"]} years old.'                # f strings 3.6+
pi = 3.14159265
sentence = 'Pi is equal to {}'.format(pi)     # 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi) # 3.14
sentence = '1 MB is equal to {} bytes'.format(1000**2)      #1000000
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)    #1,000,000
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2) #1,000,000.00

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45); print(my_date) # March 01, 2016
# Note the use of index number 0 as we are using the same input param twice
sentence = '{0:%B %d, %Y} fell on a {0:%A} '.format(my_date) #September 24, 2016 fell on a Saturday

# STRING FUNCTIONS - checks ######################
'word'.startswith('a')
'word'.endswith('a')
'word'.replace('abc', 'pqr')
'word'.isalnum() # Checks if ALL chars are alphanumeric
'word'.isalpha() # Checks if ALL chars are alphabets
'word'.isdigit() # Checks if ALL chars are digits

#istitle() # Checks if string contains title words
'Hello'.istitle()       #True
'hello'.istitle()       #False
'H'.istitle()           #True
'h'.istitle()           #True
'Hello World'.istitle() #True
'Hello world'.istitle() #False

# isupper()/islower() # Checks if ALL the chars are upper/lower case
'word'.isupper() # False
'Word'.isupper() # False
'WORD'.isupper() #True
'    '.isupper() # False
'   W'.isupper() #True <-- note
'W'.isupper()    #True

#isspace() # Checks if ALL the chars are spaces

# STRING FUNCTIONS - transform
word.upper()
word.lower()
word.capitalize()
word.swapcase()

# strip(): TRIMS WHITESPACES
'  word  '.strip()  # 'word'
'  word  '.lstrip() # 'word  '
'  word  '.rstrip() # '  word'
'        '.strip() # '' - same result for lstrip n rstrip

# replace()
'Hello World'.replace('World', 'Universe') # 'Hello Universe'

# split(): 
# Returns a list. Default separator: space
'Hello World'.split()    # ['Hello', 'World']
'Hello,World'.split()    # ['Hello World']
'Hello,World'.split(',') # ['Hello', 'World']

# join()
# `string_name.join(iterable)`
# The join() method takes `iterable` – objects capable of returning its **members one at a time**.
# Ex: List, Tuple, String, Dictionary and Set
"-".join #<built-in method join of str object at 0x00000192F81D37F0>
"-".join(['a','b','c']) #'a-b-c'
"-".join(('a','b','c')) #'a-b-c'
"-".join({'a','b','c'}) #'b-c-a'
"-".join({'a':'x','b':'y','c':'z'}) #'a-b-c'
':'.join('  Hello World  ') # ' : :H:e:l:l:o: :W:o:r:l:d: : '

# reversed
print(reversed("abcde")) # <reversed object at 0x0000000002BDDCC0>
print(''.join(reversed("abcde"))) # edcba


'''
# STRING MODULES
# import textwrap
# The textwrap module provides two convenient functions: wrap() and fill().

# textwrap.wrap() 
# The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
# It returns a list of output lines.
import textwrap
string = "This is a very very very very very long string."
print textwrap.wrap(string,8)
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 

# textwrap.fill() 
#The fill() function wraps a single paragraph in text and 
#It returns a single string containing the wrapped paragraph.
import textwrap
string = "This is a very very very very very long string."
print textwrap.fill(string,8)
# This is
# a very
# very
# very
# very
# very
# long
# string.
'''

```

</details>
<details>
    <summary>String - QnA</summary>

```python
# How do you reverse a given string in place? 
str = 'How do you reverse a given string in place?'
str = str[::-1]
print(str)

#2: Reversed
str = 'How do you reverse a given string in place?'
str = "".join(list(reversed(str)))
print(str)

#3: Using while loop
str = 'How do you reverse a given string in place?'
temp_str = ''
index = len(str) - 1
while(index >= 0):
    temp_str = temp_str + str[index]
    index -= 1
print(temp_str)

# Reverse the order of words in a string
str = 'Reverse the order of words in a string'
print(" ".join(str.split()[::-1]))

# Reverse internal content of each word
string = 'Reverse internal content of each word'
print(" ".join(list(map(lambda x: x[::-1], string.split(" ")))))

string = 'REVERSE internal content of every second word present in the given string'
rev = []
for index, word in enumerate(string.split(" ")):
    if (index%2 == 0):
        pass
    else: 
        rev.append(word[::-1])
print(" ".join(rev))


# Program for the requirement,input: a4z2b3c2 and expected output: aaaabbbcczz(sorted)
a = "a4z2b3c2"
res = []
for pos in range(0, len(a), 2):
    char = a[pos:pos+2][0]
    rep  = a[pos:pos+2][1]
    res.append(char * int(rep))
print("".join(list(sorted(res))))

#Program for the requirement,input: aaaabbbccz and expected output: 4a3b2c1z
import collections
results = collections.Counter('aaaabbbccz')
for key,value in results.items():
    print("{}{}".format(value,key), end="")

# Check if two stings are anagrams
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
a = "abcde"
b = "edcabbbb"

if (("".join(sorted(a))) == ("".join(sorted(b)))):
    print("\n{} & {} are anagrams".format(a, b))
else :
    print("\n{} & {} are NOT anagrams".format(a, b))
```
</details>

## Interview

<details>
    <summary> Merge two dictionaries </summary>

```python

# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
z
{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
z = dict(x, **y)
z
{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8

```

</details>
<details>
    <summary> Sort dict based on value</summary>

```python
xs = {'a':4, 'b':3, 'c':2, 'd':1}
sorted(xs.items(), key=lambda x:x[1])
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

```

</details>

- interview qs - eves drop
- can we add nay type of object to a stack
- collection queue
- set s; s.add(tuple)
- decorator - time to execute the function
- Context managers
- Memory management
- Reference counting
- Operator overloading
- How to join two dataframes in pandas based on date column
- projects u worked on in python
- issues faced while migrating from 2.x to 3.x
- can we have any obj like likst/tuple as key of a dict
- check for a key in a dict
- write a generator function to behanve like a range function.. like.. print numbers from 0 to 9
- decorator to print the time the function took to execute
- code analysis package - pychecker - how do u debug ur code

## Classes
<details>
    <summary> Creating a class </summary>

```python

class Student:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullname(self):
        print ("{} {}".format(self.first, self.last))

harry = Student("Harry", "Porter", 99)
print(harry)       #<__main__.Student object at 0x000001E1B990EC88>
print(harry.first) #Harry
harry.fullname()        # Calling method using object
Student.fullname(harry) # Calling method using class name

```

</details>

<details>
    <summary> Class Variable </summary>

- [OOP: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2)

```python

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first, self.last)

    def fullname(self):
        print ("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay *= self.raise_amount
        # self.pay *= Employee.raise_amount


emp_1 = Employee("Harry", "Porter", 50000)
emp_2 = Employee("Corey", "Schafer", 60000)

print(Employee.__dict__)
    #{
    #   'raise_amount': 1.04,
    #   'fullname': <function Employee.fullname at 0x0000024ECD082F78>,
    #   'apply_raise': <function Employee.apply_raise at 0x0000024ECD082EE8>,
    #
    #   '__init__': <function Employee.__init__ at 0x0000024ECD08A1F8>,
    #   '__module__': '__main__',
    #   '__dict__': <attribute '__dict__' of 'Employee' objects>,
    #   '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
    #   '__doc__': None
    # }
    #
    # Note: raise_amount exists in the class namespace
print(emp_1.__dict__)
    # {'first': 'Harry', 'last': 'Porter', 'pay': 50000, 'email': 'Harry.Porter@company.com'}
    # raise_amount is not present in the namespace of emp_1.
    # So,it falls back to raise_amount of class namespace
emp_1.raise_amount = 1.05
    # This will only impact the emp_1.
    # raise_amount will get added to namespace of emp_1
print(emp_1.__dict__)
    # {'first': 'Harry', 'last': 'Porter', 'pay': 50000, 'email': 'Harry.Porter@company.com', 'raise_amount': 1.05}
emp_1.raise_amount
    # Since the emp_1 has a local attribute of raise_amount -  it will be set to 0.5
    # All other objects of Employee will still refer to raise_amount of class namespace which = 0.4

Employee.raise_amount = 0.9
print(Employee.__dict__) # raise_amount = 0.9
print(emp_1.__dict__)    # raise_amount = 0.5 - refers to the raise_amount set locally to the object
print(emp_2.__dict__)    # No raise_amount in the dict of emp_2. It will refer to raise_amount of class instance

```

</details>

<details>
    <summary> @classmethods and @staticmethods </summary>

[Schafer: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3)

```python


class Employee:

    raise_amount = 1.04
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first, self.last)
        Employee.no_of_emps += 1

    def fullname(self):
        print ("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay *= self.raise_amount

    # @classmethod
    # - @classmethod is a DECORATOR
    # - It tells that the following def is a class method(not a regular or static method)
    # - The first argument to classmethod is always the class instance itself
    # - This is similar to regular methods where the first arg is self (the object itself)
    # - By conventions, we name the first argument of a classmethod as cls - which denotes the class instance

    @classmethod
    def string_to_instance(cls, string):
        # This is an example where classmethod is used as ALTERNATE Constructor
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @classmethod
    def set_raise_amount(cls, amount):
        # This is an example of classmethod where it simply behaves on an attribute in class instance
        # As obvious, this will change the value in the class namespace only
        # It will have no effect on the object namespace
        cls.raise_amount = amount

    # @staticmethod
    # - its a decorator which tells the following def is a static method(not a class method or regular method)
    # -    classmethod: first arg = class itself  = cls
    # - regular method: first arg = object itself = self
    # -  static method: no mandatory/default arguments - Its just like regular functions

    @staticmethod
    def is_working_day(day):
        if ( day.weekday()==5  or day.weekday()==6):
            return False
        return True

# Creating a new object via @classmethod
emp_3 = Employee.string_to_instance("Soumya-Das-20000")

# Changing the value of class attribute via @classmethod
print(Employee.__dict__) #'raise_amount': 1.04,
Employee.set_raise_amount(1.05)
print(Employee.__dict__) #'raise_amount': 1.05,

```

</details>

<details>
    <summary> Sub Classes </summary>

- `class childclass(parentclass)`
- `super`
- `super().__init__()`

```python
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emps(self):

        for emp in self.employees:
            print ("-->",emp.email)

dev1 = Developer("Test", "Developer1", 200, 'Perl')
dev2 = Developer("Test", "Developer2", 300, 'Python')

mgr1 = Manager("Poli","Bala",900, [dev1])
mgr1.add_emp(dev2)
print(mgr1.fullname())
mgr1.show_emps()

```

</details>

<details>
    <summary> Magic methods/ <strong>overloading</strong> methods & operators </summary>

- [Correy: Special methods](https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5)
- `__repr__`
- `__str__`
- `__add__`
- `__len__`

```python

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}-{}-{}".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first) + len(self.last)

emp1 = Employee("Soumya", "Ranjan", 100)
emp2 = Employee("Correy", "Schafer", 900)

print(emp1) #Soumya-Ranjan-100
print(emp2) #Correy-Schafer-900
print(emp1 + emp2) #1000
print(len(emp1))   #12

```

</details>

<details>
    <summary>public/protected/private - Name Mangling </summary>

```python
'''
Python has no concept of public/protected/private variables

PROTECTED
If we want to 'hint' that a variable is protected,
    Use leading underscore to the variable name
    Example: _age
    This is purely by convention - python does nothing to enforce anything

PRIVATE
If we want to 'hint' that a variable is private,
    Use two leading underscores to the variable name
    __example
    Python does 'NAME MANGLING' to provide some sense of security to private vars
    Python actually renames that to _classname__example
    This prevents accidental change to the private variable by other classes

'''

class Student:

    def __init__(self):
        self.name = 'whatever'
        self._age = 99
        self.__gender = 'A'

student1 = Student()
print(dir(student1)) # [name, _age, _Student__gender, ...]
print(student1.name) # whatever
print(student1._age) # 99
# print(student1.__gender)       # AttributeError: 'Student' object has no attribute '__gender'
print(student1._Student__gender) # A

```

</details>

<details>
    <summary> Diamond Problem - Problem with multiple inheritance </summary>

- [Harry-Diamond shape problem](https://www.youtube.com/watch?v=mEF_vVNTPUY&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=67)

```python
'''
    A
    /\
   B  C
    \/
    D

    - This is an issue which is caused due to multiple inheritance
    - Multiple inheritance causes many such issues
    - So, multiple inheritance is not supported in many languages
    - Instead we should use multilevel inheritance if required

    diamond problem:
    - now suppose A,B,C has a method demo()
    - Q. so, which demo() does D object gets ?
    - Python handles this by using the order
    - class D(B, C)
        - D will get demo() of B
    - class D(C, b)
        - D will get demo() of C
    - so, no issues for python
    - but this causes issues in other languages where the ordering has no role
      and the compiler gets confused as to which demo() should D get.

'''
class A:
    def demo(self):
        print("Demo of class A")

class B(A):
    def demo(self):
        print("Demo of class B")

class C(A):
    def demo(self):
        print("Demo of class C")

class D(B, C):
    pass

d = D()
print(dir(d))
print(d.demo())
```

</details>

## unfiled

<details>
    <summary> Iterators and Iterables </summary>

- [Correy:Iterators and Iterables - What Are They and How Do They Work?](https://www.youtube.com/watch?v=jTYiNjvnHZY)

```python

'''
- iterable IS NOT iterator
- Iterable is something which can be looped over
- Technically, anything which contains __iter__ method => ITERABLE => can be looped over
- LISTS
    - List is an iterable, not an iterator

- ITERATOR
    - an iterator mantains a STATE so that it knows where it is during an iteration
    - iterators get the nect value using __next__ method
    - lists doNOT have a __next__ method => so, lists are not iterators

'''

nums = [1, 2, 3]
for num in nums:
    print(num)

print(dir(nums))
    #__add__, __iter__ ...
    #Since list contains the __iter__ method, it is an ITERABLE

# print(next(nums))
    # TypeError: 'list' object is not an iterator
    # lists have __iter__ but don't have __next__ method, that is,
    # list has __iter__        => iterable
    # list don't have __next__ => not an iterator

i_nums = nums.__iter__() # same as i_nums = iter(nums)
print(i_nums)            # <list_iterator object at 0x000001F422974148>
print(dir(i_nums))       # __iter__','__next__','__lt__', '__ne__', '__new__'
    # Q. i_nums is an iterator. Then how come the iterator also contains __iter__ ?
    # A. All iterable are iterators
    #   if we run __iter__ on i_nums, it returns self

print(next(i_nums)) # 1
print(next(i_nums)) # 2
print(next(i_nums)) # 3
# print(next(i_nums)) # StopIteration Exception


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current



x = MyRange(1, 5) #<__main__.MyRange object at 0x000002CABF507D48>

print(x)
print(dir(x)) # __iter__, __next__, __class__ and others
for num in x:
    print (num)


# creating an iterator using generator
def my_range(start, end):
    current = start
    while(current < end):
        yield current
        current +=1

y = my_range(1,5)
for num in y:
    print(num)

```

</details>
