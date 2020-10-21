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
