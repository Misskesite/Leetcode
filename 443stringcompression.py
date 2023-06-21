# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:07:31 2020

@author: liuga
"""
#三个指针? aabbccc -> (a2b2c3) 返回6
class Solution(object):
    def stringCompression(self, s):
        n = len(s)
        i, count = 0,1
        for j in range(1, n+1):
            if j < n and s[j] == s[j-1]:
                count += 1 #标记连续多少个
            s[i] = s[j-1] #标记不连续的新位置？
            i += 1
            if count > 1:
                for m in str(count):
                    s[i] = m
                    i += 1
            count = 1
        return i
        
#此法为主      
def compress(self, s: List[str]) -> int:
        if not s:
            return
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            letter = s[i]
            count = 0
            while i < n and s[i] == letter:
                count += 1
                i += 1
            s[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    s[ans] = c
                    ans += 1

        return ans
