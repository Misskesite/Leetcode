# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:35:44 2019

@author: liuga
"""
#递归
class Solution(object):
    def sameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
    
