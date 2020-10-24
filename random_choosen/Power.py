class Solution():
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            y = pow(x, n//2)
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x
                
        if n > 0:
            return pow(x, n)
        else:
            return 1 / pow(x,n) 

solution = Solution()
solution.myPow(2, 5)