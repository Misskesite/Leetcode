# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:03:45 2020

@author: liuga
"""
# O(n) O(n) 第一天不能有卖股票
#sell 该天结束时候，手里没有股票(卖完股票？)，已经获取的最大利益
#hold 该天结束时候，手里有股票，已经获取的最大利益
class Solution(object):
    def maxprofit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        sell = [0]*n
        hold = [0]*n
        hold[0] = -prices[0]
        for i in range(1,n):
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i]) #今天啥没干| 前天卖了股票，今天买了股票(昨天必须休息)
            sell[i] =  max(sell[i-1], hold[i-1] + prices[i]) #今天啥没干，今天卖了股票            
        return sell[-1]

    
    
#1 2 3 0 2 -> 3 [buy, sell, cooldown, buy, sell]
#空间复杂度 O(1)
class Solution2(object):
    def maxprofit(self, prices):
        if not prices:
            return 0
        prev_sell = 0
        cur_sell  = 0
        hold  = -prices[0]
        for i in range(1, len(prices)):
            temp = cur_sell
            cur_sell = max(cur_sell, hold + prices[i])
            hold = max(hold, (prev_sell if i >=2 else 0) - prices[i])
            prev_sell = temp
        return cur_sell
           

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -math.inf #对应hold
        prev = 0 #冷冻期？

        for price in prices:
            cache = sell
            sell = max(sell, buy + price)
            buy = max(buy, prev - price) #不买和买?
            prev = cache

        return sell

