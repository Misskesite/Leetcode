# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:43:06 2020

@author: liuga
"""

class Solution(object):
    def maxOnes(self, nums):
        if len(nums) == sum(nums):
            return sum(nums)
        res = 0
        b = c = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                b, c = c, 0
            res = max(res, b+c+1)
        return res
    
#moving window 此法为主 [1,0,1,1,0] 输出4
class Solution2(object):
    def maxOnes(self, nums):
        k = 1
        left = 0
        zeroCount = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1

                left += 1
            res = max(res, i - left + 1)
        return res
                
        
