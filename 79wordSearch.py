# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:04:25 2019

@author: liuga
"""
#回溯法 时间复杂度O（m*n*3**l）
class Solution(object):
    def wordSearch(self, board, word):
        m = len(board)
        n = len(board[0])
        
        if len(word) == 0:
            return True
        
        for x in range(m):
            for y in range(n):
                if self.dfs(board, word, x, y, 0):
                    return True
        return False
    
    def dfs(self, board, word, x, y, i):
         if i == len(word):
             return True
         if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
             return False
         if board[x][y] != word[i]:
             return False
         board[x][y] = board[x][y].swapcase()
         result = self.dfs(board, word, x, y+1, i+1) or self.dfs(board,word, x+1, y, i+1)\
         or self.dfs(board,word,x, y-1,i+1) or self.dfs(board, word, x-1, y, i+1)
         
         board[x][y]= board[x][y].swapcase()
         
         return result


#时间复杂度O(mn4^len(word))
class Solution2(object):
    def wordSearch(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            visited.add((i,j))
            
            for dix,diy in directions:
                curx = i + dix
                cury = j + diy

                if 0 <= curx < m and 0 <= cury < n and (curx, cury) not in visited:                   
                    if check(curx, cury, k+1):                                              
                        return True
            
            visited.remove((i,j))
            return False



                    
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        return False
        
