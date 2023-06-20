# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:17:41 2020

@author: liuga
"""
#栈写法 有连续的##说明是叶子节点 这是完整二叉树，只包括度为0和2的二叉树
#"9,3,4,#,#,1,#,#,2,#,6,#,#" 遇到x,#,#把它变成#
class Solution(object):
    def verifyPreorder(self, preorder):
        stack = []
        for node in preorder.spilt('.'):
            stack.append(node)
            while len(stack)>= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack.pop()== '#' #stack == ['#']


def isValidSerialization(self, preorder):
    stack = []
    for value in preorder.split(','):
        if value == '#':
            while len(stack) >= 2 and stack[-1] == '#' and stack[-2] != '#':
                stack.pop()
                stack.pop()
        stack.append(value)
    return stack == ['#']

#类似297 The trick is to add elements one by one and when we see num, #, #, we replace it with #. If we get just one # in the end, return True,
class Solution:
    def isValidSerialization(self, preorder):
        stack = []
        for elem in preorder.split(","):
            stack.append(elem)
            while len(stack) > 2 and stack[-2:] == ["#"]*2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            
        return stack == ["#"]
    
#diff = outdegree – indegree. 当一个节点出现的时候，diff – 1，因为它提供一个入度；当节点不是#的时候，diff+2(提供两个出度)    
#在图里出度和等于入度和。空节点# 0个出度，1个入度。每个非空节点，2个出度，一个入度(根节点入度为0)
#每个节点累加 diff = 出度-入度，遍历到任何一个节点 diff>= 0
class Solution2(object):
    def isValidSerialization(self, preorder):
        nodes = preorder.split(',')
        diff = 1   #diff的初始化为1
        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0

    #二叉树是图，看成有向图，一条有向边带来一个入度和一个出度。二叉树的总入度等于总出度，也等于边数
    def isValidSerializ(self, preorder):
        if preorder == "#":
            return True
        
        indegree , outdegree = 0 , 0 # 初始 入度出度
        nodes = preorder.split(",")  # 转成数组
        n = len(nodes)
        
        if n > 1 and nodes[0] == "#":
            return False

        for i in range(n):
            if i == 0:                
                outdegree += 2 //根节点 出度+2
            elif nodes[i] == "#":
                indegree += 1
            else:
                indegree += 1
                outdegree += 2

            if i != n-1 and indegree >= outdegree:
                return False #一直保持indegree<outdegree，直到最后才indegree==outdegree，做不到就return false

        return indegree == outdegree
'''
Initially we have one ( for the root ).

for each node we check if we still have empty slots to put it in.

a null node occupies one slot.
a non-null node occupies one slot before he creates two more. the net gain is one.
