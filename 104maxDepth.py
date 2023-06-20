# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:19:45 2019

@author: liuga
"""

class Solution(object):
    def maxdepth(self, root):
        if not root:
            return 0
        return max(self.maxdepth(root.left), self.maxdepth(self.right)) + 1
