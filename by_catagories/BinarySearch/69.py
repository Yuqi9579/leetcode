'''
69. Sqrt(x)
Easy

Compute and return the square root of x, 
where x is guaranteed to be a non-negative integer.
向下取整

思路：找到一个最小的整数，其平方大于input，假如input为9，那么目标值必定在[0, 9)
     之中， 我们只需要在上述区间中进行二分查找，找到一个数，其平方和刚刚大于input，
     其之前一个数平方和刚刚小于等于input，最后返回这个index-1
'''

class Solution():
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x + 1 #目标值在[0, x+1)中，目标值等于x是1,0的情况
        while l < r:
            # 分开写的话，先判断m*m == x，return m
            # 但其实l - 1包含了这种情况，所以合起来写了
            m = l + (r - l) // 2 
            if m * m > x:
                r = m
            else:
                l = m + 1
        return l - 1

if __name__ == "__main__":
    print(Solution().mySqrt(8))
