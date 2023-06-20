# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:43:42 2019

@author: liuga
三种情况总结
nums[0] <= target <= nums[i]
               target <= nums[i] < nums[0]
                         nums[i] < nums[0] <= target
如果把握不好边界值，可以在while下面加两行
if(nums[left] == target) return left;
if(nums[right] == target) return right;
"""

class Solution(object):
    def searchRotateArray(self, nums,target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
             mid = left + (right -left)//2
             if nums[mid] == target:
                 return mid
                
             #左边有序
             if nums[mid] > nums[right]:  #456780123   target为0
                 #目标值在左边
                 if target >= nums[left] and target < nums[mid]:
                     right = mid - 1
                 #目标值在右边
                 else:
                     left = mid + 1
                          
                     
             #右边有序                         
             elif nums[mid] < nums[right]: #678012345  target 7 ?
                 #目标值在右边
                 if  target > nums[mid] and target <= nums[right]:
                    left =  mid + 1
                 else:
                #目标值在左边
                    right = mid - 1
             
            
             return -1



class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
      m = (l + r) // 2
      if nums[m] == target:
        return m
      if nums[l] <= nums[m]:  # nums[l..m] are sorted
        if nums[l] <= target < nums[m]:
          r = m - 1
        else:
          l = m + 1
      else:  # nums[m..n - 1] are sorted
        if nums[m] < target <= nums[r]:
          l = m + 1
        else:
          r = m - 1

    return -1
