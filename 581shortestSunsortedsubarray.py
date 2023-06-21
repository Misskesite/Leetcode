# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:05:35 2020

@author: liuga
"""

class Solution(object):
    def sortedSubarray(self, nums):
        _len = len(nums)
        _num = sorted(nums)
        if nums == _nums:
            return 0
        
        l = min([i for i in range(_len) if nums[i] != _nums[i])
        r = max([i for i in range(_len) if nums[i] != _nums[i])
        return r-l+1