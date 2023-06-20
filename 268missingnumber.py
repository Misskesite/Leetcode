# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:38:23 2020

@author: liuga
"""
#求出1-n的和 减去数组总和
class Solution(object):
    def missingnumber(self,nums):
        n = len(nums)
        num_sum = sum(nums)
        return n*(n+1)/2-num_sum
