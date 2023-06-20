# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:42:46 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
         if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val

        return self.hasPathsum(root.left, sum - root.val) or self.hasPathsum(root.right, sum - root.val)


#非递归 栈实现 优先访问后进来的节点，导致把右子树访问结束以后才访问左子树
#栈的本质是DFS的迭代写法
class Solution2(object):
    def hasPathsum(self, root, sum):
        if not root:
            return False

        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
            
        
#BFS 队列实现
from collections import deque
class Solution3(object):
    def hasPathsum(self, root, sum):
        if not root:
            return False
        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                queue.append((node.left, path + node.left.val))
            if node.right:
                queue.append((node.right, path + node.right.val))
        return False
