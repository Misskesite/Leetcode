# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:40:21 2020

@author: liuga
"""

class Solution(object):
    def findConcatenated(self,words):
        ans = []
        self.wordset = set(words)
        for word in words:
            self.wordset.remove(word)
            if self.search(word):
                ans.append(word)
            self.wordset.add(word)
            
        return ans
    
    def search(self,word):
        if word in self.wordset:
            return True
        for idx in range(1, len(word)):
            if word[:idx] in self.wordset and self.search(word[idx:]): #逐个字母遍历
                return True
        return False

#此法为主
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        memo = {}
        wordSet = set(words)
        res = []

        def isConcat(word: str) -> bool:
            
            if word in memo:
                return memo[word]            
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return memo[word]

        for word in words:
            if isConcat(word):
                res.append(word)
        return res
    
'''
需要排序吗
# asc order of word length, since longer words are formed by shorter words
        words.sort(key = len)

'''
#Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

#Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wordSet = set(words)

    @lru_cache(None)
    def isConcat(word: str) -> bool:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                return True

        return False

    return [word for word in words if isConcat(word)]

    #改写
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        memo = {}
        wordSet = set(words)
        
        def isConcat(word: str) -> bool:
            if len(word) == 1: #这句可以省略？ 因为word长为1，memo[word] = False
                return False
            if word in memo:
                return memo[word]
            memo[word] = False
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    memo[word] = True
                    break

            return memo[word]

        return [word for word in words if isConcat(word)]
    

#类似word break写法
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        wordset = set(words)
        for word in words:
            n = len(word)
            if n == 0:
                continue
            dp = [False]*(n+1)
            dp[0] = True
            for i in range(n):
                for j in range(i+1, n+1):
                    if dp[i] and word[i:j] in wordSet:
                        dp[j] = True
            '''
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                       dp[i] = True
                        break
            '''

                if dp[n]:
                    res.append(word)
                    break #跳出循环，开始下一个word
        return res
                
            


#也可以用Trie树实现
class TrieNode(object):
    def _init_(self):
        self.children = collections.defaultdict(TrieNode)
        self.isword = False

class Trie(object):
    def _init_(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:     
            cur = cur.children[w]
        cur.isword = True
    
    def find(self, word):  
        cur = self.root
        for i in len(word):
            if cur.isword:
                if self.dfs(word[i:]):
                    return True
            if word[i] in cur:
                cur = cur.children[word[i]]
            else:
                return False
        return cur.isword

class Solution(object):
    def findallConcatenatedWord(self, words):
        trie = Trie()
        ans = []
        for word in sorted(words, key = len):
            if word == "":
                continue
            if trie.find(word):
                ans.append(word)
            else:
                trie.insert(word)
        return ans
    
            
