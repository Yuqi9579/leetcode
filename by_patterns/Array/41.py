'''
41. First missing positive
Hard

给一个未排序的array，找出最小的missing POSITIVE int
>>> [1,2,0]
3
>>> [3,4,-1,1]
2
>>> [7,8,9,11,12]
1
要求：O(n) time and constant extra space

思路：1.不考虑空间复杂度，将array存进hashset，从1开始遍历，返回第一个不在hashset中的数字
'''

from typing import List
import doctest

class Solution():
    def firstMissingPositive_hash(self, nums: List[int]) -> int:
        '''
        This solution uses linear extra space O(n), meaning that the space needed scales linearly 
        with respect to the size of the input. 
        The challenge of this question is being able to do it in-place O(1).
        '''
        exist = set()
        for num in nums:
            if num not in exist:
                exist.add(num)
        i = 1
        while True:
            if i in exist:
                i += 1
                continue
            else:
                return i
            

    def firstMissingPositive(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    nums = [2,7,4,9,1]
    print(Solution().firstMissingPositive_hash(nums))