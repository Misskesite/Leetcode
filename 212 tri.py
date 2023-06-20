# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:25:34 2019

@author: liuga
"""

class Trie(object):
    def _init_(self):
        self.root = {}
        
    def insert(self,word):
         curNode = self.root
         for i in word:
             if i not in curNode:
                 curNode[i] = {}
                 curNode = curNode[i]
             curNode["#"] = True
                     
class Solution:   
    def findWords(self, board, words):
        row = len(board)
        colum = len(board[0])
        res = []
        
        def find(x, y, word, TrieNode):
            if x >= 0 and x < row and y >= 0 and y < colum and board[x][y]:
                TrieNode = TrieNode[board[x][y]]
                word += board[x][y]
                
                if TrieNode.get("#",9) == True:
                    res.append(word)
                    
                    t = board[x][y]
                    board[x][y]=3
                    
                    find(x+1,y,word, TrieNode)
                    find(x-1,y,word, TrieNode)
                    find(x,y+1,word, TrieNode)
                    find(x,y-1,word, TrieNode)
                    board[x][y] = t
                    
                root =Trie()
                tmp = set()
                
                for i in words:
                    root.insert(i)
                    tmp.add(i[0])
                    
                for i in range(row):
                    for j in range(colum):
                        if board[i][j] in tmp:
                            find(i,j,"",root.root)
                            
                return list(set(res))
                
            
class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
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

                
