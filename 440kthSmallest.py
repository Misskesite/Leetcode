# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:41:13 2020

@author: liuga
"""
#DFS会超时，这里用数学方法 n = 13, k = 2 -> 10
class Solution(object):
    def kthSmallest(self, n, k):
        cur = 1
        k -= 1 #需要移动k-1位，到达k位
        while k > 0:
            step, first, last = 0, cur, cur + 1
            while first <= n:
                step += min(last, n+1) - first #一次性求出下一层节点个数和，没有满就用n来减
                #进入下一层
                first *= 10
                last *= 10
            if step <= k:
                k -= step #跳过全部
                cur += 1  #向右移一位
            else:
                
                k -= 1    #跳过当前的节点
                cur *= 10 #往下走一层
                
        return cur
                
#改写 
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def fn(x):  #getSteps
            """Return node counts in denary trie."""
            ans, diff = 0, 1
            while x <= n: 
                ans += min(n - x + 1, diff) #Steps
                x *= 10 
                diff *= 10 
            return ans
        '''
            ans = 0
            first = x
            last = x + 1
            while first <= n: 
                ans += min(n + 1, last) - first #Steps
                first *= 10 
                last *= 10 
            return ans

        '''
        
        x = 1
        while k > 1: 
            cnt = fn(x)
            if k > cnt:
                k -= cnt
                x += 1
            else:
                k -= 1
                x *= 10 
         return x

#n: 13  k: 2 10 先序遍历十叉树
        
    
#dfs 如果n特别大，构建整棵树不现实。 通过计算得到某个节点下的子树节点的总数而跳过遍历的时间
class Solution(object):
    def findKthNumber(self, n ,k):
        def dfs(l, r): 
            if  l > n:
                return 0
            else:
                return min(n, r) - l + 1 + dfs(l*10, r*10 + 9)

        cur = 1
        k -= 1
        while k :
            cnts = dfs(cur, cur)
            if cnts <= k :
                k -= cnts
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
