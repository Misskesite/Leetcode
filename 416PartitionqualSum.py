# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:14:00 2019

@author: liuga
"""
#DFS加剪枝
class Solution(object):
    def partitionSum(self, nums):
        n = len(nums)
        _sum = sum(nums)
        target = _sum/2  
        mod = _sum%2
        if max(nums) > target or mod != 0:
            return False
        
        return self.dfs(nums, n-1, target)
    
    def dfs(self, nums, i, target):
        if target == 0:
            return True
        #剪枝条，否则容易超时
        if target < 0 or i < 0 or target < nums[i]:
            return False
        return self.dfs(nums, i-1, target - nums[i]) or self.dfs(nums, i-1, target)
        
#背包问题
"""
dp[i][j]表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和恰好等于j。
状态转移 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

背包状态从二维降为一维， 二维填表时，当前行总是参考了它上面一行 「头顶上」 那个位置和「左上角」某个位置的值
一维从后往前
"""
class Solution2(object):
    def partitionSum(self, nums):
        s = 0
        n = len(nums)
        s = sum(nums)

        if s % 2 == 1:
            return False

        target = s//2
        
        #数组dp[i]记录和为i的子数组是否存在，数组数字的和当做dp的一个状态
        dp = [False for _ in range(target+1)]
        dp[0] = True

        for i in range(1, n+1):
            for j in range(target, 0, -1):  #一定要从后向前更新
                if j >= nums[i-1]:
                    dp[j] = dp[j] || dp[j-nums[i-1]]
                    
                #if j >= nums[i-1] and dp[j- nums[i-1]]:
                #   dp[j] = 1
                    
        return dp[target]
        


class Solution3(object):
    def partitionSums(self, nums):
        sums = sum(nums)
        target = sums/2
        if sums %2 == 1:
            return False
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num] #取，不取
        return dp[target]
