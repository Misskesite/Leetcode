# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:28:10 2020

@author: liuga
"""

class Solution(object):
    def arrayPartition(self, nums):
        nums.sort()
        return sum(nums[::2])

#按顺序的每两个就是一对，我们取出每对中的第一个数即为较小值累加起来即可
要最大化每对中的较小值之和，那么肯定是每对中两个数字大小越接近越好，
