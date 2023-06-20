# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:31:43 2019

@author: liuga
"""
#贪心算法，每一步做出当时最佳选择(局部最优)只加正数 时间复杂度O(n) 空间复杂度O(1)\
#跨越多天的买卖都化解成相邻两天的买卖
class Solution(object):
    def maxProfit(self, prices):
        
        if len(prices)< 2:            
            return 0
        
        profit = 0
        
        for i in range(1, len(prices)):
            profit += max（prices[i] - prices[i-1], 0):
                
        return profit

    

#动态规划  dp[i][0] 表示第 i天交易完后手里没有股票的最大利润，dp[i][1] 表示第 i天交易完后手里持有一支股票的最大利润
class Solution2(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[n-1][0]

    #简化
    dp0 = 0
    dp1 = -prices[0]
    for i in range(1, n):
        newDp0 = max(dp0, dp1 + prices[i])
        newDp1 = max(dp1, dp0 - prices[i])
        dp0 = newDp0
        dp1 = newDp1
    return dp0

        
class Solution3(object):
    def maxProfit(self, prices):
        buy = -float("inf")
        sell = 0

        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p)

        return sell
    
    
class Solution2(object):
    def maxProfit(self, prices):
        profit = 0
        if len(prices) == 0:
            return 0
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            high = prices[i]
            
            profit += high - low    
        return profit
