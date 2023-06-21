# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:34:36 2020

@author: liuga
"""
#双链表 + map 返回计数最小和最大的字符串
class KeyNode(object):
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class ValueNode(object):
    def _init_(self,value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        self.first = None
        
class AllOne(object):
    def _init_(self):
        self.keyDict = dict()
        self.valueDict = dict()
        self.head = self.tail = None
        
    def inc(self, key):
        if key in self.KeyDict:            
            keyNode = self.KeyDict[key]
            valueNode = self.valueDict[keyNode.value]
            nextValueNode = valueNode.next
            keyNode.value +=1
            if not nextValueNode or nextValueNode.value > keyNode.value:
                nextValueNode = self.insertValueNodeAfter(keyNode.value, valueNode)
                if self.tail == valueNode:
                    self.tail = nextValueNode
            self.unlinkKey(keyNode, valueNode)
            self.linkKey(keyNode, nextValueNode)
        else:
            keyNode = self.keyDict[key] = keyNode(key,1)
            valueNode = self.valueDict.get(1)
            if not valueNode:
                valueNode = self.valueDict[1] = valueNode(1, None, self.head)
                if self.head:
                    self.head.prev = valueNode
                self.head = valueNode
                if self.tail == None:
                    self.tail = valueNode
            self.linkKey(keyNode, valueNode)
            
        
        
        
    
    def insertValueNodeAfter(self, value, node):
         newNode = ValueNode(value, node.prev, node)
         self.valueDict[value] = newNode
         if node.next:
             node.next.prev = newNode
         else:
             self.head = newNode
         node.prev = newNode
         return newNode
     
    def unlinkKey(self,keyNode, valueNode):
        next, prev = keyNode.next, keyNode.prev
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if valueNode.first == KeyNode:
            valueNode.first = next
        if not valueNode.first:
            self.delValueNode(valueNode)
    
    def linkNode(self, keyNode, valueNode):
        firstKeyNode = valueNode.first
        keyNode.prev = firstKeyNode
        if firstKeyNode:
            firstKeyNode.prev = keyNode
        valueNode.first = keyNode
        
            
                
    
                
                
            
            
        
