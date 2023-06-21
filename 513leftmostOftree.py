# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:13:41 2020

@author: liuga
"""
#最底层最左边的值，层次遍历BFS 时间复杂度O(n)
class Solution(object):
    def botomLeftree(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val #队列中第一个节点的值？

from collections import deque
class Solution2(object):
    def botomLeftree(self, root):
        queue = deque()
        queue = [root]
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
