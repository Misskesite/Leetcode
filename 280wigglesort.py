# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:57:51 2020

@author: liuga
"""
#nums = [3,5,2,1,6,4] 输出 [3,5,1,6,2,4]
class Solution(object):
    def wigglesort(self, nums):
        n = len(nums)
        for i in range(n-1):
            if i % 2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
#设置一个标
class Solution2(object):
    def wigglesort(self, nums):
        flag = False
        for i in range(len(nums)-1):
            if (flag and nums[i] <= nums[i+1]) or (not flag and nums[i] >= nums[i+1]):
                nums[i],nums[i+1]= nums[i+1],nums[i]
            flag = not flag
