# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:26:06 2020

@author: liuga
"""
#h[x][y], v[x][y], d[x][y], a[x][y]表示以元素M[x][y]结尾的横向，纵向，斜对角，反对角的最大长度
#h[x][y] = M[x][y]*(h[x-1][y] + 1)
#v[x][y] = M[x][y]*(v[x][y-1] + 1)
#d[x][y] = M[x][y]*(d[x-1][y-1] + 1)
#a[x][y] = M[x][y]*(a[x+1][y-1] + 1)
class Solution(object):
    def longestLine(self, M):
        h = len(M)
        w = len(M[0])
        ans = 0

        #horizontal & diagonal
        diag = [[0]* w for r in range(h)]
        for x in range(h):
            cnt = 0
            for y in range(w):
                cnt = M[x][y] *(cnt + 1)
                diag[x][y] = M[x][y]
                if x > 0 and y > 0 and M[x][y] and diag[x-1][y-1]:
                    diag[x][y] += diag[x-1][y-1]
                ans = max(ans, cnt, diag[x][y])

        #vertical & anti-diagonal
        adiag = [[0]* w for r in range(h)]
        for x in range(w):
            cnt = 0
            for y in range(h):
                cnt = M[y][x] * (cnt + 1)
                adiag[y][x] = M[y][x]
                if y < h - 1 and x > 0 and M[y][x] and adiag[y + 1][x - 1]:
                    adiag[y][x] += adiag[y + 1][x - 1]
                ans = max(ans, cnt, adiag[y][x])
        return ans
            
                
#此解法为主    
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        if m == 0 or n == 0:
            return 0
        maxlen = 0
        h = [[0]*n for _ in range(m)] #horizontal
        v = [[0]*n for _ in range(m)] 
        diag = [[0]*n for r in range(m)]
        adiag = [[0]*n for r in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                h[i][j] = h[i-1][j] + 1 if i >0 else 1
                v[i][j] = v[i][j-1] + 1 if j >0 else 1
                diag[i][j] =  diag[i-1][j+1]+1 if i > 0 and j +1 < n else 1
                adiag[i][j] =  adiag[i-1][j-1]+1 if i > 0 and j > 0 else 1
                maxlen = max(maxlen, h[i][j], v[i][j],diag[i][j], adiag[i][j])
        return maxlen
                
#递归
class Solution(object):
    def longestLine(self, M):
        m = len(M)
        n = len(M[0])
        if m == 0 or n == 0:
            return 0
        directions = [(1, 0),(0,1), (1, 1), (1, -1)]
        res = 0

        def getMax(self, M, x, y):
            res = 1
            for dir in directions:
                i = x + dir[0]
                j = y + dir[1]
                count = 1
                while i < len(M) and j < len(M[0]) and i >= 0 and j >= 0 and M[i][j] == 1:
                    i += dir[0]
                    j += dir[1]
                    count += 1
                res = max(res, count)
            return res
            
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    res = max(res, getMax(M, i, j))
        return res

#此法为主
#上面的简化版 类似于dfs的思路 
    def longestLine(self, M):
        m = len(M)
        n = len(M[0])
        if m == 0 or n == 0:
            return 0
        directions = [(1, 0),(0,1), (1, 1), (1, -1)]
        res = 0      
            
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                for dir in directions:
                    x = i
                    y = j
                    count = 0
                    while x < m and y < n and x >= 0 and y >= 0 and M[i][j] == 1:
                        i += dir[0]
                        j += dir[1]
                        count += 1
                    res = max(res, count)
                   
        return res

        
        
        
