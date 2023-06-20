# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:22:36 2019

@author: liuga
"""
#参考此题
#动态规划 时间复杂度O(n)  dp[i]代表解析s[:i]字符串所有可能的方式数目, 跟爬楼梯很像
class Solution(object):
    def numDecoding(self, s):
        n = len(s)
        
        dp =[0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            if int(s[i-1]) != 0:
                dp[i] = dp[i-1] #否则为0
            if i != 1 and 9 < int(s[i-2:i]) < 27: #看否跟前一个数字组成大于等于 10 且小于等于 26 的数，能的话可以加上 dp[i-2]，否则就只能保持为0了
                dp[i] = dp[i] + dp[i-2]
                
        return dp[-1]



#两个数字组成小于26且大于10时。字符串s[:i]的所有可能解码方式等于s[:i-1]+s[:i-2].
#对0处理，S[i]=0,且‘0’前面一位大于2，比如30，无法解码，返回0
#S[i]=0,且‘0’前面一位小于2，只能让0和前面一位编码 dp[i] = dp[i-2]
#s[i-1]等于0，由于0只能跟s[i-2]字符匹配解码，那s[i]只能单独解码或者和s[i+1]共同解码

class Solution(object):
    def numDecoding(self, s):
        if not s:
            return 0
        if s and s[0] == "0":
            return 0

        dp = [0 for _ in range(len(s))]

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1: i+1] > '27' or s[i-1] == '0':
                    return 0
                else:
                    dp[i] = dp[i - 2]
            elif s[i-1: i+1] < '10':
                dp[i] = dp[i - 2]
                
            elif s[i-1: i+1] < '27':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]
    
