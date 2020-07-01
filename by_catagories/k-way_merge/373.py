'''
373. Find K pairs with smallest sums
Medium

给定两个list，找出最多k个数对(ui, vi)，u来自list1，v来自list2，使得u+v的和为最小的k个，这里不要求(u,v)的排列顺序。
思路：1.遍历所有数对，再排序
     2.python中heapq默认为小根堆，这里把入堆值取负，名义上是小根堆，但是实际上背后代表的item是按大根堆排列的，遍历产生k个item
       的堆，新入堆的值如果小于负堆顶，即还存在比堆顶u+v还小的，则弹出堆顶压入新item。口诀：小->大(根堆)->小
'''
from heapq import *
from typing import List

class Solution():
    def kSmallestPairs_bf(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        brutal force
        '''
        sum_uv = []
        n = 0
        for u in nums1:
            for v in nums2:
                sum_uv.append(([u,v],u+v))
                n += 1
        res = sorted(sum_uv, key=lambda s : s[1])
        return [item[0] for item in res]


    def kSmallestPairs_heapq(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        priority queue
        '''
        res = []
        for u in nums1:
            for v in nums2:
                val = u + v
                if len(res) < k: # 这里注意条件小于k，不能取等，即k-1进来之后在push进一个就是k了
                    heappush(res, (-val, [u,v]))
                else:
                    if val < -res[0][0]:
                        heapreplace(res, (-val, [u,v])) # heapreplace相当于同时pop和push，操作时间会快点
        return [item[1] for item in res]

if __name__ == '__main__':
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 7
    print(Solution().kSmallestPairs_heapq(nums1, nums2, k))