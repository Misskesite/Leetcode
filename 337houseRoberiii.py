# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:33:02 2020

1 当前节点选择不偷: 左孩子能偷到的钱 + 右孩子能偷到的钱
2 当前节点选择偷： 左孩子选择自己不偷得到的钱 + 右孩子选择不偷得到的钱 + 当前节点的钱

res[0] = max(left[0], left[1]) + max(right[0], right[1])
res[1] = left[0] + right[0] + root.val 
# 0 代表不偷，1 代表偷
@author: liuga
"""
#树上进行状态转移， 递归的过程中，系统栈会保存每一层递归的参数，后序遍历
class Solution(object):
    def houseRobery(self, root):
        
        def dfs(root):
            if not root:
                return [0,0]
            robleft = dfs(root.left)
            robright = dfs(root.right)
            noroot = robleft[1] + robright[1]
            withroot = root.val + robleft[0] + robright[0]
            robcur = max(withroot, noroot) #当前节点获得最大值？
            return [noroot, robcur]
        return dfs(root)[1]
    #重写
    def houseRobery(self, root):
        res = []
        
        def dfs(root):
            if not root:
                return [0,0]
            robleft = dfs(root.left)
            robright = dfs(root.right)
            robl = max(robleft[0], robleft[1]) + max(robright[0], robright[1])
            rob2 = root.val + robleft[0] + robright[0]
            
            return [rob1, rob2]

        res = dfs(root)
        return max(res[0], res[1])




class Solution:
  def rob(self, root: Optional[TreeNode]) -> int:
    def robOrNot(root: Optional[TreeNode]) -> tuple:
      if not root:
        return (0, 0)

      robLeft, notRobLeft = robOrNot(root.left)
      robRight, notRobRight = robOrNot(root.right)

      rob1 = root.val + notRobLeft + notRobRight
      rob2 = max(robLeft, notRobLeft) + max(robRight, notRobRight)

      return (rob1,rob2)

    return max(robOrNot(root))
'''
递归三部曲：
1：确认递归函数的参数和返回值 (这里返回值是长度为2的数组) 在递归的过程中，系统栈会保存每一层递归的参数
2：确定终止条件（这里是dp的初始化）
3：确认遍历的顺序 (这里明确使用后序遍历，先递归左节点，然后右节点，通过递归的返回值做下一步遍历)
4：确认单层递归的逻辑。
vector<int> left = robTree(cur->left); // 左
vector<int> right = robTree(cur->right); // 右

// 偷cur
int val1 = cur->val + left[0] + right[0];
// 不偷cur
int val2 = max(left[0], left[1]) + max(right[0], right[1]);
return {val2, val1};
