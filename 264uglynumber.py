# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:44:01 2020

@author: liuga
"""

class Solution(object):
    def uglynumber(self,n):
        if not n:
            return 0
        dp = [0]*n
        index2, index3,index5 =0,0,0
        for i in range(1,n):
            dp[i]= min(2*dp[index2], 3*dp[index3], 5*dp[index5])
            if dp[i]==2* dp[index2]:
                index2+=1
            if dp[i]==3* dp[index3]:
                index3+=1
            if dp[i]==5* dp[index5]:
                index5+=1
        return dp[n-1]

class Solution:
  def nthUglyNumber(self, n: int) -> int:
      nums = [1]
      i2 = 0
      i3 = 0
      i5 = 0

      while len(nums) < n:
          next2 = nums[i2] * 2
          next3 = nums[i3] * 3
          next5 = nums[i5] * 5
          nextn = min(next2, next3, next5)
          if nextn == next2:
              i2 += 1
          if nextn == next3:
              i3 += 1
          if nextn == next5:
              i5 += 1
          nums.append(nextn)

    return nums[-1]

#堆 暴力？
import heapq
class Solution(object):
    def uglyNumber(self, n):
        nums = [2,3,5]
        pq = [1]
        seen = {1}

        for i in range(1, n+1):
            x = heapq.heappop(pq)
            if i == n:
                return x
            for num in nums:
                t = num*x
                if t not in seen:
                    seen.add(t)
                    heapq.heappush(pq, t)
         return -1

        

        
