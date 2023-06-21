# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:35:22 2020

@author: liuga
"""
import math

class Solution(object):
    def goodBase(self, n):
        n = int(n)
        for m in range(int(math.log(n,2)), 1, -1):
            k = int(n**(1.0/m))
            if sum(k**i for i in range(m+1)) == n:
                return str(k)
        return str(n-1) #找不到就返回第二小的(n-1)进制， 11

#Time: O(logn*logn)
class Solution:
  def smallestGoodBase(self, n: str) -> str:
    n = int(n)

    for m in range(int(math.log(n, 2)), 1, -1):
      k = int(n**m**-1)
      if (k**(m + 1) - 1) // (k - 1) == n:
        return str(k)

    return str(n - 1)
            
''' k >= 2
放缩+ 二项式
e.g 11111...1
(1) k^0 + k^1 +...+ k^m = n
(2) (k+1)^m
所以k^m < n

(k+1)^m > n > k^m   ->    k+1 > n^(-m) > k

n = 13
3^2 < 13 < 4^2

m的范围[1,60]
