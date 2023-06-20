# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:44:17 2020

@author: liuga
"""

class Solution(object):
    def longestSubsequence(self, nums):
        if not nums:
            return 0
        dp = [0]* len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            tmax = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmax = max(tmax, dp[j] + 1)
            dp[i] = tmax
        return max(dp)
    
                    
#动态规划 第二种方法更好 计算每一个d  [0,1,0,3,2,3] -> 4
class Solution(object):
    def longestSubsequence(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n       #每一个dp[i]初始化为1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
            

#动态规划+二分法 维护列表tails,每个元素的值代表长度为k+1的子序列尾部元素的值
class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0]*len(nums)
        res = 0
        for num in nums:
            i = 0
            j = res    #二分法遍历[0, res)区间，找出nums[k]的大小分界点
            while i < j:
                m = (i+j)//2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tail[i] =  num #替换
            if j == res: #(j没改变？)区间中不存在tails[i] > nums nums是最大的？
                res += 1
        return res
    
    # smallest tailing number of a increasing subsequence of length i + 1
    #计算每个 dp[k] 时，就可以通过二分法遍历 [0,k)区间元素，将此部分复杂度由 O(N)降至 O(logN)
    def lengthOfLIS2(self, nums):
        tails = []
        for num in nums:
            i = bisect_left(tails, num) # binary search the index to insert/update the array.
            if i == len(tails): #没找到？
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)

#用二分查找法在 dp 数组找第一个不小于它的数字，如果这个数字不存在，那么直接在 dp 数组后面加上遍历到的数字，如果存在，则将这个数字更新为当前遍历到的数字
[4, 2， 4， 5， 3， 7 ] -> [2,3,5,7]
