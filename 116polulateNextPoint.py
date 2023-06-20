# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:37:06 2019

@author: liuga
"""

class TreeLinkNode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
            
        
class Solution(object):
    def populateRightpointer(self, root):
              
        if not root:
            return []
        
        current_level =[root]
        
        while current_level:
            next_level = []
        
            for temp in current_level:
                                
                if temp.left:
                   next_level.append(temp.left)
                   
                if temp.right:
                   next_level.append(temp.right)
                    
                for i in range(len(next_level) -1):
                    next_level[i].next = next_level[1+1]
                
            current_level = next_level

            
#BFS层次遍历
class Solution2(object):
    def connect(self, root):
        if not root:
            return root

        queue = [root]
        while queue:
            n = len(queue)
            #将队列中的元素串联起来
            tmp = queue[0]
            for i in range(1, n):
                tmp.next = queue[i]
                tmp = tmp.next # tmp = queue[i]

            for _ in range(n):
                tmp = queue.pop(0)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return root
    
#BFS改写
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        from collections import deque
        q = deque([root])
        while q:
            size = len(q)
            pre = None
            for _ in range(size):
                node = q.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

#常数辅助空间，时间复杂度O(n),空间复杂度O(1)
class Solution(object):
    def connect(self, root):
        if not root:
            return root

        cur = root
        #循环条件是当前节点的left不为空, 当只有根节点或者所有的叶子节点串联完以后就退出
        while cur.left:
            head = cur
            while head:
                #将head的左右节点串联起来
                head.left.next = head.right
                #下一个不为空说明上层已经帮我们串联了
                if head.next:
                    head.right.next = head.next.left #串联节点的父节点不同
                #指针向后移动
                head = head.next
            #从下一层的最左边开始遍历
            cur = cur.left
        return root

#模拟117改写
class Solution:
  def connect(self, root: 'Node') -> 'Node':
      node = root  # the node just above current needling

      while node and node.left:
          dummy = Node(0)  # dummy node before needling
          # needle children of node
          pre = dummy
          while node: #满二叉树，不用判断node.right是否为空？
              pre.next = node.left
              pre = pre.next
              pre.next = node.right
              pre = pre.next
              node = node.next
          node = dummy.next  # move node to the next level

    return root

    
#迭代法 时间复杂度O(n),空间复杂度O(h),h为树的高度               
class Solution3(object):
  
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root.right:
            root.left.next = root.right  #root的左右节点串起来
            if root.next:     #下一个不为空，说明上层已经串联好了
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
