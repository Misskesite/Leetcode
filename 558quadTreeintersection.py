# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:54:59 2020

@author: liuga
"""
#
class Node(object):
    def _init_(self, val, isleaf, topleft, topright, botleft, botright):
        self.val = val
        self.isleaf = isleaf
        self.topleft = topleft
        self.topright = topright
        self.botleft = botleft
        self.botright = botright
        
    
class Solution(object):
    def intersect(self, q1, q2):
        if q1.isleaf: #一个叶子节点，如果全为1(true)，直接True(因为是或运算)
            return q1 if q1.val else q2 #即使q2不是叶子节点，也直接返回
        if q2.isleaf:
            return q2 if q2.val else q1
        
        #A,B 都不为叶子节点的情况，分别递归获取四个方向的子节点
        q1.topleft = self.intersect(q1.topleft, q2.topleft)
        q1.topright = self.intersect(q1.topright, q2.topright)
        q1.botleft = self.intersect(q1.botleft, q2.botleft)
        q1.botright = self.intersect(q1.botright, q2.botright)

        #四个都是叶子节点，值一样，都是1或者0 合并？
        if q1.topleft.isleaf and q1.topright.isleaf and q1.botleft.isleaf and q1.topright.isleaf:
            if q1.topleft.val == q1.topright.val ==  q1.botleft.val == q1.botright.val:
                q1.isleaf = True
                q1.val = q1.topleft.val
        return q1 #如果不是叶子节点，value无所谓

'''    
Combine two leaves according the logical OR of their values.
If one node is a leaf then return it if it is True, else return the other node.
If neither are leaves, intersect each of the 4 subtree children and return a leaf if they are all leaves with the same value, or else return a non-leaf with value of False.
'''
def intersect(self, quadTree1, quadTree2):
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        children = [topLeft, topRight, bottomLeft, bottomRight]
        values = [child.val for child in children]
        leaves = [child.isLeaf for child in children]

        if all(leaves) and (sum(values) == 0 or sum(values) == 4): #都是叶子节点，0 或者 1
            return Node(topLeft.val, True, None, None, None, None)

        # non-leaf must have False val
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
