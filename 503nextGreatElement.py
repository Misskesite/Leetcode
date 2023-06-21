# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:31:42 2020

@author: liuga
"""
#Input: [1,2,1]  Output: [2,-1,2]
class Solution(object):
    def nextGreatElement(self, nums):
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(n*2): #handle circular
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
    

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n * 2):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if i < n:
                stack.append(i)

        return ans
