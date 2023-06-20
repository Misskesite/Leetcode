# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:31:10 2019

@author: liuga
"""
#DP  DP[i][j]表示S1的前i个字符和S2的前j个字符能否构成s3的前 i+j个字符
#时间复杂度O(m*n) 空间复杂度O(m*n)

class Solution(object):
    def interleavingString(self, S1, S2, S3):
        m = len(S1)
        n = len(S2)
        l = len(S3)
        
        if m + n != l:
            return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and S1[i-1] == S3[i-1]
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and S2[j-1] == S3[j-1]
            
        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and S1[i-1] == S3[i+j-1]) or (dp[i][j-1] and S2[j-1] == S3[i+j-1])
        return dp[m][n]
            
'''
s1 的前 i 个字符和 s2 的前 j-1个字符能否构成 s3 的前 i+j-1位，且 s2的第 j 位（s2[j-1]）是否等于 s3的第 i+j位（s3[i+j-1]）。
