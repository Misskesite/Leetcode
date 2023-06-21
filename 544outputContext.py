# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:49:05 2020

@author: liuga
"""
#递归 强队匹配弱队(比如季后赛)
class Solution(object):
    def outputContext(self, groups):
        n = len(groups)
        if n == 1:
            return groups[0]
        ngroups = []
        for i in range(n/2):
            ngroups.append('(' + groups[i] + ',' + groups[n-i-1] + ')')
        return self.outputContext(ngroups)
    
    def findMatch(self, n):
        return self.outputContext(map(str, range(1,n+1))) #生成1-n的string
        

#Iterative
class Solution:
  def findContestMatch(self, n: int) -> str:
      matches = [str(i + 1) for i in range(n)]

      while n > 1:
          for i in range(n // 2):
              matches[i] = '(' + matches[i] + ',' + matches[n - 1 - i] + ')'
          n //= 2

      return matches[0]
