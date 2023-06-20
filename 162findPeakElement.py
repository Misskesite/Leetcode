# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:30:32 2019

@author: liuga
"""
#二分搜索
class Solution(object):
    def findPeakelement(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[mid+1]: #判断上坡还是下坡
                left = mid +1
            else:
                right = mid
        return left
            
class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if nums[m] >= nums[m + 1]:
        r = m
      else:
        l = m + 1

    return l
'''
确定二分查找折半后中间那个元素后，和紧跟的那个元素比较下大小，
如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了
