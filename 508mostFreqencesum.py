# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:22:14 2020

@author: liuga
"""
import collections

class TreeNode(object):
    def _init_(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    
class Solution(object):
    def mostFrequentsubtree(self,root):
        if not root:
            return []
        vals = []
        def getsum(root):
            if not root:
                return 0
            s = getsum(root.left) + root.val + getsum(root.right)
            vals.append(s)
            return s
        
        getsum(root)
        count = collections.Counter(vals)
        frequent = max(count.values())
        return [x for x, v in count.items() if v == frequent ]


class Solution(object):
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        count = collections.Counter()

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            summ = root.val + left  + right
            count[summ] += 1
            return summ
        
        dfs(root)
        maxFreq = max(count.values())
        return [summ for summ in count if count[summ] == maxFreq]
