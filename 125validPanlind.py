d# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:18:51 2019

@author: liuga
"""
#时间O(n) 空间O(1) 在原字符串修改
class Solution(object):
    def validPanlind(self, s):        
        if len(s) == 0 :
            return True
        i = 0
        j = len(s)-1
        while i < j:
            while s[i].isalnum() == False and i < j:
                i += 1
            while s[i].isalnum() == False and i < j:
                j -= 1
                
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True


#双指针 时间O(n) 空间(n)
class Solution(object):
    def validPanlind(self, s):        
        if len(s) == 0 :
            return True
        s = [ch.lower() for ch in s if ch.isalnum()]
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True
            
