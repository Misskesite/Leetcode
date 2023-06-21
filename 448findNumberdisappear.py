# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:38:04 2020

@author: liuga
"""

class Solution(object):
    def findnumber(self, nums):
        for n in nums:
            nums[abs[n]-1] = - nums[abs[n]-1] #表示为负数，说明被占了。
        return [i+1 for i, n in enumerate(nums) if n > 0] #正数说明没被占
