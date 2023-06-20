# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:18:49 2020

@author: liuga
"""
#把每个节点都当成根节点，验证是否二叉搜索树, 自顶向下 O(n*n)
class Solution(object):
    def largestBST(self, root):        
        if not root:
            return 0
        res = 0
        if isBST(root, float('-inf'), float('inf')):
            return countNode(root)

        return max(largestBST(root.left), largestBST(root.right))
    
    def isBST(self, root, mn, mx):
        if not root:
            return True
        if root.val <= mn or root.val >= mx:
            return False
        
        return self.isBST(root.left, mn, root.val) and self.isBST(root.right, root.val, mx)
      
      
    def countNode(self, root):
        if not root:
            return 0
        return 1 + countNode(root.left) + countNode(root.right)

            
        


#时间复杂度O(n)  只遍历一遍二叉树，边验证 BST 的过程中边统计个数
#先递归到最左子节点，然后逐层向上递归，对每个节点都记录当前最大BST节点数. 左子树最大值保存在left[1] 右子树最小值保存在right[0]
class Solution3(object):
    def largestBSTtree(self, root):
        res = 0
        res = helper(root)
        
        def helper(root):
            #对于空节点，是可以任意节点的子节点的  所以 让左边最大，右边界最小,可以满足下面对BST的判断  l_max(float('-inf')) < root.val < r_min(float('inf'))
            if not root:
                return float('inf'), float('-inf'), 0 
            
            l_min, l_max, lv = helper(root.left)
            r_min, r_max, rv = helper(root.right)
            
            if l_max < root.val < r_min:
                return min(root.val, l_min), max(root.val, r_max), lv + rv + 1
            else:
                #跟空节点截然相反，如果一个根不可以是BST，那么返回这个根 左边是最小，右边最大，这样  回溯都上面任何一个包含此节点 根 都不可能为 BST
                return float('-inf'), float('inf'), max(lv, rv)
                #保证叶子节点通过(叶子节点是BST)? 空的左子树的最大值设置为整型最小值，这样一定能通过，同理，将空的右子树的最小值设置为整型最大值
        return res[2]

#上面的扩展写法
    def largestBSTtree(self, root):
        self.res = 0
        mn =  float('-inf')
        mx = float('inf')
        

        def isBST(self, root, mn, mx, res):
            if not root:
                return
            left_cnt, right_cnt = 0, 0
            left_mn, right_mn, left_mx, right_mx = float('-inf'), float('-inf'), float('inf'), float('inf')
            self.isBST(root.left, left_mn, left_mx, left_cnt)
            self.isBST(root.right, right_mn, right_mx, right_cnt)

            if (not root.left or root.val > left_mx) and (not root.right or root.val < right_mn): #可能一边为空，或者两边为空
                self.res = left_cnt + right_cnt + 1
                mn = root.left?  left_mn : root.val
                mx = root.right? right_mx : root.val
            else:
                self.res = max(left_cnt, right_cnt) #不是BST
            
        isBST(root, mn, mx, res)       
        return self.res


A Tree is BST if the following is true for every node x. 

1. The largest value in the left subtree (of x) is smaller than the value of x.
2. The smallest value in the right subtree (of x) is greater than the value of x.

So, we will just check if the largest value of the left subtree is less than the value of the root node and the smallest value of right subtree is greater than the value of root node.

#此方法为主
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.largest = 1

        def dfs(root):
        
            if root == None:
                return (False, 0, float("-inf"), float("inf"))

            if root.left == None and root.right == None : #leaf is BST
                return (True,1 ,root.val, root.val)
            
            l_bst, l_size, l_min, l_max = dfs(root.left)
            r_bst, r_size, r_min, r_max = dfs(root.right)
    
            if l_bst and r_bst and l_max < root.val < r_min:
                cur_size = l_size + r_size + 1
                self.largest = max(self.largest, cur_size)
                return (True, cur_size, l_min, r_max)
            elif l_bst and not root.right and l_max < root.val:
                cur_size = l_size + 1
                self.largest = max(self.largest, cur_size)
                return (True, cur_size, l_min, root.val)
            elif r_bst and not root.left and root.val < r_min:
                cur_size = r_size + 1
                self.largest = max(self.largest, cur_size)
                return (True, cur_size, root.val, r_max)
            else:
                return (False, 0, float("-inf"), float("inf")) # cannot form a BST

        dfs(root)
        return self.largest
