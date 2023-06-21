# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:05:01 2020

@author: liuga
"""
#画一个 len 行，target + 1 列的表格。这里 len 是物品的个数，target 是背包的容量。len 行表示一个一个物品考虑，target + 1多出来的那 1 列，表示背包容量从 0 开始考虑。很多时候，我们需要考虑这个容量为 0 的数值。
#前i个数字的，选取一些正整数，每个用一次，和能不能构成j，选不选nums[i]的问题， 背包问题
#dp[i][j] = dp[i-1][j] || dp[i-1][j- nums[i]] 不选或者选

#另一种方法: use dictionary to caculate all the sums
class Solution(object):
    def partitionSum(self, nums):
        '''
        sums = 0
        
        sums = sum(nums)
        if sums % 2 == 1: 
            return False
        n = len(nums)
        target = sums/2
        j = target
        #dp[j]表示从数组中任意取数字的和能不能构成j,j从后面向前面更新(变小)
        dp = [False]*(target+1)
        for num in nums:
            while j >= num:     #相等说明正好等于背包容积
                dp[j] = dp[j] or dp[j-num]  # or dp[j] |= dp[j-num] 不选num， 选num
                j-=1
        return dp[target]
        '''

        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]

#时间复杂度O(n*target)
#边界条件:(1)如果不选取任何正整数，则被选取的正整数等于0。因此对于所有 0 <= i < n，都有dp[i][0]=true。(2) i =0 时，只有一个正整数nums[0]可以选取 dp[0][nums[0]]= Ture

class Solution(object):
    def partitionSum(self, nums):
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target]


        ''''
        for i in range(1, n+1):
            #if dp[target]== 1: return True 已经发现目标，提前退出循环节省时间
            for j in range(target):
                if j - nums[i-1] >= 0 and dp[j-nums[i-1]]:
                    dp[j] = 1
        return dp[-1]
        ''''

dp[i][j]表示从nums[0]..nums[i]这些数中，取若干个数(可以为0)，能否构成j，dp[n-1][target]为所求
dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]] (j >= nums[i])
dp[i][0] = True
dp[0][nums[0]] = True
使用一维数组：
dp[j] = dp[j] | dp[j - nums[i]]     
       
    
class Solution3(object):
    def partition3(self, nums):
        if not nums:
            return
        sums = 0
        
        sums = sum(nums)
        if sums % 2 == 1: 
            return False
        nums.sort(reverse=True) 
        target = sum/2
        if target < nums[0]:
            return False
        return self.dfs(nums, target)
    
    def dfs(self, nums, target):
        if target == 0:
            return True
        if target <0 :
            return False
        for i in range(len(nums)):
            if self.dfs(nums[i+1:], target - nums[i]):
                return True
        return False
    
            
