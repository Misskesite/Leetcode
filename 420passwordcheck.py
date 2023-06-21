# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:59:25 2020

@author: -
"""
'''
6个以内，需要补字母才能满6个(一种: 缺的字母超过缺的种类，比如123缺3个字母 二种：缺的种类超过字母，aaaaa缺一个字母，种类缺数字和大写 三种：上两种合起来
6到12个，一种连续满3个需要换一个aaa，第三个字母必须换，替换的数量ans 二种：更换次数少，种类不够aabaabaabaab，随便换两个，变成1Abaabaabaab， 三种:两种的混合
20个以上，必然删除多出的n-20
'''
import heapq

class Solution(object):
    def passwdCheck(self,s):
        
        totalcnt = len(s)
        
        lowers = [c for c in s if c.islower()]
        uppers = [c for c in s if c.isupper()]
        digits = [c for c in s if c.isdigit()]
        
        typecnt = bool(lowers) + bool(uppers) + bool(digits)
        
        clist = []
        li = 0
        lc = (s[0] if s else None)
        
        for i, c in enumerate(s):
            if c != lc:
                clist.append(lc,li,i-1)
                li,lc = i,c
        clist.append(lc,li, totalcnt-1)
        
        repeates = [y - x + 1 for c, x, y in clist if y - x > 1]
        
        if totalcnt < 6:
            if max(repeates + [0]) == 5:
                return max(2, 3 - typecnt)
            return max(6 - totalcnt, 3 - typecnt)
        
        deletecnt = max(totalcnt - 20, 0)
        
        heap = [(r%3, r) for r in repeates]
        
        heapq.heapify(heap)
        while heap and totalcnt > 20:
            mod, r = heapq.heappop(heap)
            delta = min(mod+1, totalcnt -20)
            totalcnt -= delta
            heapq.heappush(heap,(2, r-delta))
        
        changecnt = sum(r/3 for mod, r in heap)
        
        return deletecnt + max(changecnt, 3- typecnt)
            
            
