# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:17:43 2019

@author: liuga
"""
#递归方法 时间复杂度O(n) 用到了递归调用，空间复杂度O(h), h为树的高度
#相邻的2个节点调换，非相邻的2个节点调换。
#中序遍历，结果中如果有一个降序对，说明该两个node需交换；若有两个降序对，说明第一对的前一个node和第二对的后一个node需要交换
class Solution(object):
    def recoverTree(self,root):
        
        self.pre, self.first, self.second = None, None, None
        
        self.findDefect(root)
        
        self.first.value, self.second.value = self.second.value, self.first.value
        
        def findDefect(self, root):
            if not root:
                return
            
            self.findDefect(root.left)
            
            #pre用来比较相邻两个值的大小关系, 上一个节点(pre)和当前节点的值，如果pre的值大于当前节点值，则记录下这两个节点
            if self.pre and self.pre.val > root.val: #当前节点前面有节点
                
                if not self.first:                   #说明是第一个有问题的节点？                
                    self.first = self.pre            #初始标记第一个有问题的节点

                self.second = root

            """
               1 2 3 7 5 6 4
               7 < 5    6 < 4
               if not self.first and self.pre.val >= root.val: #当前是第一对错误
                  self.first = self.pre  #7  记录第一个错误点

               if self.first and self.pre.val >= root.val: #第一个错误点已确定
                  self.second = root     #4  记录第二个错误点
            """ 
                                
            self.pre = root                          #中序遍历，一直更新pre            
            self.findDefect(root.right)


#迭代方法
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            #输出栈顶元素
            p = stack.pop()
            
            if not firstNode and pre.val > p.val:
                    firstNode = pre
                    
            if firstNode and pre.val > p.val:
                
                secondNode = p
                
            pre = p
            #看右子树
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val

            
#Morris遍历 O(1)空间复杂度, 叶子节点2的右子树指向上上个节点3？ 找根节点的左子树的最右节点
class Solution(object):
    def recoverTree(self, root):
        x = None
        y = None
        pre, tmp = None, None

        while root:
            if root.left:
                #寻找左子树最右节点(也可以是左子树根节点)
                tmp = root.left 
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                    
                if tmp.right is None: #搭桥，直接找到root,将右节点指向root,开始遍历root的左子树
                    tmp.right = root
                    root = root.left

                else: #左子树遍历完，遍历root节点。存在说明之前已经搭好桥了，这一步要拆桥还原树结构
                    if pre and pre.val > root.val:
                        y = root
                        if not x:
                            x = pre
                            
                    pre = root                    
                    root = root.right
                    #断开前驱节点和
                    tmp.right = None  

            else:
                #无左子树，遍历当前的root 遍历中的比较部分,再继续遍历右子树
                if pre and pre.val > root.val:
                    
                    if not x:
                        x = pre
                    y = root
                    
                pre = root
                root = root.right
                
        if x and y:
            x.val, y.val = y.val, x.val
            
                    
            
