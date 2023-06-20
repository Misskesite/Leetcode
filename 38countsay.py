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
             
           return "".join(result)
          
          
class Solution2(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = '1'
        for i in range(n - 1):
            prev = res[0]
            count = 1
            ans = ""
            for j in range(1, len(res)):
                  cur = res[j]
                  if prev != cur:
                        ans = ans + str(count) + str(prev)
                        prev = cur
                        count = 1
                  else:
                        count += 1
           res = ans + str(count) + str(prev)
        return res
           
