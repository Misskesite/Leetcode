# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:10:41 2020

@author: liuga
"""

class Solution(object):
    def _init_(self):
        self.cnt  = 0
        self.d = dict()
        
    def encode(self,longUrl):
        self.cnt += 1
        self.d[self.cnt] = longUrl
        return str(self.cnt)
    
    def decode(self, shortUrl):
        return self.d[int(shortUrl)]
