# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:41:45 2019

@author: liuga
"""

class Solution(object):
       def Nqueens(self, n):
         def check(k, j, board):
             for i in range(k):
                 if board[i] == j or abs(k-i) == abs(board[i]-j):
                     return False
             return True
              
         def dfs(depth, board, valuelist, res):
             if depth == len(board):
                 res.append(valuelist)
             for row in range(len(board)):
                 if check(depth, row, board):
                     s ='.'*len(board)
                     board[depth] = row
                     dfs(depth+1, board, valuelist + [s[:row]] + 'Q' + s[row+1:],res)   
         board=[-1 for i in range (n)]
         res = []
         dfs(0,board,[],res)
         return res


#DFS board 表示方法 [1, 3, 0, 2] 第0行，皇后放在第1列；第1行，皇后放在第3列
#不同行：数组board下标不同. 不同列：board中各元素值不相同就行了。board[i]!=board[j]
#不同斜线：board中元素相应的横纵坐标差的绝对值不等 |board[i]-board[j]|!=|i-j|

#此解法为主
class Solution(object):
       def solveNqueens(self, n):
           #check if the dth queen(第d个queen) can be put in column j(第j列)
           def check(d, i):
               for c in range(d):
                   if board[c] == i or abs(board[c]-i) == abs(d - c): # (i = board[d]). board[c] == board[d] or abs(board[c] - board[d]) == abs(c-d)同列或者同斜线
                       return False
               return True

           def dfs(depth, valuelist):
               if depth == n:
                   res.append(valuelist)
                   return

               else:
                   for i in range(n):
                       if check(depth, i):
                           board[depth] = i #depth对应row, i对应列col
                           s = '.'*n        #.代表空位
                           dfs(depth+1, valuelist + [s[:i] + 'Q' + s[i+1:]]) #dfs(depth+1, valuelist + ['.'*i + 'Q' + '.'*(n-1-i)])
                           

           res = []
           board = [-1 for i in range(n)]
           dfs(0 ,[])
           return res
                            
                  
               
