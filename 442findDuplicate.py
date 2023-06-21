# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:05:12 2020

@author: liuga
"""

class Solution(object):
    def findduplicate(self, nums):
        ans = []
        for n in nums:
            if nums[abs(n)-1]<0:
                ans.append(abs(n))
            else:
                nums[abs(n)-1]*=-1
        return ans

#字典统计数目
class Solution(object):
    def findDuplicate(self, nums):
        m = {}
        for i in nums:
            m[i] = m.get(i,0) +1
        ans = []
        for i in m.keys():
            if m[i] == 2:
                ans.append(i)
        return ans

#此解法为主
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return []
        res = []
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] 
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res
