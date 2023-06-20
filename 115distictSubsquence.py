# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:29:54 2019

@author: liuga
"""
#dp[i][j]代表T的前i个字符串可以由S的j个字符串组成最多个数
class Solution(object):
    def distinctSubsquence(self, s, t):
        m = len(s)
        n = len(t)
        dp =[[0]*(m+1) for _ in range(n+1)]
        for j in range(m+1): #空集是所有字符串的子集
            dp[0][j] = 1
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if t[i-1] == s[j-1]: 
                    dp[i][j] = (dp[i-1][j-1] + dp[i][j-1])%1000000007 #选择匹配s[j-1]，(用s最后一位匹配) #不选择匹配s[j-1](用s之前的字符)
                else:
                    dp[i][j] = dp[i][j-1]                             
        return dp[-1][-1]

'''
s[i] == t[j] 时，以s = "rara" t = "ra" 为例，当i = 3, j = 1时，s[i] == t[j]。

此时分为2种情况，s串用最后一位的a + 不用最后一位的a。

如果用s串最后一位的a,那么t串最后一位的a也被消耗掉，此时的子序列其实=dp[i-1][j-1]

如果不用s串最后一位的a，那就得看"rar"里面是否有"ra"子序列的了，就是dp[i-1][j]
'''
#此解法为主
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp =[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1): #空集是所有字符串的子集
            dp[i][0] = 1
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]: 
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%1000000007 #选择匹配 不选择匹配
                else:
                    dp[i][j] = dp[i-1][j]                             
        return dp[-1][-1]
