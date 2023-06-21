# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:45:21 2020

@author: liuga
"""
#时间复杂度O(n) 空间复杂度O(1)
class Solution(object):
    def singleElement(self, nums):
        
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

#如果mid偶数，比较nums[mid]和nums[mid+1]是否相等，如果mid是奇数，比较nums[mid-1]和nums[mid]
#异或，1异或任何数字 -> 数字取反。任何数异或自己，把自己置为0
class Solution(object):
    def singleDuplicate(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
                
        
