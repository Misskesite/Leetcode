# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:11:29 2019

@author: liuga
"""
#参考快速排序子过程 partition
class Solution(object):
    def sortColors(self, nums):
        left = i = 0
        right = len(nums)-1
        
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
               
            elif nums[i] == 1:
                 i += 1
                 
            else:
                 nums[i],nums[right] = nums[right], nums[i]
                 right -= 1
                 
                 
                 
               
           
                
              
               
                
                
