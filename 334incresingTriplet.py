# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:32:46 2020

@author: liuga
"""
#遍历的时候保存已经看到的最小值和次小值，然后再发现比这两个值大的的第3小的值存在的时候，就说明有长度为3的子序列了
class Solution(object):    
    def increasingTriplet(self, nums):
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    first = math.inf
    second = math.inf

    for num in nums:
      if num <= first:
        first = num
      elif num <= second:  # First < num <= second
        second = num
      else:
        return True  # First < second < num (third)

    return False

     def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        f = [float('inf')]*n
        b = [float('-inf')]*n

        for i in range(1, n):
            f[i] = min(f[i - 1], nums[i-1])
      
        for i in range(n - 2, -1, -1):
            b[i] = max(b[i + 1], nums[i+1])

        for i in range(1,n-1):
            if f[i] < nums[i] and nums[i] < b[i]:
                return True
        return False
