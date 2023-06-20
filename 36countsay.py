# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:00:12 2019

@author: liuga
"""

class Solution(object):
    
      def countAndsay(self, n):
          result = "1"
          
          for _ in range(1, n):
                result = self.getNext(result)
          return result
          
      def getNext(self,s):
          
          result = []
          start = 0
          
          while start < len(s):
              curr = start+1
              while curr < len(s) and s[start] == s[curr]:
                  curr += 1
                  result.extend(str(curr-start), s[start])
             
                  start = curr
             
                  return result
          
          
class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            new_res, pre, count = '', res[0], 0
            
            for j in range(len(res)):
                if res[j] == pre:
                    count += 1
                else:
                    new_res += str(count) + pre
                    count = 1
                    pre = res[j]
            res = new_res + str(count) + pre
            return res
