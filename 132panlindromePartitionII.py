# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:43:38 2019

@author: liuga
"""
#看[j + 1, i]区间 dp[i] = min(dp[i], dp[j] + 1) 用一个变量j从0遍历到i，这样就可以把区间 [0, i] 分为两部分，[0, j-1] 和 [j, i]，如果区间[j, i]内的子串是回文串，那么此时dp[i]就可以用dp[j-1]+1来更新了
class Solution(object):
    def miniCut(self, s):
        n = len(s)
        dp = [i for i in range(n)]
        isPal = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            
            for j in range(i+1):
                if s[j] == s[i] and (j+1 > i-1 or isPal[j+1][i-1]):
                    isPal[j][i] = True
                    if j == 0:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1) 
            
        return dp[-1]
        


#用了两个dp实现
class Solution2(object):
    def miniCut(self, s):
        n = len(s)
        isPal = [[True]*n for _ in range(n)]
        dp = [float("inf")]*n                //也可以初始化dp[i] = i
        dp[0] = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n): #j从i+1开始 保证j-i >=1 ?
                isPal[i][j] = (s[i] == s[j]) and isPal[i+1][j-1]
    
        for i in range(1, n):
            if isPal[0][i] = 0:
                dp[i] = 0
                continue
            for j in range(i):
                if isPal[j+1][i]:
                    dp[i] = min(dp[i], dp[j]+1)

        return dp[n-1]
                    
    
