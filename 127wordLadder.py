i# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:38:04 2019

@author: liuga
"""

from collections import deque

class Solution(object):
    def wordLadder(self, beginword, endword, wordlist):
        
        wordset = set(wordList)
        bfs = deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordset and newword != word:
                        wordset.remove(newword)         #避免该词重复入列
                        bfs.append((newword, length+1)) #作为下一层的词入列
        return 0  #bfs结束，始终没有遇到终点
