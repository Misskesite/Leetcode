# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:30:02 2020

@author: liuga
"""
#从第二个字母开始，++变成—-
class Solution(object):
    def generatePossible2(self, s):
        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                res.append(s[:i] + '--' + s[i+2:])
        return res
