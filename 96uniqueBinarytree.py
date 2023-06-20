# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:42:36 2019

@author: liuga
"""
#dp[0] = 1 表示空树， dp[i]表示i个节点组成的树的种数
#遍历从1到i的每一个数，讨论作为根节点的数量
class Solution(object):
    def uniqueBinarytree(self, n):
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):            
            for j in range(i):
                dp[i] = dp[i] + dp[j]*dp[i-j-1]

        return dp[n]
        

class Solution2(object):
    def numTrees(self, n):
        dp = [1,1]
        for i in range(2, n+1):
            cnt = 0
            for j in range(i):
                cnt += dp[j]*dp[i-j-1]
            dp.append(cnt)
        return dp.pop()
