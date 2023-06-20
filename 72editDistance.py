# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:47:19 2019

@author: liuga
"""
#word1 到i位置，转换成 word2到j位置 需要多少步
class Solution(object):
    def editDistance(self, m, n):
        len1 = len(m)
        len2 = len(n)
        
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        
        for i in range(len1+1):
            dp[i][0] = i #第一列 插入
        for j in range(len2+1):
            dp[0][j] = j #第一行 插入
       
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i - 1] != word2[j - 1]:                 
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1，dp[i-1][j-1]+1) #删除（word1的第i个字符 或者word2的第j个字符） 插入dp[i][j-1] 替换 dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1]
                
        return dp[len1][len2]


#dp[i][j-1]+1 插入，直接在s1[i]插入一个和s2[j]一样的值
#dp[i-1][j]+1 删除，直接把是s[i]这个字符删掉
#dp[i-1][j-1]+1替换，直接把s1[i]替换成s2[j]
#dp是自底向上，递归是自顶向下求解

dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
