# Count subsequence 
'''
def count_subsequences(s, words):
    count = 0
    for word in words:
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j+=1
            i+=1
        if j == len(word):
            count+=1
    return count


s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(count_subsequences(s, words))
'''

# Implement stack using queue

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = None
    def push(self,  x):
        self.q1.append(x)
        self.top_element = x
    def pop(self):
        while len(self.q1) > 1:
            self.top_element = self.q1.popleft()
            self.q2.append(self.top_element)
        popped = self.q1.popleft()
        self.q1 = self.q2 
        self.q2 = deque()
        return popped
    
    def top(self):
        return self.top_element
    def empty(self):
        return len(self.q1) == 0
    
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  
print(stack.pop()) 
print(stack.empty()) 