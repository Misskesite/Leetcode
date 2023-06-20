# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:51:29 2019

@author: liuga
"""
#贪心算法？
class Solution(object):
    def wildcardMatch(self, s ,p):
        pPoint ,sPoint ,last_pPoint,last_sPoint = 0, 0, 0, -1
        
        while sPoint < len(s):
            if pPoint < len(p) and (s[sPoint]==p[pPoint] or p(pPoint) == '?' ):
                pPoint +=1
                sPoint +=1
            #mach with *
            elif pPoint < len(p) and p(pPoint) == '*' :
                last_pPoint = pPoint
                pPoint +=1
                last_sPoint = sPoint
            
            #not match, but there is * before 
            elif last_pPoint != -1:
                 last_sPoint +=1
                 pPoint = last_pPoint
                 sPoint = last_sPoint
            # Not match and there is no '*' before
            else:              
                return False
            
            #check if there is still character except * in the pattern
            while pPoint < len(p) and p(pPoint) == '*':
                pPoint += 1
            
            return pPoint == len(p)
             

#DP 时间复杂度O(m*n) 空间复杂度O(m*n)  ("ab", "?*") → true  ("aa", "a*") → true  ("aa", "*") → true *代表0个+字符
#下标从0 开始，因此Si和Pj 分别对应着 s[i-1]和 p[j-1]
class Solution(object):
    def wildCard(self,string ,pattern):
        # Code here
        m = len(string)
        n = len(pattern)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 1
        
        #p是连续的*  星号匹配空字符
        for j in range(1, n+1):
            dp[0][j] = pattern[j-1] == "*" and dp[0][j-1] #边界条件
            '''
        for j in range(1, n+1):
            if pattern[j-1] == "*":
                dp[0][j] = True
            else:
                break

            '''
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if pattern[j-1] == string[i-1] or pattern[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                    
                #p的上一个字符是*则表示s后退一位 或者 P往后走一位。 使用或者不使用这个星号
                elif pattern[j-1] == "*" :
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] #匹配一个字符？，两个，三个都可以dp[i][j] = dp[i-1][j] = dp[i-2][j]
        return dp[m][n]
