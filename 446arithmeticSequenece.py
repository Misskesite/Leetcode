# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:15:39 2020

@author: liuga
"""

#dp 413是连续数列。此题不要求连续。 因为公差有很多个，所以用字典
#映射表的每一个元素表示公差为key的等差数列的个数 （尾数为A[n]）
import collections

class Solution(object):
    def arithmaticSequence(self, A):
        size = len(A)
        ans = 0
        dp = [collections.dedaultdict(int) for x in range(size)]
        
        for x in range(size):
            for y in range(x):
                delta = A[x]-A[y]
                dp[x][delta] += 1 #考虑只包含A[i] A[j]的数列
                if delta in dp[y]:
                    dp[x][delta] += dp[y][delta] # A[i] 可以加到所有以A[j]结尾的公差为delta的数列后面
                    ans += dp[y][delta]
        return ans


#dp nums = [2,4,6,8,10] 输出7 累加所有的状态， 动态规划子序列问题
#定义二维dp[i][diff] 由于diff的范围很大， 定义dp[i]->dict,含义是在i位置，以diff为公差，且以nums[i]结尾的数列个数 dp[i][diff] -1
#长度为 dp[j][diff]的递增子序列的尾部增加了一个元素 nums[i]，所以以 diff为公差的、且以 nums[i]为结尾元素的等差数列的个数为 dp[i][diff] += dp[j][diff] + 1。
#Increase the number of elements in arithmetic subsequence at i with this dif.
import collections

class Solution(object):
    def arithmaticSequence(self, nums):
        n = len(nums)
        res = 0
        dp = [collections.dedaultdict(int) for x in range(n)]
        
        for i in range(n):
            for j in range(i):
                delta = nums[i]- nums[j]
                dp[i][delta] += dp[j][delta] + 1
                if dp[j][delta]:#if diff in dp[j] #之前的状态值里有同样的 diff 的时候,构成三个？                   
                    res += dp[j][delta]
        return res

'''  [2, 4, 6, 8, 10] 输出7
哈希表
2          前面没有元素，为空
4 {2：1}   公差：前面元素个数
6 {2：2} {4：1}
8 {2：3} {4：1} {6：1}
10 {2：4} {4：2} {6：1} {8：1}

'''
Storing all subsequence ending at i'th index with all possible arithimetic difference at nums[i]
class Solution:
    def numberOfArithmeticSlices(self, A):
        total, n = 0, len(A)
        dp = [Counter() for item in A]
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                total += dp[j][diff]
        return total
