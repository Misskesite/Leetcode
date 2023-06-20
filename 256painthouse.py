# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:49:27 2020

@author: liuga
"""
#dp[j]是这一步取j + 上一步不取j的成本的最小值 相邻的房子不能用相同的颜色来刷
class Solution(object):
    def painthouse(self, costs):
        if not costs:
            return 0
        dp = costs[0][:]
        for i in range(1, len(costs)):
            #get previous minimum cost
            pre = dp[:]
            for j in range(len(costs[0])):
                dp[j]= costs[i][j]+ min(pre[:j], pre[j+1:])
        return min(dp)
    
# no two adjacent houses have the same color   
class Solution2(object):
    def minCost(self, costs):
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g            
            
        return min(red, blue, green)


#改写
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2]) # total minimum cost of painting previous house i houses  
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])


'''
#动态规划
    if not costs:
        return 0
    dp = costs
    for i in range(1, len(costs)):
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
    return min(dp[-1][0], dp[-1][1], dp[-1][2])
