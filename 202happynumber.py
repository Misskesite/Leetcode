# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:14:34 2019

@author: liuga
"""

class Solution(object):
    def happynumber(self,n):
         s = set()
         while n != 1 and n not in s: #不是快乐数会重复出现，有loop
             s.add(n)
             summ = 0
             while n:
                 summ += (n % 10)**2
                 n //= 10
             n = summ
             
         return n == 1
        
  def happynumber(self,n):
     s = set()
        while n != 1:
            s.add(n)
            summ = 0
            while n:
                summ += (n % 10)**2
                n //= 10
            n = summ
            if n in s:
                return False
        return n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        def squaredSum(n: int) -> bool:
            summ = 0
            while n:
                summ += pow(n % 10, 2) #所有的数字的平方和？
                n //= 10
            return summ

        slow = squaredSum(n)
        fast = squaredSum(squaredSum(n))

        while slow != fast:
            slow = squaredSum(slow)
            fast = squaredSum(squaredSum(fast)) #循环到最后相等，然后等于1

        return slow == 1
