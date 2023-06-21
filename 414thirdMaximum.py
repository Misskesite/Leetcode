# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:45:04 2020

@author: liuga
"""

class Solution(object):
    def thirdMax(self, nums):
        num_set = set(nums)
        if len(num_set) < 3:
            return max(num_set)
        num_set.remove(max(num_set))
        num_set.remove(max(num_set))
        res = max(num_set)
        return res


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        diff = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                diff += 1
                if diff == 3:  # 此时 nums[i] 就是第三大的数
                    return nums[i]
        return nums[0]
