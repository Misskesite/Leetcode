# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:20:58 2020

@author: liuga
"""
from bisect import insort

class Solution(object):
    def medianWindow(self,nums,k):
        ret = []
        tmp = sorted(nums[:k])
        
        def pick(tmp,k):
            if k %2 == 0:
                return float(tmp[k/2])
            else:
                return (tmp[k/2] + tmp[k/2-1])/2.0
            
        ret.append(pick(tmp,k))
        for i in range(k, len(nums)):
            tmp.remove(nums[i-k])
            insort(tmp, nums[i])
            ret.append(pick(tmp,k))
        return ret

import bisect

class Solution2:
    def medianSlidingWindow(self, nums, k):
     
        # base case
        if k == 0: 
            return []
        win = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums)+1):             
            median = (win[k//2] + win[(k-1)//2])/2.0
            ans.append(median)
            if i == len(nums):
                break
            # get the index of the nums[i-k] and then delete it, then insort nums[i]
            index = bisect.bisect_left(win, nums[i-k])
            win.pop(index)
            bisect.insort_left(win, nums[i]) #插入到一个有序数列中，维持其有序
            
        return ans


#nums = [1,3,-1,-3,5,3,6,7]  k= 3
class Solution3:
    def medianSlidingWindow(self, nums, k):
        import bisect
        arr = []
        left = 0
        res = []
        for right in range(len(nums)):
            bisect.insort(arr, nums[right])
            while len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res

#此解法为主
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k == 0: 
            return []
        win = sorted(nums[:k])
        ans = []
        ans.append((win[k//2] + win[(k-1)//2])/2.0)
        for i in range(k, len(nums)):             
           
            # get the index of the nums[i-k] and then delete it, then insort nums[i]
            index = bisect.bisect_left(win, nums[i-k])
            win.pop(index)
            bisect.insort_left(win, nums[i]) #插入到一个有序数列中，维持其有序
            
            median = (win[k//2] + win[(k-1)//2])/2.0
            ans.append(median)
        return ans
