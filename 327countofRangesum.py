# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:42:18 2020

@author: liuga
"""
#nums = [-2,5,-1], lower = -2, upper = 2 答案: 3个区间 [0,0] [2,2] [0,2]
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        size = len(nums)
        sums = [0]*(size+1)
        for x in range(1, size+1):
            sums[x] = nums[x-1] + sums[x-1]
        INF = max(sums)
        
        #归并排序？
        def mergeSort(lo, hi):
            if lo == hi:
                return 0
            mi = (lo + hi)/2
            cnt = mergeSort(lo,mi) + mergeSort(mi+1, hi)
            x = y = lo
            for i in range(mi+1, hi+1):
                while x <= mi and sums[i]- sums[x] >= lower:
                    x+=1
                while y <= mi and sums[i] - sums[y] > upper:
                    y+=1
                cnt += x-y
            part = sums[lo:hi+1]
        
            l, h = lo,mi+1
            for i in range(lo, hi+1):
                x = part[l-lo] if l <= mi else INF
                y = part[h-lo] if h <= hi else INF
                if x < y:
                    l+=1
                else:
                    h+=1
                sum[i] =  min(x,y)
            return cnt
        return mergeSort(0,size)
                
#此解法为主
#朴素解法 二分加速   lower <= sum[i] - sum[j] <= upper 推出  sum[i] - upper =< sum[j] <= sum[i] - lower
class Solution(object): 
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        presum = [0 for _ in range(n+1)]

        for i in range(n):
            presum[i+1] = presum[i] + nums[i]

        res = 0
        preWindow = []
        for i, p in enumerate(presum): #从presum 0开始
            L = bisect_left(preWindow, p - upper)
            R = bisect_right(preWindow, p - lower)
            res += R - L
            bisect.insort(preWindow, p)
        return res

#二分法改进  O(n*logn)
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        res = 0
        pre = [0]
        cur = 0
        for n in nums:
            cur += n
            res += bisect.bisect_right(pre, cur -lower) - bisect.bisect_left(pre, cur - upper)
            bisect.insort(pre, cur)
        return res    
    


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.res = 0
        n = len(nums)
        prefixsum = [0 for _ in range(n + 1)]
        for i in range(n):
            prefixsum[i + 1] = prefixsum[i] + nums[i]

        self.mergesort(prefixsum, 0, len(prefixsum) - 1)
        return self.res

    #2个点在(left,right]中 (1):2个点在前半段中，(left, mid]递归处理 (2) 两个点后半段(mid+1, right] 递归处理
    #一个前半段，一个后半段，前半段一个点，后半段顺序不影响，反之亦然。因为是前缀和，位置顺序只影响被计算的先后顺序，递增排序后不影响。 代码中的增序处理，每层可以在O(n)实现，总共logn层 O(nlogn)
    def mergesort(self, nums: List[int], L: int, R: int) -> None:
        if L < R:
            mid = L + (R - L) // 2
            self.mergesort(nums, L, mid)
            self.mergesort(nums, mid + 1, R)
            self.merge(nums, L, mid, R)
    #merge O(n), sort O(logn)   
    def merge(self, nums: List[int], L: int, mid: int, R: int) -> None:
        i, j = L, mid + 1
        tmp = []
        while i <= mid and j <= R:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        #########################################
        ## 套用标准的归并排序   本题需要单独计算的地方
        ii, jj, kk = L, mid + 1, mid + 1
        while ii <= mid:
            while jj <= R and nums[jj] - nums[ii] < self.lower:
                jj += 1
            while kk <= R and nums[kk] - nums[ii] <= self.upper:
                kk += 1
            self.res += (kk - jj)
            ii += 1
        #########################################
        if i <= mid:
            tmp += nums[i: mid + 1]
        if j <= R:
            tmp += nums[j: R + 1]
        for i in range(len(tmp)):
            nums[L + i] = tmp[i]
                
        
