# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 21:28:53 2019

@author: liuga
"""
#local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)

#global[i][j] = max(local[i][j], global[i - 1][j])，
class Solution(object):
    def maxprofit(self, k, prices):
        if k <= 0 or not prices:
            return 0
        n = len(prices)
        if n < 2:
            return 0
        if k >= n//2:
            s = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    s += prices[i] - prices[i-1]
            return s
        
        g = [0]*(k+1)
        l = [0]*(k+1)  #最后一次交易在最后一天卖出
        for i in range(n-1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j-1] + max(diff,0), l[j] + diff)
                g[j] = max(l[j], g[j])
        return g[-1]

#Actually we only need to compare pre profit we made and profit we got in the for loop
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    
        if not prices:
            return 0
        
        if k >= len(prices) // 2:
            return sum(
                x - y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y)
        
        
        profits = [0]*len(prices)
        for j in range(k):

            preprofit = 0
            for i in range(1,len(prices)):
            
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit + profit, profits[i]) #preprofit为最后一天卖出的利润？局部最优
                profits[i] = max(profits[i-1], preprofit)
    
        return profits[-1]

class Solution(object):
    def maxProfit(self,k, prices):
        if not prices:
            return 0
        n = len(prices)

        k = min(k, n//2)
        
        #定义二维数组
        buy = [[0]*(k+1) for _ in range(n)]
        sell = [[0]*(k+1) for _ in range(n)]

        buy[0][0] = -prices[0]
        sell[0][0] = 0

        for i in range(1, k+1):
            buy[0][i] = sell[0][i] = -float["inf"]

        for i in range(1, n):
            buy[i][0] = max(buy[i-1][0], sell[i-1][0] - prices[i])
            for j in range(1, k+1):
                
            buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                
            sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])

        return max(sell[n-1])

    '''
#时间复杂度O(min(n,k))
    def maxProfit(self,k, prices):
        if not prices:
            return 0
        
        n = len(prices)

        k = min(k, n//2)
        
        #定义二维数组
        buy = [0]*(k+1) 
        sell = [0]*(k+1)

        buy[0] = -prices[0]
        sell[0] = 0
        for i in range(1, k + 1):
            buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(k, 0, -1): 
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i]); 

        return max(sell)
       '''     
    

#最大化手里的钱，买股票手里的钱变少，卖股票手里的钱变多，保证最大化手里持有钱。
#这一次买或者卖只跟上一次我们卖还是买的状态有关
class Solution(object):
    def maxprofit(self, k, prices):
        if not prices:
            return 0
        
        k = min(k, len(prices)//2)
        buy = [float("-inf")] * (k+1)
        sell = [0] * (k+1)

        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - p) 
                sell[i] = max(sell[i], buy[i] + p)

        return sell[-1]
        
'''
    sell = [0] * (k + 1)
    buy = [-math.inf] * (k + 1)

    for price in prices:
      for i in range(k, 0, -1):
        sell[i] = max(sell[i], buy[i] + price)
        buy[i] = max(buy[i], sell[i - 1] - price)

    return sell[k]
'''
    
因为第j次买入只和第j-1卖出相关，第j次卖出只和第j次买入相关
dp[j-1][1] = max(dp[j-1][1], dp[j-1][0] - prices[i]) #买入？
dp[j][0] = max(dp[j][0], dp[j-1][1] + prices[i])     #卖出？
