# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:50:10 2019

@author: liuga
"""


class Solution2(object):
    def solveSudoku(self, board):
        #检验在x, y的位置能插入val
        def isValid(x , y, k):
            for i in range(9):
                if board[i][y] == k:
                    return False

            for j in range(9):
                if board[x][j] == k:
                    return False

            for i in range(3): #判断九方格是否重复
                for j in range(3):
                    if board[int(x//3)*3 + i][int(y//3)*3 + j] == k: #int(x//3)*3 起始行号
                        return False

            return True
      
         #找到一组解就返回
        def dfs(board):
            for i in range(9): #遍历每一行，每一列
                for j in range(9):
                    if board[i][j] == '.': #不是空格，跳过                                  
                        for k in '123456789':
                            if isValid(i, j, k):
                                board[i][j] = k #放置k
                                if dfs(board):
                                    return True 
                                board[i][j] = '.'  #撤销选择，回溯
                        return False           #九个数都试完了，都不行，此位置没有能插入的数字
            return True                   #遍历完都没有返回false 每个位置都得到合法的值

        dfs(board)
                              
               
                
            
          
def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3)*3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3)*3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter+1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()

