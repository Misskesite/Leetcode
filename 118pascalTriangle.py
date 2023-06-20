# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:56:47 2019

@author: liuga
"""

class Solution(object):
    def pascalTriangle(self, numsRow):
        if not numsRow:
            return []
        result = [[1]]
        for i in range(numsRow):
            for j in range(0, i+1):
                if j == 0 or j == i:
                    result[i][j] = 1
                else:
                    result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result
            

def pascalTriangle(self, numsRow):
if not numRows:
            return []
        res = []
        for i in range(numRows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(row)
        return res
    
