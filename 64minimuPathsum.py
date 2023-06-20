# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:51:32 2019

@author: liuga
"""

class Solution(object):
    def minimumPath(self,grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        
        for j in range(1,n):
            dp[j] = dp[j-1] + grid[0][j]
            
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j]= min(dp[j],dp[j-1]) + grid[i][j]
                
        return dp[-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m - 1][n - 1]


#时间复杂度O(mn) 空间复杂度O(1) 原地修改
class Solution(object):
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0: #j == 0
                    grid[i][0] += grid[i - 1][0]
                elif j > 0: # i == 0
                    grid[0][j] += grid[0][j - 1]

        return grid[m - 1][n - 1]
