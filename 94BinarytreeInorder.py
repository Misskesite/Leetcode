# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:12:40 2019

@author: liuga
"""
#递归
class Solution(object):
    def inorderTraversal(self, root):
        answer = []
        
        def inorder(root):
            if root == None:
                return None
            
            if root.left != None:
               inorder(root.left)
               
            answer.append(root.value)
               
            if root.right != None:
                inorder(root.right)
                
        inorder(root)
                
        return answer
                
                 
#迭代 栈实现  时间复杂度O(n), 空间复杂度O(h)
class Solution2(object):
    def inorderTraversal(self, root):
        
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()     #也可以写成 root = stack.pop()  root = root.right
                res.append(node.val)   #保存弹出的节点
                root = node.right #转向右节点，继续上面的过程(while root)
        
        return res


#复杂一点的写法
    def inorderTraversal2(self, root):
        
        res = []
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:    
            node = stack.pop()    #栈顶的节点出栈
            res.append(node.val)  #处理数值部分  
            node = node.right     #获取它的右子树
            while node:
                stack.append(node) #压入当前的右子树的root
                node = node.left   #不断压入左子节点
        return res



#莫里斯遍历, 二叉树改为链表
class Solution(object):
    def inOrdertraversal(self, root):
        res = []
        pre = None
        while root:
            #如果左节点不为空，就将当前节点连带右子树全部挂到左节点的最右子树下面
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                #root 指向root left
                tmp = root
                root = root.left
                tmp.left = None
            #左子树为空则打印这个节点，并向右遍历
            else:
                res.append(root.val)
                root = root.right
        return res
                
        
