# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:40:51 2020

@author: liuga
"""
#DP一般可以用记忆化搜索改出来
#dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j], i+1<= k <= j-1)
class Solution(object):
    def maxcoins(self, nums):
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        dp = [[0]*(n+2) for _ in range(n+2)]
        for i in range(1, n+1): #区间长度
            for l in range(1, n-i+2): 
                r = l+i-1
                for k in range(l, r+1):
                    dp[l][r]= max(dp[l][r], dp[l][k-1] + nums[l-1]*nums[k]*nums[r+1] + dp[k+1][r]) #闭区间
        return dp[1][n]

    #开区间，以此解法为主 i和j就是两个「状态」，最后戳破的那个气球k就是「选择」
    #i dp[i][k]  k  dp[k][j]  j
    def maxcoins2(self, nums)
        
        nums = [1] + nums + [1]
        n = len(nums)
        
        dp = [[0]*(n) for _ in range(n)]

        for i in range(n-2, -1, -1):    #从下往上  
            for j in range(i+2, n):     #从左往右  
                for k in range(i+1, j):   #最后戳破的气球 k取(i,j)开区间里面的值
                    dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])  #开区间

        return dp[0][n-1]

    #类似上面，对角线斜向上
    class Solution:
        def maxCoins(self, nums: List[int]) -> int:
            nums = [1] + nums + [1]
            N = len(nums)
            dp = [[0] * N for _ in range(N)] 
            for l in range(N):
                for i in range(N-l):
                    j = i + l 
                    for k in range(i+1,j):
                        dp[i][j] = max(dp[i][j], dp[i][k]+ dp[k][j]+ nums[i]*nums[k]*nums[j])
            return dp[0][-1]
    
#动态规划子问题必须独立，i,j是两个状态，k是个选择
class SOlution2(object):
    def maxcoins(self, nums):
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        dp = [[0]*(n+2) for _ in range(n+2)]
        return self.dfs(nums, dp, 1, n)

    def dfs(self, nums, dp, i, j):
        if i > j:
            return 0

        if dp[i][j] > 0:
            return dp[i][j]

        if i == j:
            return nums[i-1]*nums[i]*nums[i+1]

        res = 0
        for k in range(i, j+1):
            res = max(res, self.dfs(nums, dp, i ,k-1) + nums[i-1]*nums[k]*nums[j+1] + self.dfs(nums, dp, k+1, j))

        dp[i][j] = res
        return dp[i][j]
    
#dp[i,j] represent the maximum coins collected by bursting balloons[(i+1)...(j-1)]
