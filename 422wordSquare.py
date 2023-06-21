# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:30:02 2020

@author: liuga
"""
#字典
class Solution(object):
    def wordSquare(self, words):
        mp = {}
        m = len(words)
        n = len(words[0]) if m else 0
        if m != n:
            return False
        for i in range(m):
            for j in range(n):
                mp[j] += words[i][j]
        
        for i in range(m):
            if words[i] != mp[i]:
                return False
        return True
    
# words[i][j] != words[j][i]: return false
