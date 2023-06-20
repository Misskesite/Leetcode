# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:19:13 2019

@author: liuga
"""
#dp[i][j]是以matrix(i-1, j-1)为右下角的正方形最大边长
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                res = 1
                
        for j in range(n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                res = 1
                
        #以i,j位置为右下顶点能够从的最大长方形的边长         
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 #只有当前 (i, j) 位置为1，dp[i][j] 才有可能大于0，否则 dp[i][j] 一定为0。当 (i, j) 位置为1，此时要看 dp[i-1][j-1], dp[i][j-1]，和 dp[i-1][j] 这三个位置，我们找其中最小的值，并加上1，就是 dp[i][j] 的当前值了，这个并不难想，毕竟不能有0存在，所以只能取交集，最后再用 dp[i][j] 的值来更新结果 res 的值即可
                    res = max(res, dp[i][j])
                    
        return res*res

'''
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            res = max(res, dp[i][j])
return res*res

'''
