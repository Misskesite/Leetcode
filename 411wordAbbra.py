# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:12:14 2020

@author: liuga
"""
# 408(valid abbrev) + 320(general abbrev)的综合
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        self.target = target
        self.size = len(target)
        self.dlist = [d for d in dictionary if len(d) == self.size]
        self.ans = target
        self.length = self.size
        self.dfs('', 0, 0)
        return self.ans
    
    def dfs(self, abbr, length, depth):
        if length > self.length:
            return
        if depth == self.size:
            for word in self.dlist:
                if self.validWordAbbreviation(word, abbr):
                    return
            self.ans = abbr
            self.length = length
            return
        self.dfs(abbr + self.target[depth], length+1, depth+1])
        if depth == 0 or not abbr[-1].isdigit():
            for x in range(2, self.size - depth +1):
                self.dfs(abbr + str(x), length+1, depth+x)
                
    def validWordAbbreviation(self, word, abbr):
        size = len(word)
        cnt = loc = 0
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt*10 + int(w)
            else:
                loc += cnt
                cnt = 0
                if loc >= size or word[loc] != w:
                    return False
                loc += 1
        return loc + cnt == size
    
        
#此解法为主            
class Solution2:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)
        if n == 0:
            return ""
        
        if all(len(s) != n for s in dictionary): 
            return str(n)   

        dictionary = set(word for word in dictionary if len(word) == len(target))
        
        q = self.generateAbbreviate(target)
        
        q.sort(key= len)

        for w in q:
            if all(not self.check_ambiguity(w, word) for word in dictionary):
                return "".join(w)
        return target
    


    def generateAbbreviate(self, word):
        res = []
        
        def helper(i, tmp, cnt):
            #cnt代表前面记录了多少数字
            if i == len(word):
                if cnt > 0:            #cnt为0时不能拼接
                    tmp = tmp + str(cnt)
                res.append(tmp)
                return 
            else:
                #不用word[i]
                helper(i+1, tmp, cnt+1) #累加已经省略的数字+1
                #用word[i]
                helper(i+1, tmp + (str(cnt) if cnt > 0 else "") + word[i], 0) #省略掉的字符从0开始
        helper(0, "", 0)
        return res

    #1l3 -> blade
    def check_ambiguity(self, abbr, word):
        n = len(word)
        cnt = i = 0
        
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt*10 + int(w) #abbr是string
            else:
                i += cnt
                cnt = 0
                
                if i >= n or word[i] != w:
                    return False
                i += 1
        return i + cnt == n




#改写
class Solution3(object):
    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        abbr = []
        dictionary = set(dictionary)
        self.generateAbbreviate(target, 0, [], 0, abbr)
        abbr.sort(key = len)  #5 a4 4e ap3
        for w in abbr:
            if all(not self.check_ambiguity(w, word) for word in dictioanry):
                return "".join(w)
        return target
           
        
        
    def generateAbbreviate(self, s, pos, path, cnt, ans):
        if pos == len(s):
            ans.append(path + [str(cnt)] if cnt else path) #注意这里用的是列表，不是str [str(cnt)]
            return
        self.generateAbbreviate(s, pos+1, path +([str(cnt)] if cnt else []) + s[pos], 0, ans)
        self.generateAbbreviate(s, post+1, path, cnt+1, ans)

    def check_ambiguity(self, abbr, s):
        #O(max(len(abbr), len(s)) decide if abbr can be an abbrivation of s. compare letter by letter
        i = j = 0
        while True:
            if i == len(abbr) and j == len(s):
                return True
            if i >= len(abbr) or j >= len(s):
                return False
            if abbr[i].isdigit(): #abbr[i] 存的是12
                step = int(abbr[i])
                i += 1
                j += step #jump
            else:
                if abbr[i] != s[j]:
                    return False
                i += 1
                j += 1
        return True
