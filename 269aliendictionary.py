# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:44:58 2020

@author: liuga
"""
#此题为准
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ""
        
        adj_list = collections.defaultdict(set)

        indegree = {ch:0 for word in words for ch in word}
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                        indegree[c2] += 1
                    break
                #没有跳出一直相等
                if len(w1) > len(w2) and j == minLen-1: #check if second word is prefix of first word
                    return ""
                
        q = collections.deque()            
        for k, v in indegree.items():
            if v == 0:
                q.append(k)
        
        ans = ""
         
        while q:
            c = q.popleft()
            ans += str(c)
            for d in adj_list[c]:
                indegree[d] -= 1
                if indegree[d] == 0 :
                    q.append(d)
        
        if len(ans) < len(indegree):
            return ""
        else:            
            return ans

                
            
#BFS
import collections
class Solution(object):
    def alienOrder(self, words):
        #构建邻接表，入度
        adj_list = collections.defaultdict(set)

        indegrees = {ch:0 for word in words for ch in word}

        #construct the grapgh and indegrees
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: #避免indegree of d will be repeatedly added
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                break #  Later characters' order are meaningless  避免["wrt","wrf","er","ett","rftt","te"] r->t重复加入，也要跳出，break位置提前

            else: # it match the final if of the for loop（only when all above pairs match(c == d?), the "else" will run）
                #edge case - no order: ["wrtkj","wrt"] 1:next stop at end 2: cur still have lefts
                    #check if second word is prefix of first word
                if len(second_word) < len(first_word):
                    return ''
        '''
    for first, second in zip(words, words[1:]):
      length = min(len(first), len(second))
      for j in range(length):
        u = first[j]
        v = second[j]
        if u != v:
          if v not in graph[u]:
            graph[u].add(v)
            inDegree[ord(v) - ord('a')] += 1
          break  # Later characters' order are meaningless
        # First = 'ab', second = 'a' . invalid
        if j == length - 1 and len(first) > len(second):
          graph.clear()
          return

        '''

        q = collections.deque()
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)


        ans = []
        while q :
            c = q.popleft()
            ans.append(c)
            for d in adj_list[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0 :
                    q.append(d)
        #可以判断indegee是不是都为0
        '''
        for k. v in indegree.items():
            if v != 0:
                return ""

        '''
        #进入ans的字符indegee都是0， there are letters not appear in output(ans)
        if len(ans) < len(indegrees):
            return ''

        return "".join(ans)
                    

#DFS
    def alienOrder(self, words):
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    adj_list[c1].add(c2)
                    break

        visited = {}
        res = []

        def dfs(c): #check if there is loop
            if c in visited:
                return visited[c]

            visited[c]= True
            for nei in addj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
