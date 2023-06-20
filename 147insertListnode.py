# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:01:08 2019

@author: liuga
"""
class ListNode(object):
     def _init_(self,x):
         self.val = x
         self.next = None
                  
#插入排序,从左往右比较，找出节点，临时保存，删除，给它找位置，插入它
#插入前要先改tmp.next,再接到pre后面，不能相反，否则会丢失pre.next
class Solution(object):
    def insertSortlist(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        tmp = ListNode(0)


        while cur and cur.next:
             if cur.val <= cur.next.val:
                  cur = cur.next

             else:
                 tmp = cur.next
                 cur.next = cur.next.next

                 while pre.next.val <= tmp.val:
                     pre = pre.next 
                 #prev.next.val > temp.val ，temp 插入到 prev 和 prev.next 之间
                 tmp.next = pre.next
                 pre.next = tmp
          
       return dummy.next

#输人: -1->5->3->4->0 输出: -1->0->3->4->5 
class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:
      dummy = ListNode(0)
      curr = head

      while curr:
           prev = dummy
           while prev.next and prev.next.val < curr.val:
                prev = prev.next
           nxt = curr.next
           curr.next = prev.next
           prev.next = curr
           curr = nxt

     return dummy.next


     def insertionSortList(self, head):

        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                    
                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
            
        return dummyHead.next

        
#时间复杂度O(n**2) 输人: -1->5->3->4->0 输出: -1->0->3->4->5       
class Solution2(object):
    def insertSortlist(self, head):
        dummy = ListNode(0)
        dummy.next = head

        cur = head.next        #待插入的节点
        last = head            #已排序部分最后一个节点

        while cur:
             if last.val <= cur.val:
                  last = last.next

             else:
                  prev = dummy  #prev从dummy开始 一直变化，不停的和cur比较
                  while prev.next.val <= cur.val:
                       prev = prev.next
                       
                  #3步交换 5 和 3
                  last.next = cur.next  #5->4
                  cur.next = prev.next  #3->5
                  prev.next = cur       #-1->3
            cur = last.next  #cur跳到4

        return dummy.next

                  
        
        while head.next: #下一个循环从4开始
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                q = dummy
                head.next = head.next.next  #5 -> 4 
                
                while q.next and q.next.val < temp.val:
                    q = q.next              #q到了-1 ?
                    
                temp.next = q.next          #3->5
                q.next = temp               #-1 ->3
        return dummy.next
