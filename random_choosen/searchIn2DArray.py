'''
剑指04

Find a number in an array whose row and column 
are in an ascended order.

if exist: return True
else: return False
'''
from typing import List

class Solution():
    def findNumberIn2DArray_ls(self, matrix: List[List[int]], target: int) -> bool:
        #linear search 从右上角或者左下角开始是因为这样可以确定上下界，从左上角或者右下角就不行
        if matrix == []:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False

