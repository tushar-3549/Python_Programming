# find 2nd largest element
'''
arr = [1,2,3,4,5]
f = float('-inf')
s = float('-inf')
for num in arr:
    if num > f:
        s = f 
        f = num
    elif num > s and num != f:
        s = num 
print(s) 
'''

# find 3rd largest element 
'''
arr = [1,2,3,4,5]
f = float('-inf')
s = float('-inf')
t = float('-inf')
for num in arr:
    if num > f:
        t = s 
        s = f 
        f = num 
    elif num > s and num != f:
        t = s 
        s = num 
    elif num > t:
        t = num
print(t)
'''

# kth largest number 
'''
import heapq
arr = [1,2,3,4,5]
k = 2
min_heap = []
for i in arr:
    if len(min_heap) < k:
        heapq.heappush(min_heap, i)
    else:
        heapq.heappushpop(min_heap, i)
print(min_heap[0])
'''

# rotate array
'''
def rotate(arr, k):
    n = len(arr)
    k = k%n 
    return arr[k:] + arr[:k]
arr = [1,2,3,4,5]
k = 3
print(rotate(arr, k))
'''

# merged two sorted array
'''
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge_sorted_arrays(arr1, arr2))
'''

# Count occurrences of a character
'''
s = "aasttressx"
char_cnt = {}

for char in s:
    if char in char_cnt:
        char_cnt[char] += 1
    else:
        char_cnt[char] = 1

for char, count in char_cnt.items():
    if count > 1:
        print(f"'{char}' occurs {count} times")
'''

# First non-repeating character
'''
s = "aasttressx"
char_count = {}

# Count each character manually
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the first non-repeating character
for char in s:
    if char_count[char] == 1:
        print("First non-repeating character is:", char)
        break
else:
    print("No non-repeating character found.")
'''

# binary search 
'''
arr = [1,2,3,4,5]
x = 4
l = 0
r = len(arr)-1
ans = -1
while l <= r:
    mid = (l+r)//2
    if arr[mid] == x:
        ans = mid
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid-1
print(ans)
'''

# Print array using recursion
'''
def print_arr(arr, ind = 0):
    if ind == len(arr):
        return
    print(arr[ind])
    print_arr(arr, ind+1)
arr = [1,2,3,4]
print_arr(arr)
'''
# Generate all permutations of a list
'''
def permute(nums, path=[]):
    if not nums:
        print(path)
        return
    for i in range(len(nums)):
        permute(nums[:i] + nums[i+1:], path + [nums[i]])

nums = [1, 2, 3]
permute(nums)
'''
# permutations backtrack
'''
def permute(nums):
    ans = []
    sol = []
    n = len(nums)

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
    backtrack()
    return ans

nums = [1,2,3]
print(permute(nums))
'''
# Sort a list of tuples by 2nd value

'''
data = [(1, 5), (2, 3), (4, 1), (3, 2)]
sorted_data = sorted(data, key = lambda x: x[1])
print(sorted_data)
'''

# Group Anagram 
'''
from collections import defaultdict
def groupAnagram(strs):
    anagram = defaultdict(list)
    for w in strs:
        key = ''.join(sorted(w))
        anagram[key].append(w)
    return list(anagram.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))
'''

# Check Prime number
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = 7
print(is_prime(num))
'''

# Sum Of Digits
'''
def sumOfDigit(n):
    ans = 0
    while n != 0:
        ans += n % 10
        n = n // 10
    return ans 
n = 12
print(sumOfDigit(n))
'''

# String to int 

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    if not s:
        return 0
    sign = 1
    if s[0] == '+':
        sign = 1
        s = s[1:]
    elif s[0] == '-':
        sign = -1
        s = s[1:]
    num = 0
    for c in s:
        if c.isdigit():
            num = num*10+int(c)
        else:
            break
    num *= sign 

    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX

    return num
print(myAtoi("32"))
        
