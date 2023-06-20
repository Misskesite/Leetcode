# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:41:03 2020

@author: liuga
"""
#选取元素的顺序 排列 dp[i]目标和为i的解的个数
class Solution(object):
    def combinationSum(self, nums, target):
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp.pop() #DP[TARGET]

''''    dp[target] = sum(DP(target - num) for num in nums)
nums = [1,2,3] target = 4
(1,1,1,1)
(1,1,2)
(1,2,1)
(1,3)
(2,1,1)
(2,2)
(3,1)
当计算 dp[3] 的时候，3可以拆分为 1+x，而x即为 dp[2]，3也可以拆分为 2+x，此时x为 dp[1]，
3同样可以拆为 3+x，此时x为 dp[0]，把所有的情况加起来就是组成3的所有情况了

背包问题
（1） 组合问题 dp[i] += dp[i-num]
377. 组合总和 Ⅳ
494. 目标和
518. 零钱兑换 II
(2) True False问题 dp[i] = dp[i] or dp[i-num]
139. 单词拆分
416. 分割等和子集
(3) 最大最小问题   dp[i] = min/max(dp[i], dp[i-num] +1)
474. 一和零
322. 零钱兑换

背包问题步骤
1 是否背包问题，三种中的哪一种？ 给定一个target(数字或者字符串)，给定一个数组nums(数字字符串)，能否使用nums中的元素做各种排列组合得到target
 0-1背包，数组里的元素不能重复利用，nums放在外循环，target放在内循环，内循环倒序
 for num in nums:
     for i in range(target, nums-1, -1):

 完全背包，可以重复利用，内循环正序
 for num in nums:
     for i in range(nums, target+1):
 
 
2 0-1背包还是完全背包，即nums数组中的元素是否可以重复使用
3 如果是组合问题，是否要考虑元素之间的顺序。考虑顺序，不考虑顺序，解法不同
  target放在外循环，nums放在内循环
  for i in range(1, target+1):
      for num in nums:
