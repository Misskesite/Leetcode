# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:30:41 2020

@author: liuga
"""
import heapq

class Solution(object):
    def findkPairs(self, nums1, nums2,k):
        
        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0 or len2 == 0:
            return []
        heap = []
        for x in range(len1):
            heapq.heappush(heap,(nums1[x]+ nums2[0]), x, 0)
        while pq and len(res) < min(k, len1*len2):
            s,i,j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j +1 < len2:
                heapq.heappush(heap,(nums1[i]+ nums2[j+1]),i,j+1)
        return res


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
       
        pq = []
        for i in range(min(k, m)):
            heapq.heappush(pq, (nums1[i]+nums2[0], i, 0))

        ans = [] 
        while pq and len(ans) < k: # min(k, m*n)
            s, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


'''
1 先把所有的 nums1 的索引入队，即入队的元素有 [0, 0]、[1, 0]、[2, 0]、[3, 0]、......
2 首次弹出的肯定是 [0, 0]，再把 [0, 1] 入队；
3 这样就可以通过优先级队列比较 [0, 1] 和 [1, 0] 的结果，再弹出较小者；
4 依次进行，进行 k 轮。
'''
#小优化是：我们始终确保 nums1为两数组中长度较少的那个？
#if n > m:
        #   n, m, nums1, nums2 = m, n, nums2, nums1



 def kSmallestPairs(self, nums1, nums2, k):
        res = []
        if not nums1 or not nums2 or not k:
            return res
        
        heap = []
        visited = set()
        
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        
        visited.add((0, 0))
        
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
        return res


