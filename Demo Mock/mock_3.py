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

# Write a function which converts decimal number to hexadecimal
'''
def decimal_to_hexa(decimal):
    if decimal == 0:
        return "0"
    hexa_digits = "0123456789ABCDEF"
    hexadecimal = ""
    
    while decimal > 0:
        rem = decimal % 16 
        hexadecimal =  hexa_digits[rem] + hexadecimal
        decimal = decimal // 16 
    return hexadecimal

decimal = 11
print(decimal_to_hexa(decimal))
'''

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            res = 0 

            while num > 0:
                res += num % 10
                num = num // 10
            num = res
        return num
'''
#  make a stack with a queue

from collections import deque
class Stack:
    def __init__(self):
        self.q = deque()
    
    def push(self,x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            return self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    def top(self):
        return self.q[0]
    def empty(self):
        return not self.q

s = Stack()
s.push(1)
s.push(2)
s.push(3)



print(s.pop())   # 3
print(s.pop())   # 2
print(s.pop())   # 1
print(s.empty()) # True
