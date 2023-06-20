# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:31:19 2019

@author: liuga
"""

class Solution(object):
    def maximumSubarray(self, nums):
        if not nums:
            return 0
        n = len(nums)
        current = nums[0]
        m = current
        
        for i in range(1, n):
            if current < 0:
               current = 0
                
            current += nums[i]
           
            m = max(m, current)
               
        return m


#DP 数组的含义是以dp[i]为结尾的最大数组的和
#状态转移方程 dp[i] = dp[i-1] + nums[i] or dp[i] = nums[i] 

class Solution(object):
    def maximumSubarray(self, nums):
        n = len(nums)
        dp = [0]*(n)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            res = max(res, dp[i])

        return res # max(dp)?
            
        
