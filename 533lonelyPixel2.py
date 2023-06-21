# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:20:13 2020

@author: liuga
"""
import collections
class Solution(object):
    def findLonelyPixel(self, picture, N):
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1
                    
        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)] += 1
            
        ans = 0
        
        for x in range(w):
            row = ''.join(picture[x])
            if sdict[row] != N: #含有B的行都相同，总共有N个
                continue
            for y in range(h):
                if picture[x][y] == 'B': #行列的B数目都相同，对应坐标的值是B
                    if rows[x] == N:
                        if cols[y] == N:
                            ans += 1
        return ans


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m = len(picture)
        n = len(picture[0])
        ans = 0
        rows = [row.count('B') for row in picture]
        cols = [col.count('B') for col in zip(*picture)]
        rowStrings = [''.join(row) for row in picture]
        countRowStrings = collections.Counter(rowStrings)

        for i, (row, stringRow) in enumerate(zip(rows, rowStrings)):
            if row == target and countRowStrings[stringRow] == target:
                for j, col in enumerate(cols):
                    if picture[i][j] == 'B' and col == target: #黑色为n个的列
                        ans += 1

        return ans
