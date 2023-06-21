# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:49:45 2020

@author: liuga
"""
# [2,4,3,5,1] 输出3  （满足i < j 且 nums[i] > 2*nums[j]）
class Solution(object):
    def reversePair(self, nums):
        num2 = [n*2 for n in nums]
        dmap = {v: k+1 for k, v in enumerate(sorted(set(nums+num2)))}
        ft = FenwichTree(len(dmap))
        ans = 0
        for n in num2[::-1]:
            ans += ft.sum(dmap[n/2]-1)
            ft.add(dmap[n],1)
        return ans

class FenwichTree(object):
     def _init_(self,n):
         self.n =n
         self.sum = [0]*(n+1)
         
     def add(self,x, val):
         while x <= self.n:
             self.num[x] += val
             x+= self.lowbit(x)
             
     def lowbit(self,x):
         return x & -x
    
     def sum(self,x):
         res = 0
         while x >0:
             res += self.nums[x]

#二分查找 类似于315(右侧有多少个比自己小的元素) [1,3,2,3,1] 输出2
class Solution(object):
    def reversePairs(self, nums):
        tb , res = [] , 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res
#改写
import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb , res = [] , 0
        for n in reversed(nums):
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            bisect.insort(tb, n2)
        return res

    


             
#类似327, 归并排序 这里需要维护两个升序的序列。不断二分直到不能二分，就形成了有序序列。然后不断合并。
#每次2分，有一段不用考察，时间复杂度O(nlogn) 统计翻转时机: 得到左右序列之后，合并左右序列之前
class Solution3:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergesort(nums, 0, len(nums) - 1)
        return self.cnt

    def mergesort(self, nums: List[int], L: int, R: int) -> None:
        if L < R:
            mid = L + (R - L) // 2
            self.mergesort(nums, L, mid)
            self.mergesort(nums, mid + 1, R)
            self.merge(nums, L, mid, R)
    
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
        ######################## 借助归并排序  本题的特殊计算
        ii, jj = L, mid + 1
        while ii <= mid and jj <= R:
            if nums[ii] <= 2 * nums[jj]:
                ii += 1
            else:
                self.cnt += (mid - ii + 1)
                jj += 1
        ########################
        if i <= mid:
            tmp += nums[i: mid + 1]
        if j <= R:
            tmp += nums[j: R + 1]
        for i in range(len(tmp)):
            nums[L + i] = tmp[i]

    
        
    def reversePairs(self, nums):
        res = 0
        sorted_values = []
        for j in range(len(nums)):
            i = bisect.bisect_right(sorted_values, 2 * nums[j])
            res += (j - i)
            bisect.insort(sorted_values, nums[j])
        return res
