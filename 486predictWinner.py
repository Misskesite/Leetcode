# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:23:06 2020

@author: liuga
"""
#零和博弈问题， 类似问题1406
class Solution(object):
    def predictWinner(self, nums):
        
        dp = {}

        def find(i, j):
            if i == j:
                return nums[i]
            if (i, j) not in dp:
                
                dp[i,j] = max(nums[i]-find(i+1, j), nums[j]-find(i, j-1))
            return dp[i,j]

        return find(0, len(nums)-1) >= 0
    
    
#dp[i][j]作为先手，从[i,j]获得的相对分数？ 
#状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1: 
            return True
        dp = [[0]*N for _ in range(N)]
        
        for i in range(N - 1, -1, -1): #i <= j
            for j in range(i , N):
                if i == j:
                    dp[i][i] = nums[i]
                else:
                    dp[i][j] = max(nums[i]- dp[i+1][j], nums[j] - dp[i][j-1])
        
        return dp[0][N-1] >= 0

#O(n)空间 下面的简化
    dp = [0]*n
    for i, num in enumerate(nums):
            dp[i] = num
    for i in range(n-2, -1, -1): #逆序？
        for j in range(i+1, n):
            dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
    return dp[n-1] >= 0
    
#dp从底层开始(只有2个数字时?)自底向上
class Solution3:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        for i in range(n - 2, -1, -1): #[i,j] [n-2:n-1]两个元素开始 -> [n-3:n-2] [n-3:n-1]
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]) #分别选头尾元素 left number, right number
        return dp[0][n - 1] >= 0

