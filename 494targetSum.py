# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:28:13 2020

@author: liuga
"""
#数组中选取子集，达到某一目标 第 i-1 个数字且和为j的情况总数
import collections
class Solution(object):
    def targetSum(self,nums,s):
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n+1)] #用一个数组的哈希表
        
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i+1][sum+num] += cnt
                dp[i+1][sum-num] += cnt
        return dp[n][s]

#省空间写法 只用一个哈希表，遍历数组每个数字时候新建一个哈希表，在遍历原哈希表的时更新新建的哈希表。最后把新建的哈希表赋值给原哈希表
    def targetSum(self, nums):
        dp = collections.defaultdict(int)
        dp[0] = 1
        for num in nums:
            t = collections.defaultdict(int)
            for summ, cnt  in dp.items():
                t[summ + num] += cnt
                t[summ - num] += cnt
            dp = t
        return dp[s]

#dp[i][j] = dp[i-1][j - nums[i]] + dp[i-1][j + nums[i]]
#dp[i][j]表示i个数字选取元素，且和为j的情况总数 定义二维数组dp，其中dp[i][j] 表示在数组nums 的前 i个数中选取元素，使得这些元素之和等于 j的方案数
#假设数组nums 的长度为 n，则最终答案为dp[n][neg]

class Solution2(object):
    def targetSumways(self, nums, S):
        
        def subsetSums(target):
            dp = [0]*(target+1)
            dp[0] = 1
            for i in range(len(nums)):
                for j in range(target, nums[i]-1, -1):
                    dp[j] += dp[j-nums[i]]
            return dp[-1]
        
        if sum(nums) < S or (S + sum(nums))%2 >0 :
            return 0
        return subsetSums(S + sum(nums))/2


#简化第二种方法 #数组和为sum，target就是数组的若干+变成—，因此将负的地方消去，取+的地方翻倍 sum+target必须为偶数 需要取正的和为它的一半
#背包问题？ 组中选取出部分元素，给它们加上+号，这些元素和为S + sum(nums))/2。 类似于518 组合？
class Solution3(object):
    def targetSumways(self, nums, S):
        if sum(nums) < S or (S + sum(nums))%2 >0 :
            return 0
        
        target = int((S + sum(nums))/2)
                
        dp = [0]*(target+1) #dp[i] := # Of ways to sum to i by nums so far
        dp[0] = 1
        for num in nums: #从前1个数字凑，前2个凑(取这个， 不取)
            for j in range(target, num-1, -1): #j >= num 问题：逆向循环？ 0-1背包必须逆序，完全背包可以重复选择，所以正序
                dp[j] += dp[j-num] #可选择当前数字num，也可不选【两种方式之和】
        return dp[-1]
        
        
#之所以需要从后向前更新状态，是因为我们需要使用到之前的状态。如果从前向后更新，原先的状态F[i-1,v]会被新状态F[i,v]覆盖掉，导致在后面需要使用F[i-1,v]时无法找到，从而出现计算错误。
    
组中选取出部分元素，给它们加上+号，这些元素和为S + sum(nums))/2
**Input:** nums is [1, 1, 1, 1, 1], S is 3. 
**Output:** 5
**Explanation:** 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
