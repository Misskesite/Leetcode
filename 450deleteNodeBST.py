# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:07:26 2019

@author: liuga
"""
#难点在于删除完结点并补上那个结点的位置后还应该是一棵二叉搜索树。被删除掉的结点位置，不一定是由其的左右子结点补上
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val == key:
            if not root.right:
                left = root.left
                return left
            else: #寻找右子树的左边最小值
                node = root.right
                while node.left:
                    node = node.left
                root.val, node.val = node.val, root.val
                #交换后在之后的操作中将会把它删除

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
            

    class Solution2(object):
        def deleNode(self, root, key):    
    
            if not root: 
                return None
            
            if key < root.val:   #要删除的节点在左子树
                root.left = self.deleNode(root.left, key)
                
            elif key > root.val: #要删除的节点在右子树
                root.right = self.deleNode(root.right, key)
            else:
        	if root.left and root.right:
                    #找successor后继节点，即右子树的最左节点
        	    node = root.right
        	    while node.left:
                        node = node.left
                        
                    '''
        	    node.left = root.left  #将欲删除root左子树,成为其右子树的最左节点(node)的左子树
        	    root = root.right      #将欲删除节点的右节点顶替其位置
                    '''
                    
                    root.val = node.val
        	    root.right = self.deleNode(root.right, node.val)
        	    
        	    
        	else:
        	    if not root.left:    #无左子树
        		root = root.right
        	    elif not root.right: #无右子树
        		root = root.left
        	
            return root
