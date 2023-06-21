# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:47:33 2020

@author: liuga
"""

class Solution(object):
    def findlonelyPixel(self, picture):
        w,h = len(picture), len(picture[0])
        rows = [0]*w
        cols = [0]*h
        for x in range(w):
            for y in range(h):
                if picture[x][y]=='B':                    
                    rows[x] += 1 #x行有多少个B
                    cols[y] += 1 #y列有多少个B
        ans = 0
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    if rows[x] == 1:
                        if cols[y] == 1:
                            ans += 1
        return ans
        
