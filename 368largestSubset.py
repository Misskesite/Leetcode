# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:09:08 2020

@author: liuga
"""
#最大递增子序列DP dp[i]表示到数字nums[i]位置最大可整除的子集合的长度 nums[i]能否接在
class Solution(object):
    def largestSubset(self, nums):
        if not nums:
            return []
        
        N = len(nums)
        nums.sort()
        dp = [0]*N
        parent = [0]*N
        
        mx = 0
        mx_idx = -1
        for i in range(N):
            for j in range(i-1,-1,-1):
                if nums[i]% nums[j] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1         #dp[i] = max(dp[i],dp[j]+1)
                    parent[i] = j  #可以用字典存 index之间的映射关系，可以从后向前找.
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_idx = i
            ''' 需要移到前面吗？
            if dp[i] > mx:
                mx = dp[i]
                mx_idx = i
            '''
        res = []
        for k in range(mx + 1): #while len(res) < mx:
            res.append(nums[mx_idx])
            mx_idx = parent[mx_idx]
        return res[::-1] #从后向前找.所以倒过来
            
#倒推获得子集？ 都能被最大数整除的. 较小数对较大数取余一定不为0，那么问题就变成了看较大数能不能整除这个较小数
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        path = [0] * n
        mx = 0
        mx_idx = -1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    path[i] = j
                    
            if mx < dp[mx_idx]:
                mx = dp[i]
                mx_idx = i
                
        ans = []
        while len(ans) < mx:
            ans.append(nums[mx_idx])
            mx_idx = path[mx_idx]
        return ans[::-1]

#此方法空间复杂度更大
class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0: return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)
