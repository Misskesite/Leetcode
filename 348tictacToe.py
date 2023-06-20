# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:11:40 2020

@author: liuga
"""
#三子棋？ 每次下棋检查行列，对角线是不是连成一条线
class Tictactoe(object):
    def _init_(self,n):
        self.grid = [['']*n for i in range(n)]
        
    def move(self, row, col, player):
        if player == 1:
            mark = 'X'
        else:
            mark = 'O'
            
        self.grid[row][col] = mark
        
        n = len(self.grid)
        sum_row  = sum([self.grid[row][c] == mark for c in range(n)])
        sum_col = sum([self.grid[r][col] == mark for r in range(n)])
        sum_leftd = sum([self.grid[i][i] == mark for i in range(n)])
        sum_rightd = sum([self.grid[i][n-i-1] == mark for i in range(n)])
        if sum_row == n or sum_col == n or sum_leftd == n or sum_rightd == n:
            return player
        else:
            return 0

#Use addtional arrays rows[n], cols[n] and two varialbes diagonal, anti_diagonal to mark the number of Xs and Os.
#if it is player 1 put one chess, add that location by 1. If it is player 2, deduce it by one. Finally, if either player 1 or player 2 win, that location must be equal to n or -n. 
class Tictactoe2(object):
    def _init_(self, n):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.antiDiag = 0
        self.n = n

        
    def move(self, row, col, player):
        if player == 1:
            offset = 1
            target = self.n 
        else:
            offset = -1
            target = -self.n 

        self.rows[row] += offset
        self.cols[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.antiDiag += offset

        if target in [self.row[row], self.col[col], self.diag, self.antiDiag]:
            return player
        return 0
'''
一个大小为n的一维数组rows和cols，还有变量对角线diag和逆对角线rev_diag，这种方法的思路是，如果玩家1在第一行某一列放了一个子，那么rows[0]自增1，如果玩家2在第一行某一列放了一个子，则rows[0]自减1
只有当rows[0]等于n或者-n的时候，表示第一行的子都是一个玩家放的，则游戏结束返回该玩家即可
