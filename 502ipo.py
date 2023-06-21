# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:39:44 2022

@author: liuga
"""
import heapq
class Solution(object):
    def ipo(self, w, k, profits, capital):
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        n = len(profits)
        i = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key = lambda x: x[0])

        pq = []
        for _ in range(k): #将所有能投资的项目的利润压入堆中，每次取出最大值，然后更新资本
            while cur < n and arr[i][0]<= w:
                heapq.heappush(pq, -arr[i][1]) #最小堆?
                i += 1
            if pq:
                w -= heappop(pq) #更新资本
            else:
                break #为空，说明没有选择够，直接跳出
        return w
                
                
        
#两个堆 堆的核心就是动态求极值。动态和极值二者缺一不可   使用一个最大堆和一个最小堆，把资本利润对放在最小堆中，这样需要资本小的交易就在队首，然后从队首按顺序取出资本小的交易，如果所需资本不大于当前所拥有的资本，那么就把利润资本存入最大堆中    
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        n = len(Profits)
        cap_pro_minHeap = []
        canget_pro_maxHeap = []
        for i in range(n):
            heapq.heappush(cap_pro_minHeap, (Capital[i], Profits[i]) )

        for _ in range( min(n, k) ):
            while cap_pro_minHeap and cap_pro_minHeap[0][0] <= W:   #堆顶的，启动资金 小于等于 W，可以开这个项目
                heapq.heappush(canget_pro_maxHeap, -cap_pro_minHeap[0][1])   #可获得的利润
                heapq.heappop(cap_pro_minHeap)   #弹出避免后面重复加入，上面用cur控制     
            if canget_pro_maxHeap:              #如果还有项目的利润可以赚,弹出k次
                W += -(canget_pro_maxHeap[0])
                heapq.heappop(canget_pro_maxHeap)
            else:                               #没有项目可以开了，没有利润可以赚了
                break
        return W


#The reason for sorting and the nature of the iterator is to establish Capital Boundaries for projects that can be taken on given your current working capital.
#Then after each increment in Pure Profit you "may" be able to jump across boundaries to take on more expensive projects
def findMaximizedCapital(self, k, W, Profits, Capital):
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda c: c[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap:
                W -= heapq.heappop(heap)
        return W
    
