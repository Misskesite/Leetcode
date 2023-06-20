# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:12:43 2019

@author: liuga
"""

class Solution(object):
    def addBinary(self, a, b):
        
        res = []
        carry = val = 0
        
        if len(a) < len(b):
            a,b = b,a
            
        lenA = len(a)
        lenB = len(b)
        
        for i in range(lenA):
            val = carry
            val += int(a[-(i+1)]) #数字倒过来
            
            if i < lenB:
                val += int(b[-(i+1)])
                
            carry, val = val//2, val % 2
            res.append(str(val))
                
        if carry:
             res.append(str(carry))
                    
        return "".join(res[::-1])


class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:] #去除前缀0b




class Solution(object):
    def addBinary(self, a, b):
        if not a or not b:
            return a or b

        a = a[::-1]
        b = b[::-1]
        ans = []
        i, j, carry = 0, 0 ,0

        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            carry, cur = divmod(n1 + n2 + carry, 2)
            ans.append(str(cur))

            i = i +1
            j = j +1
        return ''.join(ans[::-1])


#a = "1010", b = "1011" 输出"10101"
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
