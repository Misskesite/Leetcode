# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:19:22 2019

@author: liuga
"""

class Solution(object):
    def invertbinarytree(self, root):
        if root == None:
            return root
        tmp = root.left
        root.left = self.invertbinarytree(root.right)
        root.right = self.invertbinarytree(tmp)
        return root


class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    left = root.left
    right = root.right
    root.left = self.invertTree(right)
    root.right = self.invertTree(left)
    return root
