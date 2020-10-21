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