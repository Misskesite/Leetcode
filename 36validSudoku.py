# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:51:34 2019

@author: liuga
"""

class Solution(object):
    def validSokudo(self, board):
        point = "."
        n = len(board)
        m = sqrt(n)
        for i in range(n):
            row = []
            col = []
            square = []
            for j in range(n):
                 element = board[i][j]
                 if element != point:
                     if element in row:
                         return False
                     else:
                         row.append(element)
                         
                 element = board[j][i]
                 if element != point:
                     if element in col:
                         return False
                     else:
                         col.append(element)
                        
                 element = board[i//m*m + j//m][i%m*m + j%m] #第几个格子，格子的第几个元素  [i,j]=[1,8] board[2][5]
                 if element != point:
                     if element in square:
                         return False
                     else:
                         square.append(element)
                         
            return True

#字典套字典 哈希表
class Solution2(object):
    def validSokudo(self, board):
        record = {0:defaultdict(set), 1:defaultdict(set), 2: defaultdict(set)} #row col square
        n = len(board)
        m = sqrt(n)

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
                    return False

                sq = i//m*m + j//m #第几个小格子
                if board[i][j] in record[2][sq]:
                    return False
                record[0][i].add(board[i][j])
                record[1][j].add(board[i][j])
                record[2][sq].add(board[i][j])
        return True

#上面的改写 数字1-9每一行只出现一次，每一列只出现一次，每个3*3的格只出现一次
    def validSokudo(self, board):
        a = defaultdict(set)
        b = defaultdict(set)
        c = defaultdict(set)

        n = len(board)
        m = sqrt(n)
        
        for i in range(n):
            for j in range(n):
                #空白格
                if board[i][j] == '.':
                    continue

                if board[i][j] in a[i] or board[i][j] in b[j]:
                    return False
                
                sq = i // m*m + j // m
                if board[i][j] in c[sq]:
                    return False

                # 0: row, 1: column, 2: square
                a[i].add(board[i][j])
                b[j].add(board[i][j])
                c[sq].add(board[i][j])

        return True
                
                
