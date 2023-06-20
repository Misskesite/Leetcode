# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:39:01 2019

@author: liuga
"""

class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        result = []
        n = len(nums)
        i = 0
        
        while i < n - 2:
            l = i + 1
            r = n - 1
            while l < r:
                s = [nums[i], nums[l], nums[r]]
                if sum(s) == 0:
                    result.append(s)
                    l += 1
                    r -= 1
                    
                    # Ignore repeat numbers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    
                elif sum(s) > 0:
                    r -= 1
                    
                else:
                    l += 1
            i += 1
            #ignore repeated numbers
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
         return result



class Solution(object):
    def threeSums(self, nums):
        n = len(nums)
        res = []
        if not nums or n < 3:
            return []

        nums.sort()

        for i in range(n-2):
            
            #ignore repeat nums
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l = l +1
                    while l < r and nums[r] == nums[r-1]:
                        r = r-1
                    l = l+1
                    r = r-1
                elif s > 0:
                    r = r-1
                else:
                    l = l+1

        return res
                
            
