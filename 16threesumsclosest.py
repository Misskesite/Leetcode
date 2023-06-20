# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:37:20 2019

@author: liuga
"""
#Time O(n*n) SpaceO(1)
class Solution(object):
    def threeSumcloset(self, nums, target):
        nums.sort()
        n = len(nums)
        res = float('inf')
        
        for k in range(n):
            i = k+1
            j = n-1
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            while i < j:
                s = nums[i]+ nums[j]+ nums[k]
                
                if abs(s - target) < abs(res - target):
                    res = s                    
                    
                if s == target:
                    return target                
                    
                elif s > target:
                    j -= 1
                    
                else:
                    i += 1
                
         return res
            
