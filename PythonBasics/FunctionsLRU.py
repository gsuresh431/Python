'''
function caching(aka memoization)
- Memoization is an optimization technique used primarily 
to speed up computer programs by storing the results expensive function calls
and returning the cached results when the same inputs occur again

function contains a method lru_cache 
- LRU = Least Recently Used
- lru_cache maintains a cache which use LRU policy for cache maintenance
- what is lru policy? 
    - https://www.youtube.com/watch?v=S6IfqDXWa10&t=620s

How to use the lru_cache of functools module ?
- functools.lru_cache is a DECORATOR
- we need to place it on top of our function
'''

import time
import functools

@functools.lru_cache(maxsize=20)
def expensive_task(num):
    # time.sleep(num)
    return num

expensive_task(1)
expensive_task(5)
expensive_task(10)
expensive_task(10) # <-- will be fetched from LRU