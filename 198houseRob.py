# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:29:49 2019

@author: liuga
"""
#dp 此法为主
class Solution(object):
    def houseRobber(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
    
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            
        return dp[n-1]

#滚动数组 空间复杂度O(1)
    def houseRobber(self, nums):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]
        #抢当前房子， 不抢当前房子
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first+ nums[i], second)

        return second


def rob(self, nums: List[int]) -> int:
    prev = 0
    cur = 0
    
    # 每次循环，计算“偷到当前房子为止的最大金额”
    for num in nums:
        # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
        # dp[k] = max{ dp[k-1], dp[k-2] + num }
        prev, cur = cur, max(cur, prev + num)
        # 循环结束时，cur 表示 dp[k]，prev 表示 dp[k-1]

    return cur
