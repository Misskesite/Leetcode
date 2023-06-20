# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:20:56 2019

@author: liuga
"""
#贪心算法 先确定一边(右边评分比左边大)
class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candy = [1]*n
        for i in range(1, n):      #从前向后，右边评分大于左边
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1]+1
        for i in range(n-2, -1, -1):#从后向前，左边大于右边
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)
        return sum[candy]
                
'''
贪心(归纳法)，手动模拟，举反例
