# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:15:02 2020

@author: liuga
"""
import collections
#利用 HashMap 来建立前缀和所有包含此前缀单词的集合之前的映射
#如果prefix对应单词不存在，则可以剪枝 ，否则枚举mdict[prefix]，并递归搜索
class Solution(object):
    def wordSquares(self, words):
        
        m = len(words)
        n = len(words[0]) if m else 0
        
        mdict = collections.defaultdict()
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        
        matrix = []
        ans = []
        
        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:]) #已经填充好每一行列?
                #return
           
            prefix = ''.join(matrix[x][line] for x in range(line))#(0,1)开始
            for word in mdict[prefix]:
                search(word, line+1)
                    
            matrix.pop()
            
        for word in words:
            search(word,1) #也可以从0开始
        return ans 

#此解法为主
class Solution(object):
    def wordSquares(self, words):
        
        m = len(words)
        n = len(words[0]) if m else 0
        
        mdict = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                mdict[word[:i+1]].append(word) #make prefix dictionary

        res = []

        def dfs(i ,square):
            if i == len(square[0]):
                res.append(square)
                return
            #for the ith row, find a word with prefix string square[0..i-1][i] first i rows on the ith column
            prefix = "".join(square[k][i] for k in range(i)) #列拼出prefix
            for word in mdict[prefix]:
                dfs(i+1, square + [word])
        #Try each word as possible leading candidate
		#use second char of the leading word as next prefix to search for
        for w in words:
            dfs(1, [w])
        return res
'''
A better approach is to check the validity of the word square while we build it.
Example: ["area","lead","wall","lady","ball"]
We know that the sequence contains 4 words because the length of each word is 4.
Every word can be the first word of the sequence, let's take "wall" for example.
Which word could be the second word? Must be a word start with "a" (therefore "area"), because it has to match the second letter of word "wall".

we need to fast retrieve all the words with a given prefix. 
Using a hashtable, key is prefix, value is a list of words with that prefix.
'''

#使用Trinode
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.word_list.append(word)
        node.is_word = True
        

    def find(self, word):
            node = self.root
            for char in word:
                node = node.children.get(char)
                if node is None:
                    return None
                
            return node
    
    def word_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list
            

class Solution2(object):
    def wordSquare(self, words):
        trie = TrieNode()
        
        for word in words:
            trie.add(word)
        results = []
        
        for word in words:
            self.search(trie, [word], results)
            
        return results
    
    def search(self, trie, square, results):
        
        n, pos = len(square[0]), len(square)
        
        if pos == n:
            results.append(list(square))
            return
        
        for col in range(pos, n):
            prefix = ''.join(square[i][col] for i in range(pos))
            if trie.find(prefix) is None:
                return
            
        prefix = ''.join(square[i][pos] for i in range(pos))
        for word in trie.word_prefix(prefix):
            square.append(word)
            self.search(trie, square, results)
            square.pop()
    
