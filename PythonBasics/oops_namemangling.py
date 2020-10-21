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