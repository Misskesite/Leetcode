# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:26:01 2019

@author: liuga
"""
#环形的，选择偷第一个，或者最后一个
class Solution(object):
    def houserobery(self, nums):
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        return max(self.rob(nums[0:n-1]), self.rob(nums[1:n]) )

        def rob(self, nums):
            n = len(nums)
            
            if not nums:
                return 0
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0],nums[1])
            
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]

