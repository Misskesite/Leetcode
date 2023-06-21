# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:44:21 2020

@author: liuga
"""
#类似的问题 5，409, 516， 647， 730
#字符不连续 bbbab -> bbbb(4) 对角线表示一个字符的回文子序列长度为1
#dp[i][j]表示字符串在[i,j]范围内最长的回文子序列
class Solution(object):
    def longestPanlin(self, s):
         n = len(s)
         dp =[[0]*n for _ in range(n)]
         for i in range(n-1,-1,-1):
             dp[i][i] = 1
             for j in range(i+1,n):
                 if s[i] == s[j]:
                     dp[i][j] = dp[i+1][j-1]+2
                 else:
                     #分别加入s[i], s[j]看看哪一个可以组成最长的回文子序列
                     dp[i][j]= max(dp[i+1][j],dp[i][j-1])
         return dp[0][n-1] #dp[0][-1]


''''
base状态，最终状态，通过相对位置，确认状态转移方城
base: dp左下角三角形为0，对角线为1(回文子序列为自己) 对角线下半部分三角形表示i>j 不可能出现这种情况，因此为0
最终状态 dp[0][n-1]
对于dp[i][j] 知道了左边元素。下边元素，左下边元素。结合最终状态，从左到右，从下到上遍历dp
'''
模板:
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if s[i]== s[j]:
            dp[i][j] = dp[i+1][j-1] + 2
        else:
            dp[i][j]= = max(dp[i+1][j], dp[i][j-1])
