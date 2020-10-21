'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

dummy_list = [10, 15, 3, 7]
temp = []
k = 17
while (len(dummy_list) > 0):
    if (k - dummy_list[0]) not in temp:
        temp.append(dummy_list[0])
        dummy_list = dummy_list[1:]
    else:
        print("Match found!")
        print(dummy_list[index], k-dummy_list[index])
        exit(0)
    
print("No match found")
exit(1)