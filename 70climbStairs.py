d# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:02:24 2019

@author: liuga
"""

class Solution(object):
    def climStair(self, n):
        
        if n <= 2:
            return n
        dp =[0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
            
        return dp[n]
