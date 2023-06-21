
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:29:47 2020

@author: liuga
"""
#BST首先想到BST
class Node(object):
    def _init_(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
        
#子链表(左右)的头结点和尾节点与母链表(root)相连        
class Solution(object):
    def doubleLinklist(self, root):
        if not root:
            return None
        
        head, tail = self.helper(root)
        return head
    
    def helper(self,root):
        head, tail = root, root
        if root.left:
            left_head, left_tail = self.helper(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
            
        if root.right:
            right_head, right_tail = self.helper(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail
            
        head.left = tail
        tail.right = head
        return head, tail
    
#建议用下面的方法
#memory complexity O(1) #用一个变量 pre，来记录上一个遍历到的结点。还需要一个变量 head，来记录最左结点，这样的话，在递归函数中，先判空，之后对左子结点调用递归，这样会先一直递归到最左结点，
#定义一个pre节点，和root双向指向。然后把pre更新到成root
class Solution2(object):
    def treeToDoublyList(self, root):
        if not root:
            return root
        self.prev = dummy = Node(-1)  #dummy.right对应头节点head ?
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.prev.right = node
            node.left = self.prev
            self.prev = node
            inorder(node.right)
            
        inorder(root)
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        
        return dummy.right

    #此解法为主
    
    #memory complexity O(1) #用一个变量 pre，来记录上一个遍历到的结点
    #此时如果 head 为空的话，说明当前就是最左结点，赋值给 head 和 pre，对于之后的遍历到的结点，那么可以和 pre 相互连接上，然后 pre 赋值为当前结点 node，再对右子结点调用递归即可
    def treeToDoublyList(self, root):
        if not root:
            return
        #head表示最左节点, pre表示上一个节点
        self.head, self.pre = None, None
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if not self.pre:  
                self.head = node
                
                self.pre = node  
            else:
                self.pre.right = node
                node.left = self.pre
                
                self.pre = node   

            inorder(node.right)  
        inorder(root) 
        self.head.left = self.pre
        self.pre.right = self.head
        
        return self.head

    

        def treeToDoublyList(self, root):
            if not root:
                return
            dummy = Node(0,None, None)
            pre = dummy
            satck, node = [], root
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                node.left, pre.right , pre = pre, node, node
                node = node.right

            dummy.right.left, pre.right = prev, dummy.right
            return dummy.right
        
    
#memory complexity O(n)
class Solution3(object):
    def treeToDoubleklist(self, root):
        if not root:
            return root

        res = []
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            res.append(node)
            inOrder(node.right)
            
        inOrder(root)
        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]
            
            
        
    
