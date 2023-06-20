# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:08:00 2019

@author: liuga
"""
#此解法为主
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        nums = [lower-1] + nums + [upper+1]
        pre = lower-1
        res = []
        for n in nums:
            if n == pre + 1:
                pre = n
                continue
            if n == pre + 2:
                res.append(str(pre+1))
                pre = n
                
            elif n > pre +2:
                res.append(str(pre+1) + "->" + str(n-1))
                pre = n
        return res

    
class Solution(object):
    def getmissingRange(self, nums,lower, upper):
        def getRange(lower,upper):
            if lower == upper:
                return "{}".format(lower) #str(left)
            
            else:
                return "{}->{}".format(lower, upper) #str(left) + "->" + str(right)
            
        res = []
        pre = lower -1
        '''
        for num in nums:
            if pre +1 != num:
                res.append(getRange(pre+1, num-1))
            pre = num

        if nums[-1] < upper:
            res.append(getRange(nums[-1]+1, upper))

        '''
        for i in range(len(nums)+1):
            if i == len(nums):
                cur = upper+1
            else:
                cur = nums[i]
                
            if cur - pre >= 2:
                res.append(getRange(pre+1, cur-1))
            
            pre = cur
            
        return res


class Solution:
  def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    def getRange(lo: int, hi: int) -> str:
      if lo == hi:
        return str(lo)
      return str(lo) + '->' + str(hi)

    if not nums:
      return [getRange(lower, upper)]

    ans = []

    if nums[0] > lower:
      ans.append(getRange(lower, nums[0] - 1))

    for prev, curr in zip(nums, nums[1:]):
      if curr > prev + 1:
        ans.append(getRange(prev + 1, curr - 1))

    if nums[-1] < upper:
      ans.append(getRange(nums[-1] + 1, upper))

    return ans

        
#双指针法，用start和end表示可能缺失的区间
class Solution2(object):
    def getmissingRange(self, nums, lower, upper):
        start, end = lower, lower
        res = []
        for i in range(len(nums)): 
            if nums[i] == end:    #没有缺失区间
                start, end = nums[i]+1, nums[i]+1
                
            elif nums[i] > end:   #真的缺失区间
                end = max(end, nums[i] -1)

                if end != start:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start)) #差一个值

                start, end = nums[i]+1, nums[i]+1

        if start < upper:         #处理最后一段
            res.append(str(start) + "->" + str(upper))
            
        elif start == upper:
            res.append(str(start))

        return res
