# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:43:45 2019

@author: liuga
"""
#前缀树又称为字典树, 每一个节点的子孩子都是一个字典,isword保存当前是不是一个词（也可能是路径中的点）
import collections

class TrieNode(object):
    def _init_(self):
        self.children = collections.defaultdict(TrieNode) #Dict[str, TrieNode]
        self.isword = False

class Trie(object):
    def _init_(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:      #字典key不存在，则是添加元素（如果key已存在，则是修改key对应的value）
            cur = cur.children[w]
        cur.isword = True
    
    def search(self, word): #和下面的比较，多了一个isword判断
        cur = self.root
        for w in word:
            cur = cur.children.get(w)
            if cur is None:
                return False
        return cur.isword

    def StartsWith(self, prefix):
        cur = self.root
        for w in prefix:
            cur = cur.children.get(w) #if cur not in cur.children: return False. cur = cur.children[w]
            
            if cur is None:
                return False
        return True


'''
def search(self, word):
    node = self.find(word)
    return node and node.isword

def StartsWith(self, prefix):
    return self.find(prefix)
'''

    
def find(self, prefix):
    cur = self.root
    for w in word:
        if w not in cur.children:
            return False
        cur = cur.children[w]
    return cur

'''

1. 根节点不包含字符，除根节点意外每个节点只包含一个字符。

2. 从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。

3. 每个节点的所有子节点包含的字符串不相同
    
            
#字典树的每一个节点都是一个map，key是当前字母,value是所有子树。如果一个单词结束，就在下方差一个#标志
class Solution(object):
    def _init_(self):
        self.dic = {}

    def insert(self, word):
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word):
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix):
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
        
            
    
        
