# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:56:53 2019

@author: liuga
"""

class Solution(object):
    def oneeditDistance(self, s,t):
        len1 = len(s)
        len2 = len(t)
        
        if abs(len1 - len2) >1:
            return False
        
        for i in range(min(len1, len2)):
            if s[i] != t[i]:
                if len1 == len2:
                    return s[i+1:] == t[i+1:]
                elif len1 < len2:
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:] #去掉s[i] 后面的值相等
        return abs(len1 - len2) == 1


class soluion(object):
    def isOneEditDistance(self, s, t):
        l1 = len(s)
        l2 = len(t)
        if abs(l1- l2) >1 :
            return False

        s = list(s)
        t = list(t)

        if l1 < l2:
            for i , c in enumerate(s):
                if s[i] != t[i]:
                    s.insert(i, t[i])
                    return s == t

            return True

        if l1 == l2:
            for i , c in enumerate(s):
                if s[i] != t[i]:
                    s[i] = t[i]
                    return s == t

        if l1 > l2:
            for i, c in enumerate(t):
                is s[i] != t[i]:
                    s.pop(i)
                    return s == t
            return True
