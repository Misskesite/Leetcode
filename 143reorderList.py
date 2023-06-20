# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:36:50 2019

@author: liuga
"""
#时间复杂度O(n) 空间复杂度O(1)
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return
        
            #split
            fast, slow = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            head1 = head
            head2 = slow.next
            slow.next = None #断开
            
            #reverse list2. tmp先保存下一个指针
            cur, pre = head2, None
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                 
            #merge
            cur1, cur2 = head1, pre #对应head2 
            while cur2: # 也可以while cur1 & cur2: 因为cur2对应的比较短
                nex1, nex2 = cur1.next, cur2.next
                cur1.next = cur2
                cur2.next = nex1
                cur1, cur2 = nex1, nex2
                  
#方法2，时间空间复杂度O(n). 线性表存储链表，利用线性表可以访问下标，重建链表
class Solution2(object):
    def reorderList(self, head):
        if not head:
            return
        res = list()
        node = head

        while node:
            res.append(node) #node.val?
            node = node.next

        i = 0
        j = len(res)

        while i < j:
            res[i].next = res[j]
            i += 1
            if i == j:
                break
            res[j].next = res[i]
            j -= 1
        res[i].next = None
        
