# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:29:10 2020

@author: liuga
"""

class Solution(object):
    def addString(self, num1,num2):
        res = ""
        carry  = 0
        m,n = len(num1), len(num2)
        if m <n:
            num1 = "0"*(n-m) + num1
        else:
            num2 = "0"*(m-n) + num2
            
        n = max(m,n)
        for i in range(n-1,-1,-1):
            add = int(num1[i]) + int(num2[i]) + carry
            if add >= 10:
                carry = 1
                add -= 10
            else:
                carry = 0
                
            res = str(add) + res
        if carry:
            res = "1" + res
        return res


class Solution(object):
    def addString(self, num1, num2):
        result = []
        carry = 0
        idx1, idx2 = len(num1)-1, len(num2)-1
        while idx1 >= 0 or idx2>= 0 or carry:
            if idx1 >= 0:                
                carry += int(num1[idx1])
                idx1 -= 1
            if idx2 >= 0:
                carry += int(num2[idx2])
                idx2 -= 1
            result.append(str(carry % 10))
            carry = carry//10
            

        return ''.join(result[::-1])
    

class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
      ans = []
      carry = 0
      i = len(num1) - 1
      j = len(num2) - 1

      while i >= 0 or j >= 0 or carry:
          if i >= 0:
              carry += int(num1[i])
          if j >= 0:
              carry += int(num2[j])
          ans.append(str(carry % 10))
          carry //= 10
          i -= 1
          j -= 1

      return ''.join(reversed(ans)) #ans[::-1]
