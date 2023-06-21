# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:21:46 2020

@author: liuga
"""
#先修改比较大的节点，保证顺序是 右->中->左 扩展follow up：Morris 遍历(常数空间)
class Treenode(object):
    def _init_(self,x):
        self.val = x
        self.left = None
        self.right = None
        
#当递归到最右时，我们终止递归，开始累加这条路径上的所有节点值，即，当前节点值累加全局变量的值并更新全局变量的值为累加后的值        
class Solution(object):
    def convertBST(self,root):
        self.sum = 0
        def afterOrder(node):
            if not node:
                return 
            afterOrder(node.right) #递归root的右节点，找到所有比当前节点值大的节点
            self.sum += node.val
            node.val = self.sum
            afterOrder(node.left)
            #使用全局变量保存前一个节点的值，因此不需要返回值
            
        afterOrder(root)
        return root

    #修改 定义pre
    self.pre = 0
    def afterOrder(node):
        if not node:
            return 
        afterOrder(node.right) #递归root的右节点，找到所有比当前节点值大的节点
        node.val += self.pre
        self.pre = node.val
        afterOrder(node.left)
         
#非递归版
class Solution(object):
    def convertBST(self, root):
        s = 0
        stack = []
        cur = root

        #右子节点不断压入栈
        while cur:
            stack.append(cur)
            cur = cur.right

        while stack:
            cur = stack[-1]   #栈顶出栈
            stack.pop()
            s += cur.val      #做事情
            cur.val = s       #做事情
            cur = cur.left    #找左子节点
            while cur:
                stack.append(cur)  #左子节点压入栈
                cur = cur.right    #让当前左子节点的右子节点不断压栈

        return root
        
'''
递归三部曲
1.确定每次进入递归函数做什么
递归root的右节点，找到所有比当前节点值大的节点；
当递归到最右时，我们终止递归，开始累加这条路径上的所有节点值，即，当前节点值累加全局变量的值并更新全局变量的值为累加后的值
递归左节点；
终止当前递归
2，确定递归函数的参数及返回值
要递归遍历，参数中少不了下一个遍历的节点
因为我们使用全局变量保存前一个节点的值，因此不需要返回值
3.确定递归函数终止条件
越过叶子节点时，终止递归
修改当前节点的值且更新全局变量的值后终止递归
代码
