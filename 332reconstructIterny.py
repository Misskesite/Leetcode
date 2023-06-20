# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 23:56:44 2020

@author: liuga
"""
题目中说必然存在一条有效路径(至少是半欧拉图)，所以算法不需要回溯. 如果字母序小的没有路径？(用stack,pop出来，插入更大的字典序的节点)
import collections
#从dfs开始做dfs, 每次找字典序最小的，并把用过的机票删掉，如果走到无法再走的机场，把它加到结果集
class Solution(object):
    def findIterney(self, tickets):
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        
        for frm, tos in graph.items():
            tos.sort(reverse = True)
        #tickets.sort(key = lambda x: x[1], reverse=True)
        #for j in adj: adj[i].sort(reverse = True)
        res = []
        self.dfs(graph, 'JFK', res)
        return res[::-1]
    
    def dfs(self, graph, source, res):
        while graph[source]: #下一站存在？
            v = graph[source].pop() #删除字典对应的下一站？移除排序小的的城市
            self.dfs(graph, v, res)
        res.append(source) #当前城市没有下一站，把它加到res里面
            
        
#每次递归调用删除一条边，所有子递归都返回后，再将当前节点加入结果集保证了结果集的逆序输出）
#欧拉通路（Eulerian path）
class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b
        '''
        for src, dest in tickets:
            targets[src].append(dest)
        
        for key in graph:
            targets[key].sort(reverse = True) 

        '''
        route = []
        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop()) #先弹出最右边的? 即最小的(从大到小排列)
            route.append(airport)
        dfs('JFK')
        return route[::-1]

class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      ans = []
      graph = defaultdict(list)

      for a, b in reversed(sorted(tickets)):
          graph[a].append(b)

      def dfs(u: str) -> None:
          while u in graph and graph[u]:
              dfs(graph[u].pop()) #删掉节点？（避免重复？死循环)然后遍历
          ans.append(u)

      dfs('JFK')
      return ans[::-1]
    
当我们遍历完一个节点所连的所有节点后，我们才将该节点入栈（即逆序入栈）。
对于当前节点而言，从它的每一个非「死胡同」分支出发进行深度优先搜索，都将会搜回到当前节点。而从它的「死胡同」分支出发进行深度优先搜索将不会搜回到当前节点。
也就是说当前节点的死胡同分支将会优先于其他非「死胡同」分支入栈

整个图最多存在一个死胡同(出度和入度相差1），且这个死胡同一定是最后一个访问到的，否则无法完成一笔画。
DFS的调用其实是一个拆边的过程（既每次递归调用删除一条边，所有子递归都返回后，再将当前节点加入结果集保证了结果集的逆序输出），一定是递归到这个死胡同（没有子递归可以调用）后递归函数开始返回。所以死胡同是第一个加入结果集的元素。
最后逆序的输出即可。
'''
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
'''

#回溯方法:
class Solution3(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1
                return True

            graph[cur_from].sort()
            for _ in graph[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0) #删除当前节点
                path.append(cur_to)
                if backtrack(cur_to): #进入下一层决策树
                    return True
                path.pop()            #取消选择
                ticket_dict[cur_from].append(cur_to)  #恢复当前节点
            return False
        backtrack('JFK')
        return path
                  
    
#回溯法 use a dictionary to represent the tickets (start -> [list of possible destinations]). Then, I start the route at JFK and I dfs from there.
#Since I do the dfs in sorted order, the first time that I find a possible route, I can return it and know that it is in the smallest lexigraphic order.   
    def findItinerary(self, tickets):
        d = defaultdict(list)
        for flight in tickets:
            d[flight[0]].append(flight[1])
        path = ["JFK"]
        def dfs(start):
            if len(path) == len(tickets) + 1:
                return True
            myDsts = sorted(d[start])
            for dst in myDsts:
                d[start].remove(dst)
                path.append(dst)
                if dfs(dst):                
                    return True
                path.pop()
                d[start].append(dst)
        dfs('JFK')
        return path
