# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:14:15 2019

@author: liuga
"""

class Solution(object):
    def summaryrange(self, nums):
        if not nums:
            return []
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums)-1 and nums[j] == nums[j+1] + 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
                #res.append(str(nums[i] + "->" + str(nums[j]))
            i = j +1
        return res



#此解法为主
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0
        while i < len(nums):
            begin = nums[i]
            while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
                i += 1
            end = nums[i]
            if begin == end:
                ans.append(str(begin))
            else:
                ans.append(str(begin) + "->" + str(end))
             i += 1

         return ans
