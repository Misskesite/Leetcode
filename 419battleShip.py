# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:35:41 2020

@author: -
"""
#只需要统计起点，每一个战舰要么是竖着，要么是横着
class Solution(object):
    def battleShip(self, board):
        if len(board) ==0 or len(board[0])==0:
            return 0
        row = len(board)
        col = len(board[0])
        cnt = 0
        for i in range(row):
            for j in range(col): #起点为X，左边不为X，上边不为X 关注左上角，寻找头部？ 战舰起始点，就是为X的点，而且该点的上方和左边的点不能为X
                if board[i][j]=='X' and (i == 0 or board[i-1][j]== '.') and (j == 0 or board[i][j-1]=='.'):
                    cnt += 1
        return cnt
    
              
    
class Solution2(object):
    def battleShip2(self, board):
        if len(board) == 0 or len(board[0])== 0:
            return 0
        row = len(board)
        col = len(board[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':                    
                    if i > 0 and board[i - 1][j] == "X": #关注左边，说明计算过了
                        continue
                    if j > 0 and board[i][j-1] == "X":    #关注上边， 说明计算过了
                        continue
            
                    cnt += 1
        return cnt
