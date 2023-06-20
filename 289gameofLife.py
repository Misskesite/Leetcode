# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:21:20 2020

@author: liuga
"""
# 1 -> live if 2, 3 living neibour else die
# 0 -> live if 3 living neibour else die
#时间空间O(m*n)
class Solution(object):
    def gameofLife(self, board):
        m = len(board)
        n = len(board[0])

        ds = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        
        board_next = [[board[row][col] for col in range(n)] for row in range(m)] #如果[:] 同时修改。这里复制数组 复制的那一份永远不修改
        for i in range(m):
            for j in range(n):
                live_cnt = 0
                for d in ds:
                    r, c = i + d[0], j + d[1]
                    if 0 <= r < m and 0 <= c <n and board_next[r][c]== 1:
                        live_cnt += 1
                #规则1 或 3       
                if live_cnt < 2 or live_cnt > 3 and board_next[i][j] == 1:
                    board[i][j] = 0
                #规则4
                if live_cnt == 3 and board_next[i][j] == 0:
                    board[i][j] = 1
        

#follow #up能否O(1) memory original - new - state (1 0 0| 1 0 1| 0 1 2 | 1 1 3)
# 定义复合状态2 表示由0(死)变成1(活) 状态-1表示由活(1)变成死(0)
#时间复杂度O(m*n) 空间复杂度O(1)
class Solution2(object):
    def gameofLife(self, board):
        m = len(board)
        n = len(board[0])

        ds = [(1, 1), (1, -1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                live_cnt = 0
                for d in ds:
                    r, c = i + d[0], j + d[1]
                    if 0 <= r < m and 0 <= c <n and abs(board[r][c]) == 1:
                        live_cnt += 1
                #规则1 或 3       
                if live_cnt < 2 or live_cnt > 3 and board[i][j] == 1:
                    board[i][j] = -1
                #规则4
                if live_cnt == 3 and board_next[i][j] == 0:
                    board[i][j] = 2

       #遍历一遍更新状态
        for i in range(m):
            for j in range(n):
               if board[i][j] > 0: #2或者1
                   board[i][j] = 1
               else:
                   board[i][j] = 0

'''
all new 0's denotes as -1, (1 ==> 0)
all new 1's denotes as 2   (0 ==> 1)
