# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 17:39:46 2019

@author: liuga
"""

class Solution(object):
    def spiralMatrix(self, n):
        left = top = 0
        right = n - 1
        bottom = n - 1
        
        num = 1
        result = [[0 for _ in range(n)] for _ in range(n)]
         
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            for i in range(top, bottom):
                result[i][right] = num
                num += 1
            for i in range(right, left, -1):
                result[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                result[i][left] = num
                num += 1
                
                left += 1
                right -= 1
                top += 1
                bottom -= 1
                
            if left == right and top == bottom:
                result[top][left] = num
                
            return result


class Solution(object):
    def spiralMatrix(self, n):
        l = t = 0
        r = b = n-1

        mat = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        tar = n*n
        
        while num <= tar:
            for i in range(1, r+1):    #left to right
                mat[t][i] = num
                num += 1
            t += 1

            for i in range(t, b+1):    #top to bottom
                mat[i][r] = num
                num += 1
            r -= 1

            for i in range(r, l-1, -1): #right to left
                mat[b][i] = num
                num += 1
            b -= 1

            for i in range(b, t-1, -1): #bottom to top
                mat[i][l] = num
                num += 1
            l += 1
        return mat



class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curx = cury = curd = 0
        for i in range(1, n * n + 1):
            res[curx][cury] = i
            newx, newy = curx + directions[curd][0], cury + directions[curd][1]
            if newx < 0 or newx >= n or newy < 0 or newy >= n or res[newx][newy]: #出边界或者已经被填过
                curd = (curd + 1) % 4
            curx += directions[curd][0]
            cury += directions[curd][1]
        return res
