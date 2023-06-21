# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:39:11 2020

@author: liuga
"""

class Solution(object):
    def deleteOperation(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0]*len(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        val = dp[-1][-1] #相同的元素个数?
        return l1 - val + l2 - val # l1 + l2 - 2*dp[n1][n2]
    
