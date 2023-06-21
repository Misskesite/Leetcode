# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:10:10 2020

@author: liuga
"""

import collections

class Solution(object):
    def lonelyPixel(self,picture,n):
        w,h = len(picture), len(picture[0])
        rows = [0]*w
        cols = [0]*h
        for x in range(w):
            for y in range(h):
                if picture[x][y]=='B':                    
                    rows[x]+=1
                    cols[y]+=1
        
        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)]+=1
        
        ans = 0
        for x in range(w):
            row = ''.join(picture[x])
            if sdict[row] != n:
                continue
            for y in range(h):
                if picture[x][y] == 'B':
                    if rows[x]==n:
                        if cols[y]==n:
                            ans +=1
        return ans
                    
                
                
        
            
        