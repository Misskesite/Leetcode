# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:12:44 2019

@author: liuga
"""

class Solution(object):
    def findword(self, words, board):
        if len(board) == 0:
            return []
        row = len(board)
        col = len(board[0])
        visit = [[False for _ in range(row)] for _ in range(col)]
        trie = Trie()
        for word in words:
            trie.insert(word)            
    
        res = []
        
        def dfs(word, node, x, y):
            child = node.childs[board[x][y]]
            if child == None:
                return
            node = child
            visit[x][y] = True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                dfs(word + board[nx][ny], node, nx, ny)
            
            visit[x][y] = False
            if node.isWord:
                res.append(word)
                trie.delete(word)  #把找到的树对应的节点删掉
                
        for x in range(row):
            for y in range(col):
                dfs(board[x][y],trie.root,x,y)
        
        return res
                
class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            child = node.childs.get(w)
            if child == None:
                child = TrieNode()
                node.childs[w] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for w in word:
            queue.append((w, node))
            child = node.childs.get(w)
            if not child:
                return False
            node = child
        if not node.isWord:
            return False
        if node.childs:
            node.isWord = False
        else:
            for w,node in reversed(queue):
                del node.childs[w]
                if node.childs or node.isWord:
                    break
        return True            


#方法2
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.chilren[c] = TrieNode()             
            cur = cur.children[c]
        cur.isWord = True
    
            
class Solution(object):
    def findWords(self, board, words):
        root =  TrieNode()
        for w in words:
            root.addWord(w)
            
        m = len(board)
        n = len(board[0])
        res = set()
        visit = set()

                    
        def dfs(r, c , node, word):
            if r < 0 or c < 0 or r >= m or y >= n or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dx, c + dy                
                    dfs(nr, nc, node, word)

            visit.remove((r, c))

        
     
        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
        
        return list(res)
                
                
                    
