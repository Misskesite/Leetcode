# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:03:20 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
    
#用栈把递归转化为迭代，栈中只保留左节点
#时间复杂度O(1), 空间复杂度O(h) h为树的高度
class Solution(object):
    def _init_(self, root):
        self.stack = []
        self._pushleft(root)
        
    def hasNext(self):
        return self.stack
    
    def next(self):
        node = self.stack.pop()
        self._pushleft(node.right) #如果栈顶元素有右子树，则把所有右边节点的左孩子放在栈中
        return node.val
    
    def _pushleft(self, node):
        while node:
            self.stack.append(node)
            node = node.left #左节点一直入栈
            
#时间复杂度O(n), 空间复杂度O(n)       
import collections
class Solution(object):
    def BSTIterator(object):
        def _init_(self, root):
            self.queue = collections.deque()
            self.inOrder(root)

        def inOrder(self, root):
            if not root:
                return

            self.inOrder(root.left)
            self.queue.append(root.val)
            self.inOrder(root.right)

        def next(self): #O(1)
            return self.queue.popleft()

        def hashNext(self):
            return len(self.queue) > 0
        
    

