# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:44:27 2019

@author: liuga
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        
        M = len(haystack)
        N = len(needle)
        for i in range(M-N+1):
            if haystack[i:i+N] == needle:
                return i
        return -1
            
    
    
#Kmp算法 复杂度O(M+N)
class Solution2(object):
    def strStr(self, haystack, needle):
        if needle == '': 
            return 0
        m = len(haystack)
        n = len(needle)
        j = 0
        pnext = self.getnext(needle)
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = pnext[j]
            if haystack[i]== needle[j]:
                j += 1
            if j == n:
                return i-n+1
        return -1
        
    def getnext(self, s):
        n = len(s)
        pnext = [0, 0] # 多一个前导0是为了方便后续指针跳跃，避免死循环
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pnext[j] # 指针跳跃
            if s[j] == s[i]:
                j += 1
            pnext.append(j) #pnext[i] = j
        return pnext
