# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:43:33 2020

@author: liuga
"""
#pattern = "abab", str = "redblueredblue" return True
#backtracking暴力搜索，将它分割成所有可能的combinaion. 双hash
class Solution(object):
    def wordPattern(self, pattern, str):
        w2p, p2w = {},{}
        return self.match(pattern, str, 0, 0, w2p, p2w)

    #pattern所在的位置i, s中所在的位置j
    def match(self, pattern, str, i, j, w2p, p2w):
        flag = False
        if i == len(pattern) and j == len(str):
            flag = True #匹配完？
        while i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in p2w:
                w = p2w[p]
                if w == str[j : j+len(w)]: #match pattern
                    flag = self.match(pattern, str, i + 1, j + len(w), w2p, p2w)
            else:   
                for k in range(j, len(str)): #try every possible word
                    w = str[j: k+1]
                    if w not in w2p:
                        # Build mapping. Space: O(n + c)
                        w2p[w] = p
                        p2w[p] = w
                        flag = self.match(pattern, str, i + 1, k + 1, w2p, p2w)
                        w2p.pop(w)
                        p2w.pop(p)
                    if flag:
                        break
        return flag
    
#此解法为主 backtracking + hashmap map the char to the string.
#try to use a character in the pattern to match different length of substrings in the input string, keep trying till we go through the input string and the pattern.
#When we do the recursion, if the pattern character exists in the hash map already, we just have to see if we can use it to match the same length of the string
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        m = len(pattern)
        n = len(s)
        mp = dict()
        visited = set() #avoid duplicate mapping

        def dfs(i, j): #j is the current index of the input string
            if i == m and j == n:
                return True
            if i == m or j == n:
                return False
            for idx in range(j, n):
                sub_str = s[j:idx+1]
                if pattern[i] in mp and mp[pattern[i]] == sub_str: #If can match, so continue match the rest
                    if dfs(i+1, idx+1):
                        return True
                if pattern[i] not in mp and sub_str not in visited: #This is not mapped by other character
                    mp[pattern[i]] = sub_str
                    visited.add(sub_str) 
                    if dfs(i+1, idx+1):
                        return True

                    del mp[pattern[i]]
                    visited.remove(sub_str)

            return False
        return dfs(0,0)
    

#改写上面？ 时间复杂度|Pattern|^|s|}
class Solution(object):
    def wordPattern(self, pattern, str):
        w2p, p2w = {},{} 
        return self.match(pattern, str, 0, 0, w2p, p2w)

    #pattern所在的位置i, s中所在的位置j
    def match(self, pattern, str, i, j, w2p, p2w):
        if i == len(pattern) and j == len(str):
            return True

        if i == len(pattern) or j == len(str):
            return False
        
        while i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in p2w:
                w = p2w[p]
                if w == str[j : j+len(w)]: #match pattern
                    if self.match(pattern, str, i + 1, j + len(w), w2p, p2w):
                        return True
            else:   
                for k in range(j, len(str)): #try every possible word
                    w = str[j: k+1]
                    if w not in w2p: #w2p可以用seen set()
                        # Build mapping. Space: O(n + c)
                        w2p[w] = p # seen.add(w)
                        p2w[p] = w
                        if self.match(pattern, str, i + 1, k + 1, w2p, p2w):
                            return True
                        w2p.pop(w)
                        p2w.pop(p)
                    
        return False
        
        
#设置两个hash表来映射他们的对应关系. 然后用DFS来搜索对应关系
class Solution2(object):
    def wordPattern(self, pattern, str):
        hash1 = {}
        hash2 = {}
        return dfs(pattern, 0, str, 1)

    def dfs(self, p, k, str, len):
        plen = len(p)
        slen = len(str)
        if plen == k and slen == 0:
            return True
        if plen - k > slen or plen == k or slen == 0 or len > slen:
            return False

        if self.dfs(p ,k ,str, len+1):
            return True

        left = str[:len]
        right = str[len:]
        flag = hash1.has_key(p[k])
        if hash1.has_key(p[k]) and hash1[p[k]] != left:
            return False
        if hash2.has_key(left) and hash2[left] != p[k]:
            return False

        hash1[p[k]] = left
        hash2[left] = p[k]

        if self.dfs(p, k+1, right, 1):
            return True

        if hash1.has_key(p[k]) != flag:
            hash1.pop(p[k])
            hash2.pop(left)

        return False
            

#pattern 里的每个字母和字符串str 中每个非空 单词之间，存在着双向连接的对应规律
class Solution3(object):
    def wordPattern(self, pattern, str):
        mmap = {}
        smap = {}
        match = False
        

        def dfs(self, pattern, str, i, j):
            if (i < len(pattern) and j >= len(str)) or ( i >= len(pattern) and j < len(str)) or match:
                return

            if i == len(pattern) and j == len(str):
                macth = True
                return

            if not mmap.has_key(pattern[i]):
                for k in range(1, len(str) - j + 1): #该字符往后匹配多少个字符
                    val = str[j:k]
                    if smap_has_key(val) and smap[val] != pattern[i]: #ab aa
                        continue
                    mmap[pattern[i]] = val
                    smap[val] = pattern[i]
                    self.dfs(pattern, str, i+1, j+k) #回溯
                    mmap.pop(pattern[i])
                    smap.pop(val)
             else:
                 val = mmap[pattern[i]]
                 n = len(val)
                 if str[j: n] != val:
                     return
                 self.dfs(pattern, str, i+1, j+n)


        dfs(pattern, str, 0, 0)
        return match

def wordPatternMatch(self, pattern: str, str: str) -> bool:
        m,n = len(pattern),len(str)
        pattern_str = dict()
        visited_str = set()
        
        def helper(i,j):
            if i == m and j == n: return True
            if i == m or j == n or n - j < m - i: return False
            
            for index in range(j, n):
                sub_str = str[j:index + 1]
                if pattern[i] in pattern_str and pattern_str[pattern[i]] == sub_str:
                    if helper(i + 1,index + 1):
                        return True
                ## 我们要判断这两个字符或子串是否同时出现或者不出现，就要关注他们要一一对应的那个东西，也就是visited数组
                ## pattern中是否出现已经由pattern_str的键值存储，因此只需要保存str中是否出现
                if not pattern[i] in pattern_str and not sub_str in visited_str:
                    pattern_str[pattern[i]] = sub_str
                    visited_str.add(sub_str)
                    if helper(i + 1,index + 1):
                        return True
                    del pattern_str[pattern[i]]
                    visited_str.remove(sub_str)
                    
            return False
        
        return helper(0,0)

                        

                
