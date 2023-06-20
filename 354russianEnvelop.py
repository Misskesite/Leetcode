# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:45:16 2020

@author: liuga
"""
#类似300(一维) 这个是二维
#时间复杂度O(N*N)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        n = len(envelopes)
        envelopes.sort()
        res = 0
        dp = [0]*n
        for i in range(n):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

#Height needs to be sorted in decreasing order when width is same because there is a constraint that envelope1 will only fit inside envelope2 when both w1 < w2 and h1 < h2
#We sort the array in increasing order of width. And if two widths are same, we need to sort height in decreasing order. We can simple reverse sort the height if two width are equal, to remove duplicacy.
#动态规划+二分查找
from bisect import bisect_left
class Solution2(object):
    def longestIncreaseSequence(self, nums):
        tails = [] #minimal last num of length -(i+1) subsequence
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        retrun len(tails)

    def maxEnvelopes(self, envelopes):
        sortedEnvelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        return self.longestIncreaseSequence(y for x, y in sortedEnvelpes)


    
class Solution:
    def maxEnvelopes(self, A):
        if not A:
            return 0
        A.sort(key = lambda x:(x[0], -x[1]))
        arr = [A[0][1]]
        for i in range(len(A)):
            if A[i][1] > arr[-1]:
                arr.append(A[i][1])
            elif A[i][1] < arr[-1]:
                # 1. 这里维护一个单调递增的arr，所以可以用二分法
                # 2. 二分返回在arr中第一个比A[i][1]大的数
                left, right = 0, len(arr) - 1
                while left < right:
                    mid = (left + right) // 2 
                    if A[i][1] <= arr[mid]:
                        right = mid
                    else:
                        left = mid + 1 
                arr[left] = A[i][1]
        return len(arr)

    
class Solution(object):
    def russianEnvelop(self, envelopes):
        
        def lower_bound(arrays, L, R, x):
            while L < R:
                mid = (L + R) / 2
                if x <= arrays[mid]:
                    R = mid
                else:
                    L = mid + 1
            return L
        
        if not envelopes:
            return 0
        A = sorted(envelopes, lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        n = len(A)
        dp = [1] * n
        g = [0x7fffffff] * (n + 1)
        for i in range(n):
            k = lower_bound(g, 1, n, A[i][1])
            dp[i] = k
            g[k] = A[i][1]
        return max(dp)
    
#首先比较宽度，宽度小的在前，宽度相同时，高度大的在前。二分查找维护一个递增队列，高度作为比较条件   
class Solution2(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # Same as 300. Longest Increasing Subsequence
        ans = 0
        dp = [0] * len(envelopes)

        for _, h in envelopes:
            l = 0
            r = ans
            while l < r:
                m = (l + r) // 2
                if dp[m] >= h:
                    r = m
                else:
                    l = m + 1
            dp[l] = h
            if l == ans:
                ans += 1

          return ans
