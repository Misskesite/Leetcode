# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:38:08 2019

@author: liuga
"""
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head and not head.next and k < 2:
            return head

        dummy = Node(0)
        dummy.next = head

        pre = dummy
        tail = dummy

        while True:
            cnt = k
            while cnt > 0 and tail != None:
                cnt -= 1
                tail = tail.next
                
            #到达尾部，长度不足k, 跳出循环
            if tail == None:
                break

            #用于下次循环
            head = pre.next

            #开始翻转, 尾插法是以此把cur移到tail后面
            while pre.next != tail:
                #获取下一个元素
                cur = pre.next
                #pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                #和剩余的链表链接起来
                cur.next = tail.next
                tail.next = cur  #插在tail后面

            #重置指针
            pre = head
            tail = head

        return dummy.next
                

#头插法
class Solution:
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
      return head

    def getLength(head: ListNode) -> int:
      length = 0
      while head:
        length += 1
        head = head.next
      return length

    length = getLength(head)
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    for _ in range(length // k): #把nxt指向的元素依次移到逆向列表的最前面
      for _ in range(k - 1):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
      prev = curr
      curr = curr.next

    return dummy.next
# Time: O(N)
# Space: O(1)
            

#recursion
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head

        for _ in range(k):
            if not tail:  # Less than k nodes, do nothing
                return head
            tail = tail.next

        newHead = self._reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return newHead

  # Reverses [head, tail)
    def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != tail:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev                    
