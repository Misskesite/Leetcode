# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:31:15 2020

@author: liuga
"""
#s = "aabbcc", k = 3 output: "abcabc"
#s = "aaabc", k = 3  output: ""
import collections
import heapq

class Solution(object):
    def reArrangeString(self,words,k):
        l = len(words)
        wordscount = collections.Counter(words)
        que = []
        heapq.heapify(que)
        for c, cnt in wordscount.items():
            heapq.heappush(que, (-cnt,c))
        
        res = ""
        while que:
            cnt = min(l,k)
            used = [] #临时数组存放,pop完一组排列好一组，然后再把临时数组里面的push
            for i in range(cnt):
                if not que:  #堆为空，说明此位置不够填字符。剩余的字符(有相同字符？)，不同字符个数不够k，那么说明不能满足题目的要求，返回空字符串
                    return ""
                v, c = heapq.heappop(que)
                res += c
                if -v > 1: # -v - 1 > 0
                    used.append((v+1, c))
                l -= 1
            for use in used:
                heapq.heappush(que, use)
        return res
                    
            
