"""Itertools

- counter - generates consecutive values
- zip 
    - returns a zip of tuples by combining together all the input iterables.
    - it stops at the shortest iterable
- zip_longest 
    - returns a zip of tuples by combining together all the input iterables.
    - however, it doesn't stop at the shortest iterable
    - it continues till the longest iterable
    - it fills the missing values with None(default) 

- cycle - 
    - cycles through a sequence of values indefinitely(default)
    - can be restricted by using times param 
- repeat - 
    - repeat the same digit indefinitely
    - can
"""
import itertools
    
# COUNTER - Used to generate consecutive values
# def count(start: _N=..., step: _N=...)
# count(start=0, step=1) --> count object
#   Return a count object whose .next() method returns consecutive values. 
#   Equivalent to:
#   def count(firstval=0, step=1):  
#        x = firstval  
#        while 1:  
#            yield x  
#            x += step  

counter = itertools.count(start=5, step=5)
print(next(counter)) #5
print(next(counter)) #10
print(next(counter)) #15

# ZIP 
# - builtin - not itertools specific
# def zip(iter1: Iterable[Any], iter2: Iterable[Any], *iterables: Iterable[Any])
# zip(iter1 [,iter2 [...]]) --> zip object
#   Return a zip object whose .next() method returns a tuple 
#       where the i-th element comes from the i-th iterable argument. 
#   The .next() method continues 
#       until the shortest iterable in the argument sequence is exhausted and 
#       then it raises StopIteration.

daily_data = list(zip(itertools.count(), [100, 200, 300, 400], ['a','b','c','d'])) 
    # [(0, 100, 'a'), (1, 200,'b'), (2, 300,'c'), (3, 400,'d')]

# ZIP_LONGEST
# def zip_longest(*p: Iterable[Any], fillvalue: Any=...)
# zip_longest(iter1 [,iter2 [...]], [fillvalue=None]) --> zip_longest object
#   Return a zip_longest object whose .next() method returns a tuple where the i-th element comes from the i-th iterable argument.
#   The .next() method continues until the longest iterable in the argument sequence is exhausted 
#   and then it raises StopIteration. 
#   When the shorter iterables are exhausted, the fillvalue is substituted in their place. 
#   The fillvalue defaults to None or can be specified by a keyword argument.

print (list(zip(itertools.count(), [100,200,300,400], ['a','b']))) # [(0, 100, 'a'), (1, 200, 'b')]
print (list(itertools.zip_longest([100,200,300,400], ['a','b'])))
    #[(100, 'a'), (200, 'b'), (300, None), (400, None)]
    #Notice that after the shortest iterator runs out, 
    #the zip_longest still continues by replacing missing values by None

# CYCLE
# def cycle(iterable: Iterable[_T])
# cycle(iterable) --> cycle object
# Return elements from the iterable until it is exhausted. 
# Then repeat the sequence INDEFINITELY.
counter = itertools.cycle(['a', 'b', 'c'])
print(next(counter)) #a
print(next(counter)) #b
print(next(counter)) #c
print(next(counter)) #a
print(next(counter)) #b
print(next(counter)) #c

# REPEAT
# def repeat(object: _T, times: int)
# repeat(object [,times]) -> create an iterator which returns the object for the specified number of times. 
# If not specified, returns the object endlessly.
counter = itertools.repeat(2)
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2

counter = itertools.repeat(2, times=3)
print(next(counter)) #2
print(next(counter)) #2
print(next(counter)) #2
# print(next(counter)) #StopIteration Exception

# practical example of repeat - sort of
squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares, end=",") #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
