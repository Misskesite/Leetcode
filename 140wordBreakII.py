# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:40:44 2019

@author: liuga
"""
from collections import defaultDict

class Solution(object):
    def wordBreak(self, s, wordDict):
        dic = collections.defaultDict(list)
        
        def dfs(s):
            if s in dic:
                return dic[s]
            if not s:
                return [None]
            
            res = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    for r in dfs(s[n:]):
                        if r:
                            res.append(word + " " + r)
                        else:
                            res.append(word)
             dic[s] = res
             return res
         return dfs(s)

#字典保存已经能切分的方式
class Solution2(object):
    def wordBreak(self, s, wordDict):
        res = []
        memo = dict() #不同s映射成不同的字符串组合

        def dfs(s, res, wordDict, memo):
            if s in memo:
                return memo[s]

            if not s:
                return [""]  #已经到末尾了，返回

            res = []
            for word in wordDict:
                n = len(word)
                if s[:n] != word:
                    continue
                for r in dfs(s[n:], res, wordDict, memo):
                    res.append(word + ("" if not r else " " + r)) 
            memo[s] = res #更新字典避免重复搜索
            return res

        return dfs(s, res, wordDict, memo)

#DP 加回溯
class Solution3(object):
    def wordBreak(s, wordDict):
        res = []
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        #[0-j]部分和[j-i]部分都可以，[0-i]部分也必然可以
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        '''
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        '''
                    
        def dfs(j, path):
            if j == n:
                res.append(" ".join(path))
                return
            for i in range(j+1, n+1):
                if dp[i]:
                    word = s[j:i]
                    if word in wordDict:
                        dfs(i, path + [word])
        
        dfs(0, [])
        return res


#此解法为主
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        wordDict = set(wordDict)
        
        
        def dfs(j, path):
            if j == n:
                res.append(" ".join(path))
                return
            for i in range(j+1,n+1):
                word = s[j:i]
                if word in wordDict:
                    dfs(i , path + [word])

        dfs(0, [])
        return res 
