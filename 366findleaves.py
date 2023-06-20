# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:59:43 2020

@author: liuga
"""
#devide and conquer
import collections

class Solution(object):
    def findleaves(self, root):
        d = collections.defaultdict(list)
        res = []
        
        def getLevel(root,d):  # return the level of the nodes
            if not root:
                return 0
            left = getLevel(root.left, d)
            right = getLevel(root.right, d)
            level = max(left, right) + 1
            d[level].append(root.val)
            return level
        
        getLevel(root, d)
        for k in sorted(d.keys()):
            res.append(d[k])        
        return res
            
            
        
class Solution2(object):
    ans = []
    def findLeaves(self, root):
        dfs(root)
        return self.ans

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        depth = 1 + max(left + right)
        if depth == len(ans):
            self.ans.append([root.val])
        else:
            self.ans[-1].append(root.val)
        return depth + 1
        
