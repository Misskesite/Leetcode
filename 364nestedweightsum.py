# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:47:55 2020

@author: liuga
"""
#DFS 建立二维数组？
class Solution(object):   
    
    def depthSumInverse(nestedlist):
        res = 0
        v = []
        
        def dfs(ni, depth, v):
            if depth > len(v):
                v.resize(depth + 1)
            if ni.isInteger():
                v[depth] += ni.getInteger()
            else:
                for a in ni.getList():
                    dfs(a, depth+1, v)
                
        for a in nestedlist:
            dfs(a, 0, v)
        for i in range(len(v),-1,-1):
            res += v[i]*(len(v)-i)
        
        return res
    
    
#[[1,1],2,[1,1]] 返回8 2*2 + 1* 4 = 8
def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, list_sum):
            temp_list = []
            for elem in nestedList:
                if elem.isInteger():
                    list_sum += elem.getInteger()
                else:
                    temp_list += elem.getList()
            if len(temp_list) != 0:
                list_sum += dfs(temp_list, list_sum)
            return list_sum
        return dfs(nestedList, 0)    

#BFS 此解法为主
class Solution2(object):
    def depthSumInverse(self, nestedList):
        res = 0
        presum = 0
        q = deque(nestedList)

        while q:
            for i in range(len(q)):
                e = q.popleft()
            
                if e.isInteger():
                    presum += e.getInteger()
                else:
                    for ni in e.getList():
                        q.append(ni)

            
            res += presum  #第一层的权重和(2)加了2次
        return res

    

#计算深度，调用339的方法       
class Solution:
    def NestedListWeightSum2(self, nestedList):
        def maxDepth(nestedList, depth):
            ans = 0
            for each in nestedList:
                if each.isInteger():
                    ans = max(ans, depth)
                else:
                    ans = max(ans, maxDepth(each.getList(), depth + 1))
            return ans
        def helper(nestedList, depth):
            s = 0
            for each in nestedList:
                if each.isInteger():
                    s += each.getInteger() * depth
                else:
                    s += helper(each.getList(), depth -1)
                return s
        return helper(nestedList, maxDepth(nestedList, 1))
