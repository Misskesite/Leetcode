# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:46:57 2020

@author: liuga
方法1：最小堆保存已有数据中最大的一半数据，最大堆保存已有数据中最小的一半，并且我们只允许最小堆的元素个数比最大堆个数多1或者相等
动态的过程：为了找到添加新数据以后，数据流的中位数，我们让这个新数据在大顶堆和小顶堆中都走了一遍。而为了让大顶堆的元素多1个，我们让从小顶堆中又拿出一个元素“送回”给大顶堆；

方法2：若插入的元素大于等于小根堆堆顶元素（说明他比中位数大哦），则将其插入小根堆，否则将其插入大根堆。这个时候堆已经可能不再平衡了，我们需要重新使得他们平衡。
具体操作如下：当小根堆的大小大于一半时，不断将小根堆堆顶元素取出并插入大根堆，直到小根堆的大小等于总序列长度的一半。反之亦然。这样我们可以始终保证小根堆的元素比大根堆的元素多1或者相等。
中位数要么在小根堆堆顶，要么就是取两个堆的堆顶求平均
"""
from collections import heapq

class Solution(object):
    def medianStream(self, num):
        #initialize 跟下面第二种方法是反的
        
        minheap  = []      # 小顶堆 存较大的一半 the larger half of the list
        maxheap = []       # 大顶堆 可以通过对元素的值 * -1

        #add number
        heapq.heappush(maxheap, -num)
        
        mintop = minheap[0] if len(minheap) else None
        maxtop = maxheap[0] if len(maxheap) else None
        
        if mintop < -maxtop or len(minheap)+1 < len(maxheap):
            heapq.heapqpush(minheap, -heapq.heappop(maxheap))
            
        if len(maxheap) < len(minheap):
            heapq.heappush(maxheap, -heapq.heappop(minheap))

        #find median
        if len(minheap) < len(maxheap): #差值为1
            return -1.0* maxheap[0]
        else:                           #相等
            return (minheap[0] - maxheap[0])/2.0

        
'''            
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of smaller half is kept to be n / 2 at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on n's parity.

This way we only need to peek the two heaps' top number to calculate median.
'''
#We can use two heaps to store the lower half and the higher half of the data stream. The size of the two heaps differs at most 1.
#one senario (heap length not equal): element is added to the minheap(large) first, then the minumu element is poped out and added to the maxheap(small).(this assures all element in minheap are greater than maxheap) Finally, the two heaps needed to be load balanced.
from collections import heapq
class Solution2(object):
    def __init__(self):
        self.large = []  #minheap 存较大一半的小顶堆 the larger half of the list, min heap                      7 8 9 
        self.small = []  #maxheap 存较小一半的大顶堆(负数？) the smaller half of the list, with invert values    6 3 5
        

    
    def addNum(self, num):
        if len(self.large) == len(self.small):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num)) # -num放入small堆中，然后弹出返回(-最小元素) 最大值压入 large
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

#改写一下
'''
    def addNum(self, num):
        if len(self.large) == len(self.small):
            heapq.heappush(self.small, -num)
            heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large, num)
            heapq.heappush(self.small, -heapq.heappop(self.large))
            
'''
    
    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

        

#此法为主
class MedianFinder:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []

  def addNum(self, num: int) -> None:
    if not self.maxHeap or num <= -self.maxHeap[0]:
      heapq.heappush(self.maxHeap, -num)
    else:
      heapq.heappush(self.minHeap, num)

    # Balance two heaps s.t.
    # |maxHeap| >= |minHeap| and |maxHeap| - |minHeap| <= 1
    if len(self.maxHeap) < len(self.minHeap):
      heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    elif len(self.maxHeap) - len(self.minHeap) > 1:
      heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

  def findMedian(self) -> float:
    if len(self.maxHeap) == len(self.minHeap):
      return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
    return -self.maxHeap[0]
