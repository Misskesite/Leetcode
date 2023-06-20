# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:20:17 2019

@author: liuga
"""
class Solution(object):
    def removeDuplicate(self,nums):
        if not nums:
            return 0
        index = 1
        start = 0
        for i in range(1, len(nums)):
             if nums[i] != nums[start]:
                 nums[index] = nums[i]
                 index += 1
                 
                 start = i
                 
        return index

