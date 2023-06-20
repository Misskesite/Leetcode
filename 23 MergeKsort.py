# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:03:01 2019

@author: liuga
"""

import heapq
 
class listNode(object):
    def _init_(self,x):
        self.val =x
        self.next = None
        
#堆排序的优化，存指针，空间优化 O(k)(K个链表) 时间O(k*n*log(k)) 空间O(k*n)
class Solution(object):
    def mergeKlist(self, lists):
        heap = []
        for node in lists:
            if node: #放链表的第一个节点
                #heapq.heappush(heap,(node.val, node))
                heapq.heappush(heap, node)
                
        tmp = listNode[-1]
        dummy = tmp

        #不断从堆中取出节点，如果这个节点还有下一个节点，就将下个节点也放入堆中
        while heap:
            #smallestNode = heapq.heappop(heap)[1]
            smallestNode = heapq.heappop(heap)
            tmp.next = smallestNode
            tmp = tmp.next
            
            if smallestNode.next:
                #heapq.heappush(heap,(smallestNode.next.val, smallestNode.next))
                heapq.heappush(heap, smallestNode.next)
                
        return dummy.next


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
                
        return dummy.next


            
