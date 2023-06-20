# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:23:51 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
            
        
class Solution(object):
    def levelOrder2(self, root):
        
        result = []
        
        if not root:
            return []
        
        current_level = [root]
        
        while current_level:
                
            level_result = []
            next_level = []
        
            for temp in current_level:
                level_result.append(temp.val)
                
                if temp.left:
                   next_level.append(temp.left)
                if temp.right:
                   next_level.append(temp.right)
                    
                result.append(level_result)                
                current_level = next_level
                
                result.reverse()
                
        return result


#时间复杂度O(n), 空间复杂度O(n),n是节点个数，每个节点访问一次，空间复杂度取决于队列开销
import collections
class Solution2(object):
    def levelOrder(self, root):
        res = []
        if not root: 
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]
