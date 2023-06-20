# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:04:24 2020

@author: liuga
"""
#Time O(h) h为树的高度 Space O(1)
class Solution(object):
    def inordersuccessor(self, root,p):
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right #不用更新，要么之前已找到更小的结果，要么还没找到比p值更大的节点
        return ans


class Solution2(object):
    def inordersuccessor(self, root, p):
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)

        inorder(root)
        for i in range(len(res)):
            if res[i] == p :
                return res[i+1] if i+1 < len(res) else None

class Solution:
  def inorderSuccessor(self, root: Optional[TreeNode], p: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
          return None
      if root.val <= p.val:
          return self.inorderSuccessor(root.right, p)
      return self.inorderSuccessor(root.left, p) or root
