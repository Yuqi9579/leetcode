'''
995. Minimum Number of K Consecutive Bit Flips
Hard

给定一个list，只包含1，0，和翻转范围k，求最小步数，将list翻转为全1
00010110 -> 111 10110 -> 1111 100 0 -> 11111 111 返回3
如果不能实现返回-1

思路：贪心算法，滑动窗口，窗口左端点遇到0就flip
'''
from typing import List

def flip(s: List, start: int, k: int):
    for i in range(k):
        s[start+i] = 1 - s[start+i]

class Solution():
    def minKBitFlips(self, A: List[int], K: int) -> int:
        '''
        窗口左端点遇到0就flip，ETL
        '''
        n = 0
        for i in range(len(A)):
            j = i + K - 1 #窗口右端的索引
            if A[i] == 0:
                if j > len(A) - 1: #当窗口右端索引大于len(s) - 1，且此时还存在0时返回-1
                    return -1
                flip(A, i, K)
                n += 1
        return n

if __name__ == '__main__':
    s = [0,0,0,1,0,1,1,0]
    print(Solution().minKBitFlips(s,3))