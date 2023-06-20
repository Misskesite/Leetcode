# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:02:52 2019

@author: liuga
"""
#滑动窗口 时间复杂度O(n) 空间复杂度O(1)
class Solution(object):
    def minimumsubarray(self, s, nums):
        l, r = 0 ,0
        summ = 0
        
        n = len(nums)
        res = n +1
        while r  < n: # for r, num in enumerate(nums):
            summ += nums[r]  #向右扩展窗口
            while summ >= s:
                res = min(res, r - l + 1)
                summ -= nums[l]  #向左收缩窗口
                l += 1
            r += 1
        if res != n+1:
            return res
        else:
            return 0
            

#前缀和 + 二分查找 保证了数组中每个元素都为正，所以前缀和一定是递增的，这一点保证了二分的正确性
import bisect
class Solution(object):
    def minimumSubarray(self, s, nums):
        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        sums = [0]*(n+1)
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]

        for i in range(1, n+1):
            target = s + sums[i-1]
            bound = bisect.bisect_left(sums, target)
            if bound != n: # >=n 说明没找到？ 目标和太大
                ans = min(ans, bound - (i-1))
        return 0 if ans == n+1 else ans 
                
