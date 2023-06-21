# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:26:57 2020

@author: liuga
"""

class Solution(object):
    def check(row, col, board):
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            return True
        return False
    
    def mineSweeper(self, board, click):
        (row,col) = click
        directions = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1))
        if self.check(row,col,board):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row+r][col+c]=='M' for r,c in directions if self.check(row+r,col+c,board)])
                board[row][col] = str(n if n else 'B') #没有相邻地雷的空方块被挖出
                if not n: #当前字符board[row][col]为‘B‘
                    for r,c in directions:
                        self.mineSweeper(board,[row+r,col+c])
        return board
    

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        def dfs(board, i, j):
            if board[i][j] != 'E':
                return

            m, n = len(board), len(board[0])       
            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            mine_count = 0

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
                    mine_count += 1

            if mine_count == 0:
                board[i][j] = 'B'
            else:
                board[i][j] = str(mine_count)                

            if mine_count == 0 :
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n:
                        dfs(board, ni, nj)

        # run dfs to reveal the board
        dfs(board, i, j)
        return board


                
            
#DFS 时间复杂度O(m*n)          
class Solution2(object):
    
    #挖的为”E“ 统计周围地雷的个数cnt
    def mineSweeper(self, board, click):
        directions = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(1,1),(-1,-1),(-1,1))
        row = len(board)
        col = len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        #计算空白快周围的地雷个数
        def count(i, j):
            cnt = 0
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                
                if 0 <= x < row and 0 <= y < col and board[x][y]=='M':
                    cnt += 1
            return cnt

        #个数为0，标记为B，B周围的点，递归的处理，将周围的E递归挖开，个数非零，标记E为数字cnt    
        def dfs(i, j):
            cnt = count(i, j)
            if not cnt:
                board[i][j] = "B"
                for dx, dy in direction:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < row and 0 <= y < col and board[x][y]== 'E':
                        dfs(x, y)
            else: #cnt > 0
                board[i][j] = str(cnt)
                #return  #这里return可以省略？
                

        dfs(click[0],click[1])
        return board

#BFS
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, -1, 1, 1, -1]

        def count(i, j):
            cnt = 0
            for dx, dy in direction:
                x = i + dx
                y = j + dy                
                if 0 <= x < row and 0 <= y < col and board[x][y]=='M':
                    cnt += 1
            return cnt
        
        # BFS
        def reveal(row, col):
            cnt = count(row, col)
            if cnt > 0:
                board[row][col] = str(cnt)
                return
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                cnt = count(row, col)
                if board[row][col] != 'E':
                    continue
                if cnt > 0:
                    board[row][col] = str(cnt)
                else:
                    board[row][col] = 'B'
                    for i in range(8):
                        nrow, ncol = row + dx[i], col + dy[i]
                        if m > nrow >= 0 and n > ncol >= 0 and board[nrow][ncol] == 'E':
                            q.append((nrow, ncol))
                            
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            reveal(row, col)
        return board

