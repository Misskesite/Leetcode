# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:44:16 2020

@author: liuga
"""
#dp[i]表示amount需要的最少数目的硬币，背包问题模板: 外循环遍历arrs，内循环遍历target，且内循环倒序
class Solution(object):
    def coinchange(self, coins, amount):
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:    #遍历物品
            for i in range(coin, amount+1): #隐含i>= coin 遍历背包
                if dp[i-coin] != float('inf'): #是初始值跳过？为什么
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

'''
钱币最小个数，那么钱币有顺序和没有顺序都可以,本题不强调排列或者组合。如果是组合，外层for循环物品。
如果排列，则是内层for遍历背包

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] := fewest # Of coins to make up i
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
