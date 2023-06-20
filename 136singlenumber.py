# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:55:28 2019

@author: liuga
"""
#所有值异或(相同的值异或为0) 0^n = n
class Solution(object):
    def singleNum(self, nums):
        result = nums[0]
        for i in nums[1:]:
            result ^= nums[i]
        return result
    
    
import collections
class Solution2(object):
    def singleNum(self, nums):
        count = collections.Counter(nums)
        return count.most_common()[-1][0]
