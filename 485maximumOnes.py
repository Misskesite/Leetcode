# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:05:13 2020

@author: liuga
"""

class Solution(object):
    def maximumOnes(self, nums):
        index = -1
        n = len(nums)
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                index = i #更新，记录最后一个0
            else:
                res = max(res, i-index)
        return res


class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    ans = 0
    summ = 0

    for num in nums:
      if num == 0:
        summ = 0
      else:
        summ += num
        ans = max(ans, summ)

    return ans
