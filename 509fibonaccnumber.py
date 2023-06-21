# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:58:18 2020

@author: liuga
"""

class Solution(object):
    def fib(self,n):
        array = [i for i in range(n+1)]
        return self.fibola(array,n)
    
    def fibola(self,array,n):
        if n <= 1:
            return n
        array[n] = self.fibola(array,n-1) + array[n-2]
        return array[n]
        
class Solution:
  def fib(self, N: int) -> int:
    if N < 2:
      return N

    dp = [0, 0, 1]

    for i in range(2, N + 1):
      dp[0] = dp[1]
      dp[1] = dp[2]
      dp[2] = dp[0] + dp[1]

    return dp[2]
