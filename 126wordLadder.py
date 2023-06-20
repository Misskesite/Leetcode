# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:04:14 2019

@author: liuga
"""
#广度优先构图 + 深度优先遍历
#BFS + hash + 回溯. 最短转换序列(树形结构，最小的树高) 层为单位来做判断是否到达 最小树高

class Solution(object):
    def wordLadder(self, beginword, endword, wordlist):
        se = set(wordList)
        if not endWord in se:
            return []
        
        #通过一个节点找到它关联的节点，也就是遍历边
        def edges(word):
            arr = list(word)
            for i in range(len(arr)):
                c = arr[i]
                for j in range(97, 123):
                    arr[i] = chr[j]
                    newWord = ''.join(arr)
                    if newWord in se and not newWord in marked:
                        yield newWord
                arr[i] = c
        '''
        hash = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)): #初始化：将单词列表的所有元素全部hash保存进字典
                hash[word[:i] + '*' + word[i+1:]].append(word)

        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i]+ '*' + word[i+1:]]:
                    if not newword in marked:
                        yield newWord #遍历该单词的所有hash,从字典中取出关联的单词
        

        '''

        res = []
        marked = set()
        queue =[[beginWord]]
        while queue:
            temp = []
            found = False
            for words in queue:
                marked.add(words[-1]) #words代表包含了一个完整路径的节点，words[-1]表示该节点当前的单词信息

            for words in queue:
                for w in edges(words[-1]):
                    v = words + [w]
                    if w == endWord:
                        res.append(v)
                        found = True
                    temp.append(v)

            if found:   #找到就不再遍历了，即使再有endWord,路径会更长
                break
            queue = temp
        return res
                
            


class Solution(object):
    def wordLadderII(self, beginword, endword, wordlist):
           
        length = len(beginword)
        premap = {}
        for word in wordlist:
            premap[word] = []

        def buildPath(path, word):
            if len(premap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for w in premap[word]:
                buildPath(path, w)                
            path.pop(0)
        
        result = []
        cur_level = set()
        cur_level.add(beginword)
        
        
        while True:
            pre_level = cur_level
            cur_level = set()
            
            for word in pre_level:
                wordlist.remove(word)
                
            for word in pre_level:
                for i in range(length):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c != word[i]:                            
                            newword = word[:i] + c + word[i+1:]
                            
                        if newword in wordlist:
                            premap[newword].append(word)
                            cur_level.add(newword)
            if len(cur_level) == 0:
                return []
            
            if endword in cur_level:
                break
            
        buildPath([], endword)
            
        return result
        
              


import collections
class Solution2(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordlist = set(wordList)
        res= []
        layer = {} #记录路径
        layer[beginWord] = [[beginWord]]
        
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer: #循环字典的key 也可以layer.keys()
                if w == endWord:   #这一层所有的单词都要extend进来
                    res.extend(k for k in layer[w]) #layer[w]的意思是：能达到单词w的全部单词组合
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword = w[:i] + c + w[i+1:]
                            if newword in wordlist:
                                newlayer[newword] += [j + [newword] for j in layer[w]]
            wordlist -= set(newlayer.keys())
            layer = newlayer
        return res


#BFS用于找无权图的最短路径
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordlist:
            return []
        
        
        wordList.append(beginWord)
        
        
        nei = collections.defaultdict(list)

        # build an adjacent list
        for word in wordList: # iterate each word
            for j in range(len(word)): # find patterns of each word
                pattern = word[:j] + "*" + word[j+1:] # replace the char in j position with *
                nei[pattern].append(word) # add the word in the dict

        visited = set([beginWord]) 
        q = collections.deque((beginWord,[beginWord]))

        res = []
        wordList = set(wordList)

        while q:
            
            for _ in range(len(q)):
                word, seq = q.popleft()
                if word = endWord:
                    res.append(seq)

                # go with it's neighbors 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    # check the neighbors
                    for neiWord in nei[pattern]:
                        # we don't check the word itself
                        if neiWord in wordList:
                            visited.add(neiWord)
                            q.append((neiWord, seq+[neiWord]))   
            wordList -= visited
        return res




    
'''
#BFS，定义两个整型变量level和 minLevel，如果某条路径的长度超过了已有的最短路径的长度，那么舍弃，这样会提高运行速度，相当于一种剪枝
#定义一个 HashSet 变量 words，用来记录已经循环过的路径中的词, BFS循环路径集paths里的内容，取出队首路径，如果该路径长度大于level，说明字典中的有些词已经存入路径了，
#需要在字典中将这些词删去，然后将words清空，对循环对剪枝处理, 取出当前路径的最后一个词，对每个字母进行替换并在字典中查找是否存在替换后的新词,如果替换后的新词在字典中存在，将其加入 words 中，并在原有路径的基础上加上这个新词生成一条新路径
