# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:58:35 2020

@author: liuga
"""
#(0,0)只能在内层递归添加，最外层的递归不能加(不能开头加0)
#时间复杂度O(5**n)
class Solution(object):
    lookup = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
    
    def findStrobogrammatic(self, n):
        return self.dfs(n, n)
    
    def dfs(self, n, k): 
        if k == 0:
            return ['']
        
        if k == 1:
            return ['0', '1', '8']
        
        res = []
        for num in self.dfs(n, k - 2):
            for key, val in self.lookup.items():
                if n != k or key != '0':
                    res.append(key + num + val)
        return res
                    
        ''''
    for num in self.dfs(n, k - 2):
        if k < n:
            res.append('0' + num + '0') #中间递归的过程中，需要有在数字左右两边各加上0的那种情况

        res.append('1' + num + '1')
        res.append('6' + num + '9')
        res.append('8' + num + '8')
        res.append('9' + num + '6')

        ''''



class Solution:
  def findStrobogrammatic(self, n: int) -> List[str]:
    def helper(n: int, k: int) -> List[str]:
      if n == 0:
        return ['']
      if n == 1:
        return ['0', '1', '8']

      ans = []

      for inner in helper(n - 2, k):
        if n < k:
          ans.append('0' + inner + '0')
        ans.append('1' + inner + '1')
        ans.append('6' + inner + '9')
        ans.append('8' + inner + '8')
        ans.append('9' + inner + '6')

      return ans

    return helper(n, n)
