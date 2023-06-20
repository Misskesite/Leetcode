# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 21:02:52 2019

@author: liuga
"""


#dfs算法
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        edges = collections.defaultdict(list)
        visited = [0]*numCourses
        result = []
        valid = True
        
        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u):
            nonlocal valid #外层变量（外层函数的局部变量，而且不能是全局变量）
            visited[u]=1
            for v in edges[u]:
                #未搜索
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] =2
            result.append(u)
            
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        if not valid:
            return list()
        
        return result[::-1]
            
        
#dfs步骤，1.构建逆邻接表，2.递归处理每一个没访问的结点(先输出指向它的所有顶点，再输出自己)
#3 访问一个结点时，先递归访问它的前驱结点，直到前驱结点没有前驱结点为止
class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        n = len(prerequisites)
        if n == 0:
            return [i for i in range(numCourses)]
        #逆邻接表
        adjacency = [set() for _ in range(numCourses)]
        
        visited = [0 for _ in range(numCourses)]
        res = []
        
        for cur, pre in prerequisites:
            adjacency[cur].append(pre)

            
        def dfs(i): #返回是否有环
            if visited[i] == 2:
                #2表示正在访问， 如果dfs时遇到一样的节点，表示有环
                return True
            
            if visited[i] == 1: 
                return False
            
            visited[i] = 2
            
            #递归访问前驱节点
            for j in adjacency[i]:
                #没有环就返回false
                #执行以后，逆拓扑序列就存在 res 中
                if dfs(j): 
                    return True
                
            #执行到这里，说明所有的前驱节点都访问完了，可以输出了。将这个结点状态设置为1
            visited[i] = 1
            
            #先把i节点的所有前驱节点都输出之后，再输出自己
            res.append(i)
            return False #表示无环
        
            
        for i in range(numCourses):
            if dfs(i): 
                return []
        return res


#拓扑排序 numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 输出[0 2 1 3]
#拓扑排序是广度优先和贪心算法在有向图的应用.如果有多种答案，返回任意一种 贪的点是：当前让入度为 0 的那些结点入队；
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        n = len(prerequisites)
        if n == 0: #没有prerequisites 边？包含节点，但是没有边，任何一种编号的排序都是拓扑排序
            return [i for i in range(numCourses)]
        
        in_degree = [0 for _ in range(numCourses)]
        
        #邻接表 重复被删除. adj可以用字典collections.defaultdict(set)
        adj = [set() for _ in range(numCourses)]

        for cur, pre in prerequisits:
            in_degree[cur] += 1
            adj[pre].add(cur)  #set方法 add, remove

        #入度为0的节点入队
        res = []
        queue = []
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            top = queue.pop(0)
            res.append(top)

            for successor in adj[top]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)
        #队列为空时 检查顶点个数是否和课程数相等
        if len(res) != numCourses:
            return []

        return res
            
#此法为主
class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    ans = []
    graph = [[] for _ in range(numCourses)]
    inDegree = [0] * numCourses
    q = deque()

    # build graph
    for v, u in prerequisites:
        graph[u].append(v)
        inDegree[v] += 1

    # topology
    for i, degree in enumerate(inDegree):
        if degree == 0:
            q.append(i)

    while q:
        u = q.popleft()
        ans.append(u)
        for v in graph[u]:
            inDegree[v] -= 1
            if inDegree[v] == 0:
                q.append(v)

    return ans if len(ans) == numCourses else []
