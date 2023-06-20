# -*- coding: utf-8 -*-
"""
Created on Fri August 27 15:53:48 2019

@author: liuga
"""

class Solution(object):
      def twoSums(self, nums, target):
          dicts = {}
           
          for index , v in enumerate(nums):
              dicts[index] = v
                     
          for k , v in enumerate(nums):
              if target -v in dicts:
                  return [dicts.get(target-v),k]
               
               
