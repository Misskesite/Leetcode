# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:29:46 2020

@author: liuga
"""
#先求和再构建列表, 前提是python中没有最大的整数，所以无论怎么着不会越界?
class Solution(object):
    def addtwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num1 += str(l2.val)
            l2 = l2.next
        add = str(int(num1)+ int(num2))
        
        head = listNode(add[0])
        ans = head
        #ans保存头节点，尾部逐渐添加节点
        for i in range(1,len(add)):
            node = listNode(add[i])
            head.next = node
            head = head.next
        return ans
    
#类似2，这里最高位在最左边，和2相反    这里链表翻转就跟2一样，但是最低位在链表末尾，没法取到链表前面的值，所以用栈保存
#栈 时间复杂度O(max(m,n)) 空间复杂度O(m+n)
class Solution2(object):
    def addtwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
          
            
            #头插法插入节点, 将新节点的下一节点设置成头结点,即在头结点前插入新节点，然后新节点变成头结点               
            curnode = ListNode(carry % 10) 
            curnode.next = head
            head = curnode

            carry = carry // 10
            
        return head
