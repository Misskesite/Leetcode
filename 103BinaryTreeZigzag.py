# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:05:42 2019

@author: liuga
"""

class TreeNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
            
        
class Solution(object):
    def levelOrderZigzag(self, root):
        
        result = []
        
        if not root:
            return []
        
        current_level = [root]
            
        flag = False
        
        while current_level:
            
            level_result = []
            next_level = []
        
            for temp in current_level:
                level_result.append(temp.val)
                
                if temp.left:
                   next_level.append(temp.left)
                if temp.right:
                   next_level.append(temp.right)
                   
                if flag:
                   level_result.reverse()
                   flag = False
                   
                else:
                   flag = True                  
                    
                result.append(level_result)
                
                current_level = next_level
                
        return result
    
    
class Solution2(object):
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1: 
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    def zigzagLevelOrder(self, root):
        res = []
        self.preorder(root, 0, res)
        return res


import collections
class Solution3(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        #index = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
            
            """ index为奇数，正向输出
            if (index & 1)==1:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            index += 1
            """
        return [arr[::-1] if i%2 != 0 else arr for i, arr in enumerate(res)]
            
    
