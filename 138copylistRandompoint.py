# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:49:11 2019

@author: liuga
"""
class Node(object):
    def _init_(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copylistRandom(self, head):
        if not head:
            return None
        Dict = dict()
        dummy = Node(0, None, None)
        Dict[head] = dummy
        newHead = dummy

        p = head
        while p:
            node = Node(p.val, p.next, None)
            Dict[p] = node
            
            newHead.next = node
            
            newHead = newHead.next

            p = p.next
            
        p = head
        while p:
            if p.random:
                Dict[p].random = Dict[p.random]
            p = p.next
        return dummy.next

#由于每一个节点都有一个随机指针，这个指针可以为空，也可以指向链表的任意一个节点，如果在每生成一个新节点给其随机指针赋值时，都要去遍历原链表的话，OJ 上肯定会超时，
#所以可以考虑用 HashMap 来缩短查找时间，第一遍遍历生成所有新节点时同时建立一个原节点和新节点的 HashMap，第二遍给随机指针赋值时，查找时间是常数级

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        #创建一个哈希表，key是原节点, value是新节点
        d = dict()
        p = head
        #将原节点和新节点放进哈希表
        while p:
            new_node = Node(p.val, None, None)
            d[p] = new_node
            p = p.next
            
        p = head

        #遍历原链表，设置新节点的next和random
        while p:
            if p.next:
                d[p].next = d[p.next]

            if p.random:
                d[p].random = d[p.random]

            p = p.next
            
        #返回头节点, 即原节点对应的value(新节点)
        return d[head]
            
        
class Solution(object):
    def copyRandomList(self, head):
        
        mydic = dict()

        def dfs(node):
            if node is None:
                return None
            if node in mydic:
                return mydic[node]
            root = Node(node.val, None, None)
            mydic[node] = root

            root.next = dfs(node.next)
            root.random = dfs(node.random)
            return root
        
        return dfs(head)
            
