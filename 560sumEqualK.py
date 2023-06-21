# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:23:40 2020

@author: liuga
"""
#类似题: 1, 1248, 454 前缀和
import collections

class  Solution(object):
    def sumEqualtoK(self, nums,k):
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        pre_sum = 0
        res = 0
        
        for i in range(n):
            pre_sum += nums[i] #前缀和
            if pre_sum - k in d:
                res += d[pre_sum -k]
            d[pre_sum] += 1
        return res
            

            
