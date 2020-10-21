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
