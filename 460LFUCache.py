# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:05:44 2020

@author: liuga
"""
#内存O(1)双指针 时间O（1） hashmap

class LFUCache:
    # 用于记录最后使用时间的链表 
    class Node:
        def __init__(self, key):
            self.prev = None
            self.next = None
            self.key = key

        def add(self, node):
            self.next = node
            node.prev = self

        def delete_self(self):
            if self.next is not None:
                self.next.prev = self.prev
            if self.prev is not None:
                self.prev.next = self.next

    # 用于记录使用次数的链表
    class Layer:
        def __init__(self, depth: int):
            self.prev = None
            self.next = None
            # depth表示使用次数
            self.depth = depth

            # 这个就是二级的hashmap 加上下面的二级链表 做成了LRU的缓存
            self.queue = {}
            # 二级链表头
            self.start = LFUCache.Node(-1)
            # 二级链表尾巴
            self.end = self.start

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 这个就是一级的hashmap 加上下面的链表 做成了LFU的缓存
        self.data = {}
        # 这个map用于指向链表结点，如果重新设计的话，可以和上面的map合并的
        self.kToLayer = {}
        # 链表尾巴
        self.end_layer = None
        # 链表头
        self.top_layer = self.Layer(0)

    def get(self, key: int) -> int:
        r = self.data.get(key, -1)
        if r != -1:
            # 更新记录使用次数的链表
            self.kToLayer[key] = self.update_layer(self.kToLayer[key], key)
        return r

    def put(self, key: int, value: int) -> None:
        # 1. capacity为0的话直接不干了
        if self.capacity == 0:
            return
        # 2. 数据已经存在的话，就更新记录使用次数的链表
        if self.data.get(key) is not None:
            self.data[key] = value
            self.kToLayer[key] = self.update_layer(self.kToLayer[key], key)
            return

        # 3.1 如果超过了限度，就从链表头取出一个，删掉
        if len(self.data) >= self.capacity:
            key_to_del = self.pop_queue_from_layer(self.top_layer)
            self.data.pop(key_to_del)
            now = self.kToLayer[key_to_del]
            if len(now.queue) == 0 and now.depth > 0:
                self.clear_layer(now)
            self.kToLayer.pop(key_to_del)
        # 3.2 把新的加进去
        self.data[key] = value
        self.add_key_to_layer(self.top_layer, key)
        self.kToLayer[key] = self.top_layer


#方法2
import collections
class Node:
    def _init_(self, key = None, value = None, frequency = None):
        self.key = key
        self.value = value
        self.freq = frequency
        self.prev = None
        self.nxt = None

    def _repr_(self):
        return "k: {}, v: {}, f:{}". format(self.key, self.value, self.freq)

    def get_dlinkedlist():
        head = Node()
        tail = Node()
        head.nxt = tail
        tail.prev = head
        return head, tail

class LFUCache:
    def _init_(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.freq_map = defaultfict(get_dlinkedlist)
        self.key_map = {}
        #min_freq用于删除节点的时候
        self.min_freq = 0
        
        
    def _add_node(self, node):
        '''
        频率字典加入新的节点
        '''
        freq = node.freq
        head = self.freq_map[freq][0]
        node.nxt = head.nxt
        node.pre = head
        head.nxt = node
        node.nxt.prev = node

    def _del_(self, freq):
        node = self.freq_map[freq][1].pre
        self._remove(node)
        #del the node in kay_map
        self.key_map.pop(node.key)

    def _remove(self, node):
        #remove the node frrom freq_map[node.freq] if it has no useful node, or keep the DL not break

        pre_node = node.pre
        nxt_node = node.nxt
        freq = node.freq

        if self.freq_map[freq] == (prev_node, nxt_node):
            self.freq_map.pop(freq)
        else:
            pre_node.nxt = nxt_node
            nxt_node.prev = prev_node

    def _update_node(self, node, val):
        #更新node，feq_map受影响
        self._remove(node)
        #如果min_freq与当前node对应的freq_map键值被删除 min_freq需要自增1

        if node.freq == self.min_freq and node.freq nor in self.freq_map:
            self.min_freq += 1
        #更新node的频率和对应的value 加入到freq_map
        node.freq += 1
        node.value = val
        self_add_node(node)


    def get(self, key:int) ->int:
        node = self.key_map.get(key, None)
        if node is None:
            return -1
        else:
            self._update_node(node, node.value)
            return node.value

    def put(self, key: int, vlaue: int)-> None:
        if self.cap <= 0:
            return None
        if key in self.key_map:
            node = self.key_map[key]
            self._update_node(node, value)
        else:
            node = Node(key, value, 1)
            if self.size == self.cap:
                self._del(self.min_freq)
                self.size -= 1
            self.min_freq = 1
            self._add_node(node)
            self.key_map[key] = node
            self.size += 1
        
'''
First, OrderedDict is a dict + double linked list.

A count2node is a dict of OrderedDict, so you can look up like this count2node[count][key] to remove/update the node in O(1), or count2node[count].popitem(last=True) to remove the oldest node in O(1).
'''

from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        
        node.count += 1
        self.count2node[node.count][key] = node
        
        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1
            
            
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key) # NOTICE, put makes count+1 too
            return
        
        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False) 
            del self.key2node[k] 
        
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return
        
