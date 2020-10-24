'''
Upper_bound and lower_bound of a list.
两个bound的区别只是在取等号的情况下，返回的都是target的index

Binary search
'''

from typing import List

def upper_bound(A: List, val: int) -> int:
    '''
    return: First INDEX of i, such that A[i] > val
    A = [1,2,2,2,4,4,5]
    upper_bound(A, 2) = 4   A[4]=4
    '''
    l = 0
    r = len(A)
    while l < r:
        m = l + (r-l) // 2
        # 这个就是模板中的g(m)在题中g(m)就是最终那个target所要满足的条件，因为最终l==r，所以满足这个条件时要移动r!!!
        if A[m] > val: 
            r = m
        else:
            l = m + 1
    return l

def lower_bound(A: List, val: int) -> int:
    '''
    return: First INDEX of i, such that A[i] >= val
    A = [1,2,2,2,4,4,5]
    lower_bound(A, 2) = 1   A[1]=2 
    '''
    l = 0
    r = len(A)
    while l < r:
        m = l + (r-l) // 2
        if A[m] >= val:
            r = m
        else:
            l = m + 1
    return l


    
if __name__ == '__main__':

    print(lower_bound([1,2,2,2,3,3,4,5,6,6,7,7,7,9], 3.5))
    print(upper_bound([1,2,2,2,3,3,4,5,6,6,7,7,7,9], 3.5))
