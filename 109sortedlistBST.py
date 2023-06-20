# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:12:48 2019

@author: liuga
"""
class TreeNode(object):
    def _init_(self,x):
        self.val=x
        self.left = None
        self.right = None

class Solution(object):
    def sortedlistBST(self, head):
        if not head:
            return None
        
        nums = []   #链表值加入数组
        
        node = head
        while node:
            nums.append(node.val)
            node = node.next
            
        return self.sortedArrayToBst(nums)
        
    def sortedArrayToBst(self,nums):
        if not nums:
            return None
            
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
            
        mid = (len(nums)) //2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBst(nums[:mid])
        root.right = self.sortedArrayToBst(nums[mid+1:])
        return root

#此法为主
class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    A = []

    # Construct the array
    curr = head
    while curr:
      A.append(curr.val)
      curr = curr.next

    def helper(l: int, r: int) -> Optional[TreeNode]:
      if l > r:
        return None

      m = (l + r) // 2
      '''
            if (l + r)%2 == 0:
               m = (l + r) // 2  
           else:
               m = (l + r) // 2  + 1

        '''
      root = TreeNode(A[m])
      root.left = helper(l, m - 1)
      root.right = helper(m + 1, r)
      return root

    return helper(0, len(A) - 1)


#Recursion, fast/slow pointer
class Solution2(object):
    def sortedListToBST(self, head):
        def getMedian(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
            
        def buildTree(left, right):
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)
    
            
class Solution:
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    def findMid(head: ListNode) -> ListNode:
      prev = None
      slow = head
      fast = head

      while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
      prev.next = None

      return slow

    if not head:
      return None
    if not head.next:
      return TreeNode(head.val)

    mid = findMid(head)
    root = TreeNode(mid.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(mid.next)

    return root            
            
            
    
