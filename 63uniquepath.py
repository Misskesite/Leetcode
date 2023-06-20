# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:06:39 2019

@author: liuga
"""
#二维DP 
class Solution(object):
    def uniquPath2(self, Grid):
        if Grid[0][0] == 1:
            return 0
        
        m = len(Grid)
        n = len(Grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m) ]
        dp[0][0] = 1
        
        #边界出现障碍物
        for i in range (1, m):
            if Grid[i][0] == 1:
                break
            dp[i][0] = 1
            
        for j in range(1, n):
            if Grid[0][j] == 1:
                break
            dp[0][j] = 1 
        
        for i in range(1, m):
            for j in range(1, n):
                if Grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m-1][n-1] 


        m = len(Grid)
        n = len(Grid[0])
        dp = [[0]*n) for _ in range(m)]
        dp[0][0] = 1 if Grid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if Grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    if j-1>=0:
                         dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
    
#一维DP
class Solution2(object):
    def uniquPath2(self, Grid):
        if Grid[0][0] == 1:
            return 0
        
        m = len(Grid)
        n = len(Grid[0])
        
        dp = [0]*n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if Grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:                    
                    dp[j] += dp[j - 1]
        return dp[n-1]
        

