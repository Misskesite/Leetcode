# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:01:07 2020

@author: liuga
""" [1, 2, 3] 对应的边(1,2) (2,3)
#Topological Sort, 先构建一个有向图g。然后indeg计算入度，sucset记录各顶点的后继（边）
#对g执行拓扑排序，将排序结果与原始org做对比
#org: [1,2,3], seqs: [[1,2],[1,3],[2,3]] 输出True


#此解法为主
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        s = set([i for seq in sequences for i in seq])
        if len(s) != len(nums):
            return False
        n = len(nums)
        graph = [[] for _ in range(n+1)] #array更省时间
        indegree = [0 for _ in range(n+1)]
        '''
        graph = {x: [] for x in s}
        indegree = {x: 0 for x in s}
        '''

        #construct the dependency graph using seqs
        for seq in sequences:
            for s, t in zip(seq, seq[1:]):
                graph[s].append(t)
                indegree[t] += 1         

        queue = deque(node for node in nums if indegree[node] == 0)

        #topological sorting on the dependency graph
        order = []
        while queue:
            if len(queue) != 1: #check whether there is only one option to select the node
                return False
            node = queue.pop()
            order.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if not indegree[next_node]:
                    queue.append(next_node)
        return nums == order #getting the topological sorted node list, check whether it is the same with numbers
    
class Solution:
  def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        s = set([i for seq in sequences for i in seq])
        if len(s) != len(nums):
            return False
        
        graph = {x: [] for x in s}
        indegree = {x: 0 for x in s}

        #construct the dependency graph using seqs
        for seq in sequences:
            for s, t in zip(seq, seq[1:]):
                graph[s].append(t)
                indegree[t] += 1         

        queue = deque(node for node in nums if indegree[node] == 0)

        #topological sorting on the dependency graph
        order = []
        while queue:
            if len(queue) != 1: #check whether there is only one option to select the node
                return False
            node = queue.pop()
            order.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if not indegree[next_node]:
                    queue.append(next_node)
        return nums == order #getting the topological sorted node list, check whether it is the same with numbers
    
   

#org: [1,2,3], seqs: [[1,2],[1,3]] false, 因为[1,3,2] is also valid sequence
#判断是否有且仅有一个能从 seqs重构出来的父序列org (seqs里面都是它的子序列)
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        #edge case handle
        nodes = reduce(set.union, seqs, set()) #对参数列表中的元素进行累积(聚合) reduce(function, iterable[, initializer(初始值)])
        if nodes != set(org): #顶点不相同？ 类似上面的u, v 不在数字范围内
            return False

        #graphic process
        n = len(org)
        indegree = [0 for _ in range(n+1)]  
        out_edges = [[] for _in range(n+1)] #注意可能有重复sequence，所以用list

        for seq in seqs:
            for f, t in zip(seq, seq[1:]):
                out_edges[f].append(t)
                indegree[t] += 1            #有重复的seq，度会变大

        #bfs search to find the unqiue topological sort order
        queue = [node for node in org if indegree[node] == 0]
        order = []
        while queue:
            if len(queue) != 1: #拓扑排序队列里面的值为1，才是唯一拓扑排序
                return False
            node = queue.pop()
            order.append(node)
            for next_node in out_edges[node]:
                indegree[next_node] -= 1
                if not indegree[next_node]:
                    queue.append(next_node)
        return org == order
        
                

    
#首先建立原始序列org中各元素到其下标的映射indexes, 最后遍历org，判断其中两两相邻元素构成的边是否都在edges中，若是返回True，否则返回False。           
#org: [1,2,3], seqs: [[1,2],[1,3]] false        
#check boundary
class Solution2(object):
    def sequenceReconstruction(self, org, seqs):
        index = {e:i for i,e in enumerate(org)}
        edges = set()
        
        if not seqs:
            return False
        for seq in seqs:
            for s in seq:
                if s not in index:
                    return False
            for i in range(1,len(seq)):
                pre, cur = seq[i-1], seq[i]
                if index[pre] > index[cur]:
                    return False
                edges.add((pre,cur))
                
        for x in range(1, len(org)):
            if (org[x-1],org[x]) not in edges: #(2, 3) no in edges
                return False
        return True


'''
the difficulty of this question lies in the details, so we have to do it several times.

detail 1 ： since the numbers in the subsequence can be any number, the degree sum graph should use a dictionary instead of a fixed-length array. 。 add new numbers in real time as you traverse all subsequences.

detail 2 ： requires that the result of the topological sort is unique, so whenever the queue queue there is only one number in it.

details 3 ： the order of the numbers taken from the queue should exactly match the order of the numbers in the original sequence.

detail 4 ： the total number of numbers that appear in the subsequence may be more than the original sequence, so beware of numeric subscript overflow
