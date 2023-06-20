# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:40:37 2019

@author: liuga
"""

class Solution(object):
    def maxProfits(self, prices):
        if len(prices) <2 :
            return 0
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
            
        return max_profit