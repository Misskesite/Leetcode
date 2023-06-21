# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:46:14 2020

@author: liuga
"""
class Solution(object):
    def repeateSubstring(self,s):
        len_s = len(s)
        for i in range(1, len_s//2+1):
            if len_s %i == 0:
                sub_s = s[:i]
                if sub_s *(len_s//i)== s:
                    return True
        return False
    
                
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

#此解法为主
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_s = len(s)
        i = (s+s).find(s,1)
        if i < len_s:
            return True
        else:
            return False
