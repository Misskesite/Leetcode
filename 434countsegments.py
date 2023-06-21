# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:53:44 2020

@author: liuga
"""

class Solution(object):
    def countSegment(self, s):
        if s.isspace():
            return 0
        s1 = s.strip()
        if len(s1) == 0:
            return 0
        d = [0]
        m = list(s1)
        while m:
            if m[0] != "":
                d[-1] +=1
            else:
                d.append(0)
            m.pop(0)
        return len(d)-d.count(0)

         
       #或者直接用内置函数
       return len(s.split())
