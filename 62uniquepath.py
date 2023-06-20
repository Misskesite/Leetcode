# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:01:51 2019

@author: liuga
"""
#dp[i][j] 是到达 i, j 最多路径
class Solution(object):
    def uniquPath(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m) ] #边界 i=0 或者 j= 0时 dp = 1
        for i in range (1, n):
             for j in range(1, m):
                 dp[j][i] = dp[j-1][1]+ dp[j][i-1]
                 
        return dp[m-1][n-1]

#空间优化
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m): #这里顺序？不是逆序
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
'''
只需要上一排上方和同排左边的值，这里累加

