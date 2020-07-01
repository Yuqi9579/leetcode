'''
278. First bad version
Easy

[g,g,g,g,g,b,b,b] g:good b:bad
[1,2,3,4,5,6,7,8] 找到第一个bad产品
类比开二次根，都是找到一个临界值(在一个广义sorted的list中)，具体取上还是取下要具体分析
'''


class Solution():
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n + 1
        while l < r:
            m = l + (r - l) //  2
            if isBadVersion(m): #目标值在右边的判定条件
                r = m
            else:
                l = m + 1
        return l #开方中返回的l-1，注意具体问题具体分析
        
def isBadVersion(x):
    '''
    官方给的函数
    '''
    pass