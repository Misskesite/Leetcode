# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:39:44 2020

@author: liuga
"""
#字典映射 时间复杂度O(n) 空间O(n) 最长连续的串
class Solution(object):
    def maximumsize(self, nums, k):
        if not nums:
            return 0
        mp = {}
        summ = 0
        res = 0
        mp[0] = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in mp:
                res = max(res, i- mp[summ - k] + 1)
            if summ not in mp:
                mp[summ] = i+1
        return res
                
            
            
#保存第一个出现该累积和的位置，后面再出现直接跳过，这样算下来就是最长的子数组

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        summ = 0
        summToIndex = {0: -1} 

        for i, num in enumerate(nums):
            summ += num
            target = summ - k
            if target in summToIndex:
                ans = max(ans, i - summToIndex[target])
            if summ not in summToIndex:
                summToIndex[summ] = i

        return ans
