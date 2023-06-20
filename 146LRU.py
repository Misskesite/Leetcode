# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 23:12:53 2019

@author: liuga
"""
#least recently used, 缓存淘汰策略，利用哈希 DOUBLE 链表 key:listValue 因为需要 reorder list
#去点 + 加尾 = 移尾  删除 = 去头
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = dict()
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

#get和put操作都需要把双向链表中的某个节点移到末尾
    def move_node_to_tail(self, node):
        #prev <-> node <-> next         pre <-> next   ...   node
        #self.removeNode(node) 对应下面两行
        node.prev.next = node.next
        node.next.prev = node.prev

        #将node插入到尾节点前
        #prev <-> tail  ...  node       prev <-> node <-> tail
        #self.addToTail(node) 对应四行
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

  

    def get(self, key):
        #如果已经到链表中就把它移到末尾
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.move_node_to_tail(node)
        return node.value


    def put(self, key, value):
        #如果已经在哈希表中，更新对应的value
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.move_node_to_tail(node)

        else:
            if len(self.hashmap) == self.capacity:
                #去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                #去掉最久没有被访问的节点，即头节点之后的节点 self.removeNode(head.next)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            #如果不在的话就插入到尾节点前 add to tail
            new = ListNode(key, value)
            self.hashmap[key] = new

            #self.addToTail(new)
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new

#方法2 哈希 key:-> pointer (指向DOUBLE 链表）
#dic + double linkedList
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict() #map key to node
        self.cap = capacity
        
        #head = LRU  tail = most recent, head, tail are dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0 ,0) #default value
        
        self.head.next = self.tail #head tail connected to each other
        self.tail.prev = self.head

     #remove node from list
    def remove(self, node): #mid node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    #insert node between prev and tail 加到tail节点之前
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.insert(n) #insert before tail
            return n.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])   #key存在，删除节点

        n = Node(key, value)
        self.cache[key] = n #更新节点val，插入到链表
        self.insert(n)

        if len(self.cache) > self.cap:
            #remove from the list and delete the LRU from cache
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    
      
