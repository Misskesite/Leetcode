# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:17:01 2020

@author: liuga
"""
import collections
#每个节点访问一次，时间复杂度O(n),空间复杂度O(n)跟递归深度(二叉树深度)，栈空间的大小有关
class Solution(object):
    def serialize(self, root):
         vals = []
         
         def preorder(root):
             if not root:
                 vals.append("#")
             else:
                 vals.append(str(root.val))
                 preorder(root.left)
                 preorder(root.right)
         preorder(root)
         return ' '.join(vals)

    def deserialize(self, data):
        vals = collections.deque(val for val in data.split())
        #逐个pop出 list的首项，构建出当前的根节点，顺着list构建顺序是根节点，左子树，右子树
        |1|2##|34##5##|
        def build():
            if vals:
                val = vals.popleft() 
                if val == "#":
                    return None
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root
        return build()
    
    #或者改写
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return '#,'
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ',' + leftserilized + rightserilized
    
    def deserialize(self, data):
        data = data.split(',')
        root = self.buildTree()
        return root
    
    def buildTree(self, data):
        val = data.pop(0)
        if val == "#":
            node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node
        
    
#序列化 反序列化 都是递归            
class Codec:
  def serialize(self, root: 'TreeNode') -> str:
      """Encodes a tree to a single string."""
      s = []

      def preorder(root: 'TreeNode') -> None:
          if not root:
              s.append('n')
              return

          s.append(str(root.val))
          preorder(root.left)
          preorder(root.right)

      preorder(root)
      return ' '.join(s)

  def deserialize(self, data: str) -> 'TreeNode':
    """Decodes your encoded data to tree."""
      q = deque(data.split())

      def preorder() -> 'TreeNode':
          s = q.popleft()
          if s == 'n':
              return None

          root = TreeNode(s)
          root.left = preorder()
          root.right = preorder()
          return root

      return preorder()               
                
            
            
