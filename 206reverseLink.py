# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 22:42:34 2019

@author: liuga
"""
#跟25题类似

#双指针, 迭代完了之后 cur变成null, prev最后一个节点
#时间复杂度O(n), 空间复杂度O(1)
class Solution(object):
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            tmp = cur.next
            cur.next = prev
            pre = cur
            cur = tmp
            
        return prev

#递归
class Solution3(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head

        p = head.next
        ret = self.reverseList(p)

        head.next = None
        p.next = head
        return ret
    
    
class Solution(object):
    def reversehead(self, head):
        p = head
        list = []
        while p:
            list.insert(0, p.val)
            p = p.next
        p = head
        for n in list:
            p.val = n
            p = p.next
        return head

#类似于最上面的写法 这里 dummy.next = prev
class Solution2(object):
    def reverseList(self, head):
        dummy = Node(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next





