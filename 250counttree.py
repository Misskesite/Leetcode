# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:07:15 2020

@author: liuga
"""
#递归栈的最大深度n, 时间复杂度O(n)
class Solution(object):
    def countTree(self, root):
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return True
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
'''
        if l and r:
        #    if root.left and root.left.val != root.val:
                return False
             if root.right and root.right.val != root.val:
                 return False

             self.res += 1
             return True
        return False
              

'''
            self.res += 1
            return True
        return False
            

#同值节点2种可能: 叶节点必然是同值子树。左右孩子节点都是一个同值子树的根节点，当前节点的值跟左右孩子节点都相同

#方法2
def countTree(self, root):
        if not root:
            return 0
        self.ans = 0
        self.dfs(root, root.val, ans)
        return self.ans
    
def dfs(root, pre, ans):
    if not root:
        return True
    l = dfs(root.left, root.val, ans)
    r = dfs(root.right, root.val, ans)
    if l and r:
        ans += 1
        return root.val == pre #当前节点和父节点相同，左右节点相同

    return False 

'''
从下往上 check，采用后序遍历的顺序，左右根，这里还是递归调用函数，对于当前遍历到的节点，如果对其左右子节点分别递归调用函数，返回均为 true 的话，那么说明当前节点的值和左右子树的值都相同，那么又多了一棵树，所以结果自增1
'''

class Solution:
  def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    ans = 0

    def isUnival(root: Optional[TreeNode], val: int) -> bool:
      nonlocal ans
      if not root:
        return True

      if isUnival(root.left, root.val) & isUnival(root.right, root.val): #对其左右子节点分别递归调用函数，返回均为 true 的话，那么说明当前节点的值和左右子树的值都相同
        ans += 1
        return root.val == val  #返回当前节点值和给定值(其父节点值)是否相同，从而回归上一层递归调用

      return False

    isUnival(root, math.inf)
    return ans


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        self.count = 0
        def dfs(node, father):
            if not node:
                return True #这里要注意
            l = dfs(node.left, node.val)
            r = dfs(node.right, node.val)
            if l and r:
                self.count += 1
                if node.val == father:
                    return True
            return False
        dfs(root, -1)
        return self.count
