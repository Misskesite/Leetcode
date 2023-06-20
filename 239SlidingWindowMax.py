0# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 18:06:05 2019

@author: liuga
"""
#时间复杂度O(n) 空间复杂度O(k) 队列不超过k+1
from collections import deque

class Solution(object):
    def slidingWindowMax(self,nums,k):
        ans = []
        dq = deque() #只存num？
        
        for i, num in enumerate(nums):
             while dq and dq[-1] <= num:
                 dq.pop() #右边弹出，保证单调递减                   
                 
             dq.append(num)
             if nums[i-k] == dq[0] and i >= k: #out of bound
                 dq.popleft()

             if i >= k-1:
                 ans.append(dq[0])
        return ans
#此法为主
    def slidingWindowMax(self,nums,k):
        n = len(nums)
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i- k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans
    
            
#大小为k的单调递减双向队列   O(n)时间复杂度          
class Solution2:
    def maxSlidingWindow(self, nums, k):
      
        ans = []
        dq = deque() # [[i, num]] 也可以只存i
        for i, num in enumerate(nums):
            if dq and i - dq[0][0] >= k:
                dq.popleft()
            while dq and deque[-1][1] <= num: #如果从最右边加入了一个较大的数字，退出比较小的数字。需要从右开始退队列，退到队列中剩余的数字都比该数字大位置
                dq.pop()
            dq.append([i, num])
            if i >= k-1:
                ans.append(dq[0][1])
        return ans


#堆方法 复杂度更高？
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # python默认是小根堆，故加"-"，形成"大根堆"
        # 由于堆顶元素可能不在滑动窗口内，故要维护一个二元组(num, index)
        # 通过index判断堆顶元素是否在滑动窗口内
        # 首先把 k 个元素加入大根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            # 把最新的元素加入大根堆
            heapq.heappush(q, (-nums[i], i))
            # 判断堆顶元素（下标）是否在滑动窗口内
            while q[0][1] <= i - k:
                heapq.heappop(q)
            # 把大根堆的堆顶元素加入ans
            ans.append(-q[0][0])
        return ans


