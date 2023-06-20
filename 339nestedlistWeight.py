# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:26:26 2020

@author: liuga
"""

class Solution(object):
    def nestedListWeight(self, nestList):
        depth, ans = 1, 0
        while nestList:
            ans += depth*sum([i.getInteger() for i in nestList if i.isInteger()])
            newlist = []
            for i in nestList:
                if not i.isInteger():
                    newlist += i.getInteger()
            nestList = newlist
            depth += 1
        return ans
        
#we traversal all elements, so time complexity is O(n)
class Solution2(object):
    def DFS(nestedList, depth):
        ans = 0
        for elem in nestedList:
            if elem.isInteger():
                ans += elem.getInteger()* depth
            else:
                ans += DFS(elem.getList(), depth+1) #嵌套链表的一维数组直接当做一个嵌套链表的对象
        return ans
    return DFS(nestedList, 1)
        
