# Given a string of characters. Reverse the string without using any library function.
'''
s = "love"
n = len(s)
rev = ""
for i in range(n-1, -1, -1):
    rev += s[i]
print(rev)
'''
'''
def solve(s):
    s = list(s)  
    n = len(s)
    for i in range(n // 2):
        temp = s[i]
        s[i] = s[n - i - 1]
        s[n - i - 1] = temp
    return ''.join(s) 

s = "love"
reversed_s = solve(s)
print(reversed_s)
'''

# Given a string of characters [0-9]. Convert it to integer.
'''
s = "1284940"
n = len(s)
res = 0 
for i in range(n):
    res = (res*10) + int(s[i])
print(type(res))
print(res)
'''

# Write a function which finds all the subset of a given set.
'''
from itertools import permutations
nums = [1,2,3]
res = list(permutations(nums))
# print(res)
for i in res:
    print(list(i))
'''
