# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:43:28 2020

@author: liuga
"""
#12 输出[2,6] [2,2,3] [3,4]  32 输出[2,16] [2，2，8] [2, 2, 2, 4],   [2, 2, 2, 2, 2],  [2, 4, 4],   [4, 8]
class Solution:
  def getFactors(self, n: int) -> List[List[int]]:
    ans = []

    def dfs(n: int, s: int, path: List[int]) -> None:
      if n <= 1:
        if len(path) > 1:
          ans.append(path.copy())
        return

      for i in range(s, n + 1):
        if n % i == 0:
          path.append(i)
          dfs(n // i, i, path)
          path.pop()

    dfs(n, 2, [])  # The smallest factor is 2
    return ans

            
#backtracking
class Solution2(object):
    def getFactor(self, n):
        res = []
        factors = [i for i in range(2, n) if n % i == 0]
        self.dfs(n, 2, [], res, factors)
        return res
    
    def dfs(self, n, factor, path, res, factors):
        if n == 1:
            if len(path) > 0:
                res.append(path[:])
            return 
        
        for i in factors:
            if i >= factor and i <= n and n % i == 0:
                path.append(i)
                self.dfs(n/i, i, path, res, factors)
                path.pop()          
            
    #普通递归 输入12 输出[2, 6], [2, 2, 3],  [3, 4]               
    def getFactor(self, n):
        res = []
        if n <= 1:
            return res
        path = []
        dfs(res, path, n, 2)
        return res
                 

    def dfs(res, path, n, index):  #TLE
        #base case
        if n == 1:
            if len(path)> 1:
                res.append(path)

        for i in (index, n+1):
            if n % i == 0:
                path.append(i)
                dfs(res, path, n/i, i)
                path.pop()

    #改写
    def dfs(self, res, path, n, start):
        
        if len(path) >= 1:
            path.append(n) #加尾巴，之前的 for无法成立
            res.append(path)
            path.pop()

        for i in (index, sqrt(n)+1):
            if n % i == 0:
                path.append(i)
                dfs(res, path, n/i, i)
                path.pop()
#此法为主
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
      if n == 1:
            return []
        res = []
        def dfs(n, start, path):
            if len(path) > 0:
                res.append(path + [n])
                
            for i in range(start, int(sqrt(n))+1): # set upbound to sqrt(x) to ensure n/factor >= factor
                if n % i == 0:
                    dfs(n//i, i, path + [i])
        
        dfs(n, 2, [])
        return res                
        
#方法3
from math import sqrt

class Solution(object):
    def __init__(self):
        self.factors = dict()

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        elif n in self.factors:
            return self.factors[n]

        else:
            res = []
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    residue = n // i
                    res.append([i, residue])
                    for l in self.getFactors(residue):
                        if i <= l[0]:
                            res.append([i] + l)
            return res
