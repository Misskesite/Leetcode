# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:51:11 2019

@author: liuga
"""

class Solution(object):
    def spiralOrder(self, matrix):
         if not matrix:
             return []
         
         left = top = 0
         right = len(matrix[0]) -1
         bottom = len(matrix)-1
         
         result = []
         
         while True:
             for i in range(left, right+1):    # right
                 result.append(matrix[top][i])
             top += 1
             if top > bottom:
                 break
                
             for i in range(top, bottom+1):    # down
                 result.append(matrix[i][right])
             right -= 1
             if right < left:
                 break
                 
             for i in range(right, left-1, -1): #left
                 result.append(matrix[bottom][i])
             bottom -=1
             if bottom < top:
                 break
                 
             for i in range(bottom, top-1, -1): # up
                 result.append(matrix[i][left])
                 
             left +=1
             if left > right:
                 break                 
                                     
         return result


class Solution2(object):
    def spiralTraverse(self, matrix):
        if not matrix:
            return

        res = []
        while matrix:
            #first row
            if matrix:
                res += matrix.pop(0)

            #right-most col
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            #bottom from right to left
            if matrix:
                res += matrix.pop()[::-1]

            if matrix and matrix[0]:
                res += [row.pop(0) for row in matrix][::-1]

        return res
                     
