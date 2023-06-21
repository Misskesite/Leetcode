# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:46:35 2020

@author: liuga
"""
class Node(object):
    def _init_(self, val, prev, next,child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
#思路：每次遇到child节点，就把这个节点作为当前node的next节点；并且要遍历child节点后面的所有节点，
#找到child链表最后面的节点，作为要插入的一整段链表最后的节点，即原node.next节点prev节点。新定义一个函数，这个函数对每个child链表进行遍历，把整段的child链表插入到原链表中
#DFS负责查找，新定义的函数负责插入
class Solution(object):
    def flatten(self, head):
        if not head:
            return
        node = head
        while node:
            node_next = node.next #提前保存
            if node.child:
                f = self.flatten(node.child)
                node.child = None
                nextNode = self.appendTolist(node, f)
                node = nextNode
            else:
                node = node.next #没有孩子节点，继续遍历
        return head
    
    def appendTolist(self, node, listAppend):
        next_node = node.next
        node.next = listAppend
        listAppend.prev = node
        while node.next:
            node = node.next
        node.next = next_node
        if next_node:
            next_node.prev = node
        return next_node

    #改写 此解法为主
    def flatten(self, head):
        if not head:
            return
        
        node = head
        while node:
            if node.next == None:
                tail = node
            
            if node.child:
                node_next = node.next #提前保存
                f = self.flatten(node.child)
                node.next = f
                f.prev = node
                node.child = None

                if tail != None and node_next != None:
                    tail.next = node_next
                    node_next.prev = tail
                    tail = None
                
               
            else:
                node = node.next #没有孩子节点，继续遍历
        return head

class Solution:
  def flatten(self, head: 'Node') -> 'Node':
      def flatten(head: 'Node', rest: 'Node') -> 'Node':
          if not head:
              return rest

          head.next = flatten(head.child, flatten(head.next, rest))
          if head.next:
              head.next.prev = head
          head.child = None
          return head

    return flatten(head, None)

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            if curr.child:
                nex = curr.next
                child = curr.child

                # 遇到一个child，先在 curr 这里豁开一个口子，把child变成 next 的关系
                curr.next = child
                curr.child = None
                child.prev = curr

                # 找到当前这个child链的最末尾
                while child.next:
                    child = child.next
                # 把child的最末尾的节点，跟上面豁开的口子 nex 接上
                if nex:
                    nex.prev = child
                child.next = nex
            curr = curr.next
        return head

    
#迭代方法 + 栈    
class Solution2:
    def flatten(self, head):
        if not head:
            return head
        stack = []
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            #先push next, 然后push child
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                
            if stack:
                curr.next = stack[-1]
                stack[-1].prev = curr
                curr.child = None
        return head
    
#递归方法
class Solution3:
    def flatten(self, head):
        if not head:
            return
        stack = []
        self.helper(head, stack)
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
            stack[i + 1].prev = stack[i]
            stack[i].child = None
            stack[i + 1].child = None          
        return head
    
    def helper(self, node, stack):
        if node == None:
            return
        stack.append(node)
        self.helper(node.child, stack)
        self.helper(node.next, stack)


#递归  [1,2,3,7,8,11,12,9,10,4,5,6]
class Solution(object):
    def flatten(head):
        if not head:
            return head
        
        cur = head
        while cur:
            if cur.child:
                temp = cur.next # 保存4
                child = flatten(cur.child)                
                childEnd = getEnd(child) #获取10

                childEnd.next = cur.next #尾巴10->4
                
                child.prev = cur         #child 对应7->3
                
                if cur.next:
                    cur.next.prev = childEnd #4之前接尾巴10 10<-4

                cur.next = child         # 3 -> 7
                cur.child = None
                
                cur = temp
            else: #没有向下的子分支
                cur = cur.next
        return head

    def getEnd(child):
        while child.next:
            child = child.next
        return child
                
#上面的简洁写法
    def flatten2(head):
        if not head:
            return head
        
        cur = head
        while cur:
            if cur.next == None:
                tail = cur
                
            if cur.child:
                temp = cur.next         # 保存4
                child = flatten(cur.child)
                
                cur.next = child         # 3 -> 7
                child.prev = cur         #child 对应7
                cur.child = None

                if tail != None and temp != None:
                    tail.next = temp      #尾巴10 接 4
                    temp.prev = tail
                    tail = None
                
             else: #没有向下的子分支
                 cur = cur.next
        return head
    
        
#双向链表+dfs
class Solution(object):
    def flatten(head):
        if not head:
            return
        dfs(head)
        return head

    def dfs(head):
        next = head.next
        if head.child:
            head.next = head.child
            head.child = None
            head.next.prev = head
            head = head.next
            head = dfs(head)

        if next:
            next.prev = head
            head.next = next
            head = head.next
            head = dfs(head)
        return head

#preorder traveral child next 类似于左右节点？ output里面保存的是node
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        def recursion(cur):
            if not cur:
                return
            output.append(cur)
            if cur.child:
                recursion(cur.child)
            if cur.next:
                recursion(cur.next)
        output = []
        recursion(head)
        head = output[0]
        temp = head
        for index in range(1, len(output)):
            temp.child = None
            temp.next = output[index]
            output[index].prev = temp
            temp = temp.next
        return head
