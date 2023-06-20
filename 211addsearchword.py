# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:07:50 2019

@author: liuga
"""
#字典get() 方法和 [key] 方法的主要区别在于，[key] 在遇到不存在的 key 时会抛出 KeyError 错误
import collections

class Node(object):
    def _init_(self):
        self.children = collections.defaultdict(Node) #(字符: Node) 保存 children 是使用的字典，它保存的结构是 {字符：Node} ，所以可以直接通过 children['a'] 来获取当前节点的 'a' 子树。
        self.isword = True

class Trie(object):
    def _init_(self):
        self.root = Node()
    
    def addWord(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        cur.isword = True
    
    def search(self, word):
        
        return self.match(word, 0, self.root)
    
    def match(self, word, index, root):
        if root is None:
            return False
        
        #遍历到单词末尾
        if index == len(word): 
            return root.isword
        if word[index] != '.':
            return root != None and self.match(word, index+1, root.children[word[index]]) #换成root.children.get(word[index])
        else: #对‘.’ 要对当前节点的子节点遍历 递归判断
            for child in root.children.values():
                if self.match(word, index+1, child):
                    return True
        return False


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.isWord
               
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
    
        return dfs(self.root, 0)            
   
class WordDictionary:
    def _init_(self):
        self.tree = {}

    def addWord(self, word):
        cur = self.tree
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True  //加#保证长的不会被当初短的单词存在

    def search(self, word):
        return self.dfs(self.tree, word, 0)

    def dfs(self, node, word, i):
        if i == len(word):
            return '#' in node
        if word[i] == '.':
            for child in node:
                if child != '#' and self.dfs(node[child], word, i + 1):
                    return True
            return False
        
        if word[i] not in node:
            return False
        return self.dfs(node[word[i]], word, i + 1)
    
#上面的改写
class WordDictionary:
    def _init_(self):
        self.trie = {}

    def addWord(self, word):
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True  //加#保证长的不会被当初短的单词存在

    def search(self, word):
        return self.dfs(self.trie, word)

    def dfs(self, node, word):
        for i,c in enumerate(word):
            if c == '.':
                return any(self.dfs(node[w]), word[i+1:]) for w in node if w != '$')

            if c not in node:
                return False
            node = node[c]
        return '#' in node
        
        

