# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:01:46 2019

@author: liuga
"""
#从左向右匹配要考虑后面是不是有*,这里选择从右往左扫描， s、p 串是否匹配，取决于：最右端是否匹配、剩余的子串是否匹配
#星号 按照 p[j-1] 和 s[i] 是否相等，我们分为两种情况：
# p[j-1] != s[i] : dp[i][j] = dp[i][j-2]   p[j-1] == s[i] or p[j-1] == "."
class Solution(object):
    def regularExpression(self,s,p):
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                   dp[0][i] = dp[0][i-2]
                   
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '.':                
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':  #单个字符匹配(a*一个a)， 没有匹配(a*为空)， 多个字符匹配(a*多个a)
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
                    
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] = p[j-1]
            
        return dp[len(s)][len(p)]
