# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:33:05 2019

@author: liuga
"""
#找到返回第 1个大于等于目标元素的下标
class Solution(object):
    def searchInsert(self, nums, target):
        N = len(nums)
        left, right = 0, N-1
        while left <= right:
         
           mid = left + (right - left)/2 
           if nums[mid] == target:
              return mid
        
           elif nums[mid] < target:
              left = mid + 1
            
           else:
              right = mid -1
             
        return left

#写成while left < right 退出循环时 left == right, 好处是不用判断返回l ,r
#分成 [left..mid] 和 [mid + 1..right]，分别对应 right = mid 和 left = mid + 1；mid = (left + right) / 2
#分成 [left..mid - 1] 和 [mid..right]，分别对应 right = mid - 1 和 left = mid，这里mid =(left + right + 1) / 2 否则死循环
class Solution(object):
    def searchInsert(self, nums, target):
        N = len(nums)
        left, right = 0, N
        while left < right:
         
           mid = left + (right - left)/2 
           if nums[mid] == target: 
              return mid
        
           elif nums[mid] < target: #下一轮的区间是[mid+1, right]
              left = mid + 1
            
           else:
              right = mid           #下一轮搜索区间是[left, mid]
             
        return left


        
