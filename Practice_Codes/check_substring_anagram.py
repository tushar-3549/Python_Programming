# Given two strings s1 and s2, return whether a substring of s1 is an anagram of s2.
from collections import Counter
def solve(s1, s2):
    len_s2 = len(s2)
    count_s2 = Counter(s2)
    
    for i in range(len(s1)-len_s2+1):
        window = s1[i:i+len_s2]
        if Counter(window) == count_s2:
            return True
    return False
        

s1 = "hello"
s2 = "lol"
print(solve(s1, s2))
