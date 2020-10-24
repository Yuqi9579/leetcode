class Solution():
    def direction(i, j, trace):
        if i 


    def fill(ori_matrix, nums):
        m = len(ori_matrix)
        n = len(ori_matrix[0])
        trace = [[0 for i in range(n)] for i in range(m)]
        for num in nums:
            if trace[i][j] = 0:
                ori_matrix[i][j] = num
                j += 1
