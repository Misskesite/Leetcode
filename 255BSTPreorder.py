# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:10:24 2020

@author: liuga
"""
#[5,2,6,1,3] false  follow up: contant space?
#keep a stack of nodes of which we are still in the left subtree. If the next number is smaller than the last stack value.
# use the poped value as lower bound?
#时间复杂度O(n) 空间O(logn) 单调栈
class Solution(object):
    def preorder(self, preorder):
        stack = []
        low = float('-inf') #保存栈顶最大值？
        for n in preorder:
            if n < low:
                return False
            while stack and n > stack[-1]: #右子树？
                low = stack[-1]            #找出是哪一个节点的右子树
                stack.pop()
            stack.append(n) #比栈顶小，说明是左子树，继续压入栈
        return True
                
#当前节点的值一定大于其左子树中任何一个节点值，而且其右子树中的任何一个节点值都不能小于当前节点值
#[5 2 1 3 6] 返回True

#常数空间，利用原数组 [7,4,1,6,5,10,8,11] 
class Solution(object):
    def preorder(self, preorder):        
        low = float('-inf')
        i = -1
        for n in preorder:
            if n < low:
                return False
            while i >= 0 and n > preorder[i]:
                i -= 1
                low = preorder[i]
                
            i += 1
            preorder[i] = n
        return True
    
