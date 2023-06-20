# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:10:30 2019

@author: liuga
"""
#动态规划, dp[i](前i位可以用wordDict单词表示)= True 等于S[:i]可以被分割 时间复杂度O(n*n) 空间复杂度O(n)
class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True #空字符可以被表示？
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
    
    def wordBreak2(self, s, wordDict):
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]
