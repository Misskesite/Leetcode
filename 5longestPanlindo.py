# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:36:08 2019

@author: liuga
"""
#先看小子串
class Solution(object):
    def longestPalindro(self,s):
        
        if len(set(s)) == 1:
            return s
        
        n =  len(s)
        start, end, maxL = 0, 0, 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j]==s[i])& ((i-j <2) | dp[j+1][i-1])
                if dp[j][i] and maxL < i-j+1:
                    maxL = i-j+1
                    start = j
                    end = i
            
            dp[i][i] = 1
            
        return s[start: end+1]
        
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j] and j - i + 1 > maxLen:
                maxLen = j - i + 1
                begin = i
                end = j
