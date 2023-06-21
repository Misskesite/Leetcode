# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:39:44 2020

@author: liuga
"""

class Solution(object):
    def findDiagnol(self, matrix):
        if not matrix or not matrix[0]:
            return []
        directions = [(-1,1),(1,-1)]
        count = 0
        res = []
        i,j = 0,0
        m = len(matrix)
        n = len(matrix[0])
        while len(res) < m*n:
            if 0<= i <m and 0 <= j <n:
                res.append(matrix[i][j])
                direct = directions[count%2]
                i = i + direct[0]
                j = j + direct[1]
                continue
            elif i < 0 and 0 <= j <n:
                i+=1
            elif 0 <= i <m and j <0:
                j+=1
            elif i < m and j >=n: #右边越界，向下移动
                i += 2
                j -= 1
            elif i >= m and j <n: #左边越界， 像下移动
                j += 2
                i -= 1
            count +=1
        return res
    
                
import collections
class Solution2:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        lookup = collections.defaultdict(list)
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                lookup[j + i].append(matrix[i][j])
        res = []
        flag = True
        for k, v in sorted(lookup.items()):
            if flag:
                res.extend(v[::-1]) #append添加单个元素，extend添加多个元素(列表)，如果append一个列表，那么列表被当成一个元素(a,[b,c])
            else:
                res.extend(v)
            flag = not flag
        return res


#1- Group numbers according to diagonals. Sum of row+col in same diagonal is same.
#2- Reverse numbers in odd diagonals before adding numbers to result list.
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        dd = collections.defaultdict(list)
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k in sorted(dd.keys()):
            if k%2==1:
                dd[k].reverse()
            result += dd[k]
        return result
