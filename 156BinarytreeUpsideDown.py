# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:26:20 2019

@author: liuga
"""
#迭代 从上到下 parent is previous node,遍历左节点的父节点 从上往下开始翻转，直至翻转到最左子节点
class Solution(object):
    def upsideDownBT(self, root):
        cur, pre, tmp, next = root, None, None, None
        
        while cur:
            next = cur.left
            cur.left = tmp #prev_right
            tmp = cur.right
            cur.right = pre
            pre = cur
            cur = next
        return pre

class Solution:
  def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      prevRoot = None
      prevRightChild = None

      while root:
          nextRoot = root.left  # cache next root
          root.left = prevRightChild
          prevRightChild = root.right
          root.right = prevRoot
          prevRoot = root  # record previous root
          root = nextRoot  # update root

      return prevRoot

#递归 不停的对左子节点(左链)调用递归函数，直到到达最左子节点开始翻转，翻转好最左子节点后，
#开始回到上一个左子节点继续翻转即可，直至翻转完整棵树，时间复杂度O(n)
#原二叉树的最左子节点变成了根节点，其对应的右节点变成了其左子节点，其父节点变成了其右子节点
class Solution2(object):
    def upsideDownBT(self, root):
        if not root or not root.left:
            return root

        l = root.left
        r = root.right
        newRoot = upsideDownBT(l) #l is new root every time
        #右孩子不用处理，因为要么不存在，要么是叶子节点
        l.left = r     #同宗兄弟变成左支
        l.right = root #父节点变成新root右节点(叶子节点)
        root.left = None #断开
        root.right = None #断开
        return newRoot

        
'''
        newRoot = upsideDownBT(root.left) #is new root every time
        #右孩子不用处理，因为要么不存在，要么是叶子节点
        root.left.left = root.right     #同宗兄弟变成左支
        root.left.right = root #父节点变成新root右节点(叶子节点)
        root.left = None #断开
        root.right = None #断开

'''
#最左端 变成root节点，父节点变成右节点，兄弟节点变成右节点。
