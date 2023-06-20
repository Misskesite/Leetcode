# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:38:24 2019

@author: liuga
"""

class Solution(object):
     def removeElement(self, nums, var):
          N = len(nums)
          l, r = 0, N-1
          while l <= r:
              if nums[l] == var:
                 nums[l] = nums[r]
                 r -=1
              else:  
                 l +=1
                
          return l


class Solution(object):
     def removeElement(self, nums, val):
          a = 0
          b = 0
          
          while a < len(nums):
               if nums[a] != val:
                    nums[b] = nums[a]
                    b += 1
               a += 1
          return b
