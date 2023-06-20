# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:01:07 2020

@author: liuga
"""
#follow up需要O(n*n)实现
class Solution(object):
    def threesumSmall(self, nums, target):
        if not nums:
            return 
        cnt = 0
        k = 2
        n = len(nums)
                
        nums.sort()
        while k < n: #固定k？
            l, r = 0, k-1
            while l < r:
                if nums[l]+ nums[r] +nums[k] >= target:
                    r-=1
                else:
                    cnt += r-l
                    l += 1
                k += 1
            return cnt
                    
#改写 固定最左边的i
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res = 0
        for i in range(len(nums)-1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i]+ nums[l] +nums[r] < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res
