# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:14:35 2019

@author: liuga
"""
#双指针，时间复杂度O(n)
class Solution(object):
    def twosums(self, nums,target):
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            elif nums[l] + nums[r] > target:
                r -= 1 #排除一列
            else:
                l += 1 #排除了一行

        return [-1, -1]
                
