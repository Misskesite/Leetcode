# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:06:09 2020

@author: liuga
"""
#其实给 n-1 个数字加1，效果等同于给那个未被选中的数字减1
class Solution(object):
    def minimumMoves(self, nums):
        nums.sort()
        res = 0
        
        for num in nums:
            res += num - nums[0]
        return res
