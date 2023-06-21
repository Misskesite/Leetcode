# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:58:41 2020

@author: liuga
"""
#dp表示从0到i并且以nums[i]结尾的等差数列的个数 时间空间复杂度O(n)
class Solution(object):
    def srithmaticSlices(self, A):
        n = len(A)
        dp = [0]*n
        for i in range(2, n):
            if A[i]- A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
        return sum(dp)
            
#双指针
class Solution2(object):
    def srithmaticSlices(self, A):
        n = len(nums)
        ans = 0
        last_len = 0
        last = 0   #上一个差值
        for i in range(1, n):
            if A[i] - A[i-1] == last:
                last_len += 1
            else:
                last_len = 1

            ans += last_len -1
            last = A[i] - A[i-1]
        return ans


class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    n = len(A)
    if n < 3:
        return 0
    ans = 0
    l = 0

    for i in range(2, n):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            l += 1
            ans += l
      else:
            l = 0

    return ans
