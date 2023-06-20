# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:56:47 2020

@author: liuga
"""
#用一个 Iterator 对象进行初始化，它本身有next和hasNext接口。 peek不移动指针， next移动指针
class Solution(object):
    def _init_(self, iterator):
        self.iterator = iterator
        self.pk = None
    
    def peek(self): #存储上一个peek元素，如果有就在peek时直接返回，不移动指针，next时清空peek元素
        if self.pk == None:
            self.pk = self.iterator.next()
        return self.pk
            
    def Next(self):
        if self.pk != None:
            tmp = self.pk
            self.pk = None
            return tmp
        else:
            return self.iterator.next()
        
    def hasNext(self):
        if self.pk:
            return True
        else:
            return self.iterator.hasNext()

'''
peek 操作的时候，要用到 next 操作取出当前的元素
但是，使用 next 操作会将指针往后移动一位，又不符合要求
这时，使用 cache 缓存上一次 peek 操作的元素，此时的指针已经后移了一位
检查has_next要看pk是否为空
'''

#利用iterator里的v(数组) index
class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator


    def peek(self):
        return self.it.v[self.it.index]

    def next(self):
        return it.next()

    def hasNext(self):
        return self.it.hasNext()
