# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:45:01 2020

@author: liuga
"""
#背包问题 dp[x][y]表示至多使用x个0，y个1可以组成字符串的最大数目,
#dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么剩下的可以取的最多的数字

#dp[i][p][q]表示从第一个元素到第i个元素为止，背包容量还剩p个0和q个1时的最优解 
#类似凑硬币？
class Solution(object):
    def onesZeros(self, strs, m ,n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for str in strs:
            zeros, ones = 0,0
            for c in str:
                #zeros, ones = s.count('0'), s.count('1')
                if c =='0':
                    zeros += 1
                elif c == '1':
                    ones += 1
            for i in range(m, zeros-1,-1):
                for j in range(n, ones-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]
                
                    
                
        
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        
        return dp[m][n]
