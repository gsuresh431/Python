'''
2019-11-09
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, 
the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
a = [7,8,9,11,12]
# a.sort()
print(a)

start = 1
while(True):
    if (start in a):
        start += 1
    else:
        print(start)
        break








