# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:59:35 2019

@author: liuga
"""
#相对153 有重复数字 [4,5,6,7,0,1,4] [2,2,2,0,1] nums拆分成2个排序数组
#最坏的情况下，比如数组所有元素都相同，时间复杂度降低到o(n)
class Solution(object):
    def findMin(self, nums):
        l, r = 0 , len(nums)-1
        while l < r :
            m = (l + r)//2
            if nums[m] > nums[r]: #mid在第一个排序数组中 i 满徐 mid <i<=right,所以执行l = mid + 1
                l = m + 1
            elif nums[m] < nums[r]:#mid在第二个排序数组中，i满足 left<i<= mid，因此执行right = mid
                r = m
            else:
                r = r - 1 #关键点，相等，右边左移一位 nums[r] == nums[mid]
        return nums[l]
    
                
#二段性，分界线之前或者之后有一段满足条件，有一段不满足条件
class Solution2(object):
    def findMin(self, nums):
        n = len(nums)
        l = 0
        r = n -1
        while l < r and nums[0] == nums[r]: #恢复二段性
            r -= 1

        while l < r:
            mid = (l + r + 1)//2
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid -1
        return nums[r+1] if r + 1 < n else nums[0]
