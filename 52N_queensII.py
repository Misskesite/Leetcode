# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:03:52 2019

@author: liuga
"""

class Solution(object):
    def totalNqueens(self, n):
        # check if the kth queen can be put in column j
        def check(k, j):
            board =[-1 for _ in range(n)]
            for i in range(k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True
        
            row = 0
            col = 0
            sum = 0
        while row < n:
            while col < n:
                if check(row, col):
                    board[row] = col
                    col = 0
                    break
                else:
                    col += 1
            if board[row] == -1:
                if row == 0:
                    break
                else:
                    row -= 1
                    col = board[row] +1
                    board[row] -=1
                    continue
            if row == n-1:　　　　　　　　　　　　　　　　　　　　　
                sum += 1
                col= board[row]+1
                board[row]=-1
                continue
           row+=1
           return sum

#每个位置判断其是否在三个集合中,如果三个集合都不包括当前位置，则可以放皇后
#时间复杂度O(n!) 空间复杂度O(n)  回溯法
class Solution2(object):
    def totalNqueens(self, n):
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        
        def backtrack(row):
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row-i in diagonal1 or row + i in diaonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row-i)
                    diagonal2.add(row+i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row-i)
                    diagonal2.remove(row+i)

                return count

        return backtrack(0)
                
       
#DFS       
class Solution3:    
    def check(self, row, j, board): 
        for i in range(row):
            if board[i] == j or abs(row - i) == abs(board[i]-j):
                return False
        return True
    
    def dfs(self, row, board, n):
        if row == n:
            self.count += 1
            return
        for col in range(n):            
            if self.check(row, col, board):
                board[row] = col                
                self.dfs(row+1, board, n)
            
                
    def totalNQueens(self, n):
        self.count = 0
        board = [-1 for i in range(n)]
        self.dfs(0, board, n)
        return self.count


                
            
