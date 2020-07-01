'''
Exp1：Return the index of an element in a SORTED array.
      Elements are unique(注意这个条件). If not found return -1.

[l, r) 采用左闭右开，始终把subpart分为左中右三部分。
m = l + (r-l) // 2 = floor((l+r)/2)
'''

def binary_search_exp1(nums, val):
    l = 0
    r = len(nums)
    while l < r:
        m = l + (r-l) // 2 # [2,3,4,5,6,7]取5
        if nums[m] == val:
            return m
        if nums[m] > val:
            r = m
        else:
            l = m + 1
    return -1 



'''
Pattern
'''
def binary_search(l, r):
    while l < r:
        m = l + (r-l) // 2
        if f(m): return m 
        if g(m): 
            r = m
        else:
            l = m + 1
        return l # or not found

def f(m):
    pass

def g(m):
    pass