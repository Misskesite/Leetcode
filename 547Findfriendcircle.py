# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:13:11 2020

@author: liuga
"""

class Solution(object):
    def findCircle(self, m):
        dsu = DSU()
        n = len(m)
        for i in range(n):
            for j in range(i,n):
                if m[i][j]:
                    dsu.u(i,j)
        res = 0
        for i in range(n):
            if dsu.f(i) == i:
                res += 1
        return res
    
class DSU(object):
    def _init_(self):
        self.d = range(201) 
        self.r = [0]*201
        
    def f(self,a):
        return a if a == self.d[a] else self.f(self.d[a]) 
    
    def u(self,a,b):
        pa = self.f(a)
        pb = self.f(b)
        if pa == pb:
            return
        if self.r[pa] < self.r[pb]:
            self.d[pa] = pb
            self.r[pb] += self.r[pa]
        else:
            self.d[pb] = pa
            self.r[pa] += self.r[pb]


class Solution(object):
    def findCircleNum(self, isConnected):
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1, index2):
            parent[find(index1)] = find(index2)

        n = len(isConnected)
        parent = list(range(n))

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(n))
        return circles
                    
     
#bfs
from collections import deque
class Solution2(object):
    def findCirclenumber(self, M):
        N = len(M)
        visited = set()
        res = 0
        
        for i in range(N):
            if i not in visited:
                queue = [i]
                while queue:
                    j = queue.pop(0)
                    if j not in visited:
                        visited.add(j)
                        #enumerate函数用于将可遍历的数据对象(列表，元组，矩阵，数组)组合为索引序列
                        queue += [k for k, num in enumerate(M[j]) if num and k not in visited]
                res += 1
        return res
    
    def findCircleNum2(self, M):                             
        cnt, N = 0, len(M)
        visited = set()

        for i in range(N):
            if i not in visited:
                q = collections.deque([i])
                visited.add(i)
                while q:
                    j = q.popleft()                    
                    for k in range(N):
                        #未被访问过且是邻接点,注意是node的邻接点
                        if M[j][k] and k not in visited:
                            visited.add(k)
                            q.append(k)
        
                cnt += 1
                
        return cnt　

#DFS We are using DFS to find the student's friend and student's friend's friend and so on and 
#store them as one friend circle. if other studnts are in the circle, then we skip until we find
#another student not in the circle. the other student will start another circle
#时间复杂度O(N*N) 空间复杂度O(N)
class Solution3(object):
    def findCircleNum(self, M):
        
        cnt, n = 0, len(M)
        visited = set()
        
        def dfs(i):
            #这里需要添加一句 visit.add(i)？ 也可以不添加 M[i][i] = 1 后面会添加？
            for j in range(N):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                    
        for i in range(N):
            if i not in visited:                
                dfs(i)
                cnt += 1                
        return cnt
    
    #此法为主
    def findCircleNum2(self, M):
            visited = set()
            count = 0
            def dfs(student, visited):
                for class_mate, is_friend in enumerate(M[student]):
                    if class_mate not in visited and is_friend:
                        visited.add(class_mate)
                        dfs(class_mate, visited)
                        
            for student in range(len(M)):
                if student not in visited:
                    visited.add(student)
                    dfs(student, visited)
                    
                    count += 1
            return count
