# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:46:19 2020

@author: liuga
"""
import heapq

class Solution(object):
    def kthSmallest(self, matrix,k):
        m,n = len(matrix), len(matrix[0])
        q =[(matrix[0][0],0,0)]
        ans = None
        
        for _ in range(k):
            ans,i,j = heapq.heappop(q)
            if j == 0 and i+1 < m:  #the first column
                heapq.heappush(q,(matrix[i+1][j], i+1,j))
            if j+1 < n:              #from the first line, then second line
                heapq.heappush(q,(matrix[i][j+1], i, j+1))
        return ans
    
#参考23            
#归并排序 每一行是有序数组，问题转化为N个有序数组找第K大的数，这里是n个数组归并，需要小根堆维护。
class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        pq = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(pq)

        res = 0
        for i in range(k-1): #弹出k-1次，最后return弹出一次
            num, x, y = heapq.heappop(pq)
            if y != n-1:
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))
        return heapq.heappop(pq)[0] #或者上面改为k， return num


class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      minHeap = []  # (matrix[i][j], i, j)

      i = 0
      while i < k and i < len(matrix):
          heapq.heappush(minHeap, (matrix[i][0], i, 0))
          i += 1

      while k > 1:
          k -= 1
          _, i, j = heapq.heappop(minHeap)
          if j + 1 < len(matrix[0]):
              heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))

      return minHeap[0][0]


import bisect
 
class Solutions(object):
    def kthsmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi: # left < right:
            mid = (hi+lo)>>1
            loc = sum(bisect.bisect_right(m,mid) for m in matrix)
            if loc>=k:
                hi = mid-1  #high = mid
            else:
                lo = mid+1
        return lo
                
                
            
