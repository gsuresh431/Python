# How do you reverse a given string in place? 
str = 'How do you reverse a given string in place?'
str = str[::-1]
print(str)

#2: Reversed
str = 'How do you reverse a given string in place?'
str = "".join(list(reversed(str)))
print(str)

#3: Using while loop
str = 'How do you reverse a given string in place?'
temp_str = ''
index = len(str) - 1
while(index >= 0):
    temp_str = temp_str + str[index]
    index -= 1
print(temp_str)

# Reverse the order of words in a string
str = 'Reverse the order of words in a string'
print(" ".join(str.split()[::-1]))

# Reverse internal content of each word
string = 'Reverse internal content of each word'
print(" ".join(list(map(lambda x: x[::-1], string.split(" ")))))

string = 'REVERSE internal content of every second word present in the given string'
rev = []
for index, word in enumerate(string.split(" ")):
    if (index%2 == 0):
        pass
    else: 
        rev.append(word[::-1])
print(" ".join(rev))


# Program for the requirement,input: a4z2b3c2 and expected output: aaaabbbcczz(sorted)
a = "a4z2b3c2"
res = []
for pos in range(0, len(a), 2):
    char = a[pos:pos+2][0]
    rep  = a[pos:pos+2][1]
    res.append(char * int(rep))
print("".join(list(sorted(res))))

#Program for the requirement,input: aaaabbbccz and expected output: 4a3b2c1z
import collections
results = collections.Counter('aaaabbbccz')
for key,value in results.items():
    print("{}{}".format(value,key), end="")

# Check if two stings are anagrams
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
a = "abcde"
b = "edcabbbb"

if (("".join(sorted(a))) == ("".join(sorted(b)))):
    print("\n{} & {} are anagrams".format(a, b))
else :
    print("\n{} & {} are NOT anagrams".format(a, b))