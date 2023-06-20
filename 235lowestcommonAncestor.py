# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:54:53 2020

@author: liuga
"""
#如果两节点都小于根节点，说明都在根节点的子树上，往左子树找。都大于说明在根节点的右子树上
#如果一个大于，一个小于，说明一个在根节点的左子树，一个在右子树。那根节点是他们最近的公共祖先
class Solution(object):
    def lowestAncestor(self, root, p, q):
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestAncestor(root.left, p, q)
        elif  p.val > root.val and q.val > root.val:
            return self.lowestAncestor(root.right, p, q)
        else:
             return root
            
'''
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root

'''
         

class Solution2(object):
    def lowestAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0: #说明2节点在同一侧
            root = p.val < root.val ? root.left : root.right
        return root
        


    def lowestCommonAncestor(self, root, p, q):
        pointer = root
        while pointer:
            if p.val > pointer.val and p.val > pointer.val:
                pointer = pointer.right
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            else:
                return pointer
            
            
