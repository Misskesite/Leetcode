# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:18:44 2020

@author: liuga
"""

class Solution(object):
    def painthouse(self, costs):
        if not costs:
            return 0
        dp = costs[0][:]
        
        def GetMin(idx, k):
            Min = max(costs[idx])
            for i, cost in enumerate(costs[idx]):
                if i == k:
                    continue
                Min = min(Min, cost)
            return Min
        
        for i in range(1, len(costs)):
            for k in range(len(costs[i])):
                dp[i][k] += GetMin(i-1, k)
        return min(dp[-1])


import heapq
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        ## 1. Instead of finding the Minimum everytime, you can save 2 minimums from the prev row initially
        ## 2. while going through j loop, you can directly use first minimum if the first minimum column and current column are not same.
        ## 3. If the first minimum and current column are same THEN ONLY use second minimum
        
	## TIME COMPLEXITY : O(MxN) ##
	## SPACE COMPLEXITY : O(1) ##

        if not costs : 
            return 0
        for i in range(1, len(costs)):
            mins = heapq.nsmallest(2, costs[i - 1])
            for j in range(len(costs[0])):
                if costs[i - 1][j] == mins[0]: 
                    costs[i][j] += mins[1] 
                else:
                    costs[i][j] += mins[0]
        return min(costs[-1])
