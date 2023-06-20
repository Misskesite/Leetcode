# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:47:01 2019

@author: liuga
"""

class Solution(object):
    def largetNumber(self, nums):
        def compare(a, b):
            return int(b+a) - int(a+b)
        
        nums = sorted([str(n) for n in nums], cmp = compare) # key = compare ?
        '''
        nums = [str(n) for n in nums]
        nums.sort(reverse = True, cmp = compare)
        if nums[0] == '0':
            return "0"
        else:
            return "".join(nums)
        '''
        ans = ''.join(nums.lstrip('0'))
        
        if ans[0] == '0':
            return '0'
        else:
            return ans
        
