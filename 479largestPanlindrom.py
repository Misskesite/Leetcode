# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:15:04 2020

@author: liuga
"""
#n=2 uppperbound = 99 lowbound = 10 手动生成(99*99 = 9801) 取前部分 9889，判断是否回文
class Solution(object):
    def largestPanlindrom(self, n):
        upper = 10**n -1
        lower = upper//10
        for i in range(upper, lower, -1):
            l = int(str(i)+ str(i)[::-1])
            j = upper
            while j*j > l:
                if l % j == 0:
                    return l%1337
                j -= 1
        return 9
    #n = 1, return 9


class Solution:
  def largestPalindrome(self, n: int) -> int:
    if n == 1:
      return 9

    kMod = 1337
    upper = pow(10, n) - 1
    lower = pow(10, n - 1) - 1

    for i in range(upper, lower, -1):
      cand = int(str(i) + str(i)[::-1])
      j = upper
      while j * j >= cand:
        if cand % j == 0:
          return cand % kMod
        j -= 1
