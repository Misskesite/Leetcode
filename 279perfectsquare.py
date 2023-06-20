
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:59:36 2020

@author: liuga
"""
#时间复杂度O(n)，空间复杂度O(n) 完全背包。求完全平方数的最小数量 12 = 4 + 4 +4
class Solution(object):
    def perfectSquare(self, n):
        dp = [n]*(n+1)
        dp[0] = 0 #n大于0，非法
        dp[1] = 1
        for i in range(2, n+1):
            j = 1
            while j*j < i : #for j in range(1, int(i**0.5)+1))
                dp[i] = min(dp[i],dp[i-j*j] + 1)
                j += 1
        return dp[-1]

    def perfectSquare(self, n):
        dp = [0] + [inf] * n
        rg = int(sqrt(n))
        for i in range(1, rg + 1):
            curr = i * i
            for j in range(curr, n+1):
                dp[j] = min(dp[j],dp[j - curr] + 1)
        return dp[n]

    def numSquares(n):
	dp = [0] + [float('inf')]*n
	for i in range(1, n+1):
		dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
	return dp[n]

#dp[i] records to least number of perfect square numbers that sum up to i. And there are multiple ways for perfect square numbers to sum up to i.
#The candidate way is to add a perfect square number j*j to a sum of perfect square numbers that equals to i.
#And it can be generized as(概括为) i-j*j + j*j. So the least number of perfect square numbers that sum up to i-j*j is dp[i-j*j]. 
