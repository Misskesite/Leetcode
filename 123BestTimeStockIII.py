# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:56:58 2019

@author: liuga
"""

class Solution(object):
    def BesttimeStock(self, prices):
        n = len(prices)
        if n ==0:
            return 0
        f1 =[0]*n
        f2 =[0]*n
        
        minV = prices[0]
        f1[0] = 0
        for i in range(1, n):
            minV = min(minV, prices[i])
            f1[i] = max(f1[i-1], prices[i] - minV)
            
        maxV = prices[n - 1]
        f2(n - 1) = 0
        for i in range(n - 1, 0, -1):
            maxV = max(maxV, prices[i])
            f2[i] = max(f2[i+1], maxV - prices[i])
            
        res = 0
        for i in range(n):
            if f1[i] + f2[i] > res:
                res = fi[i] + f2[i]
                
        return res

#未进行空间优化，任意天结束的时候 我们处在五个状态中的一种： 
'''
未进行任何操作 利润为0,不用记录
只进行一次买  buy1
进行了一次买和卖，即完成一笔交易 sell1
完成一笔交易的前提下，进行二次买 buy2
完成两笔交易 sell2
'''
class Solution2(object):
    def maxProfit(sef, prices):
        n = len(prices)
        buy1 = [0]*n
        sell1 = [0]*n
        buy2 = [0]*n
        sell2 = [0]*n

        buy1[0] = buy2[0] = -prices[0] #buy1[0] 以prices[0]的价格买入。buy2[0]在同一天买入卖出后再以prices[0]的价格买入
        sell1[0] = sell2[0] = 0        #sell1[0]同一天买入卖出，收益为0
        for i in range(1, n):
            buy1[i] = max(buy1[i-1], -prices[i])  #第i天没有操作，第i天买入股票
            sell[i] = max(sell1[i-1], buy1[i-1] + prices[i]) #第i天没有操作，第i天卖出股票
            buy2[i] = max(buy2[i-1], sell1[i-1] - prices[i])
            sell2[i] = max(sell2[i-1], buy2[i-1] + prices[i])

        return sell2[-1]
        
#空间优化 最大化手里的钱，买股票手里的钱变少，卖股票手里的钱变多，时间复杂度O(n), 空间复杂度O(1)
#最终答案是0, sell1, sell2中的最大值
class Solution2(object):
    def maxProfit(sef, prices):
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0 
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i]) #不买和买
            sell2 = max(sell2, buy2 + prices[i])

        return sell2
