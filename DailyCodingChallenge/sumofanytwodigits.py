'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

dummy_list = [1, 4, 45, 6, 10, -8]
k = 16
dummy_list.sort()
print(dummy_list)

while (len(dummy_list) > 0):
    sum = dummy_list[0] + dummy_list[-1]
    if sum == k:
        print("Match found")
        exit(0)
    elif sum > k:
        dummy_list = dummy_list[:-1] # remove the right most element
    else:
        dummy_list = dummy_list[1:] # remove the left most element
    print(dummy_list)

print("No match found")
exit(1)