# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:13:27 2020

@author: liuga
"""

class Solution(object):
    def licenceKey(self,s,k):
        res = []
        s = "".join(s.split("-").upper())
        n = len(s)
        if n % k !=0:
            res.append(s[: n%k])
        for i in range(n%k, n, k):
            res.append(s[i:i+k])
        return '-'.join(res)
            