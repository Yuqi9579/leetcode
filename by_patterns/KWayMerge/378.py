'''
378. Kth smallest element in a sorted matrix
Medium

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

Out: 13

给一个行列都排序过的矩阵，返回第k个最小的元素，注意不是返回第k个distinct的最小元素，也就是说
可以有重复，如exp，将矩阵展开，[1,2,9,10,11,12,13,13,15]，第8小的是13。

思路：1.暴力解法，直接排序再取值,可以用归并排序，这样做只考虑了单方向的顺序
     2.小根堆 https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/shi-yong-dui-heapde-si-lu-xiang-jie-ling-fu-python/
     3.二分搜索
'''

from typing import List
from heapq import *
import sys
sys.path.append('/home/yuqi/Projects/leetcode/')
from utils.mergesort import MergeSortSortedList



class Solution():

   def kthSmallest_bf(self, matrix: List[List[int]], k: int) -> int:
      sort = MergeSortSortedList()
      sorted_list = sort(matrix)
      return sorted_list[k-1]


   def kthSmallest_heap(self, matrix: List[List[int]], k: int) -> int:
      '''
      把矩阵第一列作为初始heap，for q < k，pop，push其右边的元素，q--
      '''
      if matrix == [] or matrix[0] == []:
         return None

      n = len(matrix) #行数
      m = len(matrix[0])   #列数
      heap = [(matrix[i][0], i, 0) for i in range(n)] # 建立初始堆，为矩阵的第一列，第一行也行，后面是该元素的坐标方便后面的操作，初始堆不用heapify，因为每一列是增序的
      q = k
      while heap != [] and q > 0:
         val, x, y = heappop(heap) # item[0]:val, item[1]:xaxis, item[2]:yaxis
         if y != m - 1: #pop的元素是行最后一个的话，该行就不能再push元素进去了，列最后一个元素被pop后不影响，因为push的是它右边的元素
            heappush(heap, (matrix[x][y+1], x, y+1)) # 每次pop之后将被pop的右边的元素加进来
         q -= 1
      return val

if __name__ == '__main__':

   matrix1 = [
      [ 1,  5,  9],
      [10, 11, 13],
      [12, 13, 15]
   ]
   matrix2 = [[1,2],[1,3]]
   solution1 = Solution().kthSmallest_bf(matrix2, 4)
   solution2 = Solution().kthSmallest_heap(matrix2, 4)
