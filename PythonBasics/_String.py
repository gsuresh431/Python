'''
Corey: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2
'''

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