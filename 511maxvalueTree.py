# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:24:28 2020

@author: liuga
"""
#BFS
class Solution(object):
    def maxlevelTree(self, root):
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
                    
                result.append(max(level_result))                
                current_level = next_level
                
                
        return result

#O(n)   
import collections
class Solution2:
    def largestValues(self, root):
        if not root:
            return []
        d = collections.deque()
        d.append(root)
        res = []
        
        while d:
            n = len(d)
            max_num = -2**31
            for i in range(n):
                node = d.popleft()
                if node.val > max_num:
                    max_num = node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(max_num)

        return res
