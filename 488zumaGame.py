+-# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:20:09 2020

@author: liuga
"""

class Solution(object):
    def zumaGame(self, borad, hand):
        res = float('inf')
        m = {}
        for c in hand:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        
        res =  dfs(board,m)
        if res == float('inf'):
            return -1
        else:
            return res
        
    def dfs(board, m):
        if not board:
            return 0
        board = removeConsecutive(board)
        cnt = float('inf')
        j = 0
        for i in range(len(board)):
            if i < len(board) and board[i] == board[j]:
                continue
            #有可以消除的情况下，连续的个数只能是1个或2个，然后用3减去连续个数，就是需要补充的球数
            need = 3 -(i-j)
            if m(board[j]) >= need:
                m(board[j]) -= need
                t = dfs(board[:j]+board[i:], m)
                if t != float('inf'):
                    cnt = min(cnt,t + need)
                m[board[j]] += need
            j = i
        return cnt
    
    def removeConsecutive(board):
        j = 0
        for i in range(len(board)):
            if i < len(board) and board[i]==board[j]: #插入第一个位置，第二个位置相同情况？
                continue
            if i - j >= 3:
                return removeConsecutive(board[:j] + board[i:])
            else:
                j = i
        return board


    class Solution2(object):
        def findMinstep(self, board: str, hand: str) -> int:
            def remove(board):
                j = 0
                for i in range(len(board) + 1):
                    if i == len(board) or board[i] != board[j]:                         
                        if i - j >= 3:
                            return removeConsecutive(board[:j] + board[i:])
                        else:
                            j = i
                return board

            @lru_cache(None)
            def dfs(b, h):
                b = remove(b)
                if b and not h:
                    return float('inf')
                if not b:
                    return 0

                res = float('inf')'
                for i in range(1, max(len(b)-1, 2)):
                    for j in range(len(h)):
                        res = min(res, 1+ dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
                return res
            
            hand = ''.join(filter(lambda x: x in board, hand))
            res = dfs(board, hand)
            return res if res != float('inf') else -1
                            




