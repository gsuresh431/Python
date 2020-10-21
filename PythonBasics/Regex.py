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
 


