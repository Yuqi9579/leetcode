'''
J13: 机器人运动范围

题目描述：
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1]
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

分析：
虽然说机器人可以上下左右移动，但是

'''

# from typing import List

# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         visited = [[0 for i in range(n)] for j in range(m)]
#         return self.dfs(0, 0, m, n, k, visited)

#     def bit_add(self, num):
#         s = 0
#         while num != 0:
#             adding = num % 10
#             num = num // 10
#             s += adding
#         return s 

#     def xy_bit_add(self, *args):
#         return sum(map(self.bit_add, args))
        
#     def dfs(self, i:int, j:int, m:int, n:int, k:int, visited):
#         if (i > m - 1 or j > n - 1 or self.xy_bit_add(i,j) > k or visited[i][j] == 1):
#             return 0
#         visited[i][j] = 1
#         return 1 + self.dfs(i, j+1, m, n, k, visited) + self.dfs(i+1, j, m, n, k, visited) 


class Solution:
    # 广度优先搜索
    def bit_add(self, num):
        s = 0
        while num != 0:
            adding = num % 10
            num = num // 10
            s += adding
        return s 

    def xy_bit_add(self, *args):
        return sum(map(self.bit_add, args))

    def bfs(self, start_i, start_j, m, n, k):
        n = 0
        queue = [(start_i,start_j)]
        visited = set((start_i, start_j))
        while len(queue) > 0:
            item = queue.pop(0)
            i, j = item[0], item[1]
            n += 1
            # towards right
            if not (i >= m or j+1 >= n or self.xy_bit_add(i, j+1) > k or (i, j+1) in visited):
                queue.append((i, j+1))
                visited.add((i, j+1))
            # towards dowm
            if not (i+1 >= m or j >= n or self.xy_bit_add(i+1, j) > k or (i+1, j) in visited):
                queue.append((i+1, j))
                visited.add((i+1, j))
        return n
    
    def movingCount(self, m: int, n: int, k: int) -> int:
        return self.bfs(0, 0, m, n, k)


print(Solution().movingCount(1,2,1))