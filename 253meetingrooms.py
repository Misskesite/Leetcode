# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:26:35 2020

@author: liuga
"""
#Time O(n) Space O(1) 堆是一种特殊的优先队列
import heapq
class Solution(object):
    def meetingrooms(self, intervals):
        intervals.sort(key = lambda x:x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]: #释放房间
                heapq.replace(heap, i.end) #heappushpop
            else:
                heapq.heappush(heap, i.end)
        return len(heap)

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      minHeap = []  # store end times of each room

      for start, end in sorted(intervals):
          if minHeap and start >= minHeap[0]:
              heapq.heappop(minHeap) #释放房间？
          heapq.heappush(minHeap, end)

     return len(minHeap)
  
class Solution2(object):
    def minMeetingRooms(self, intervals):
        starts, ends = [],[]
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
            
        starts.sort()
        ends.sort()
 
        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1
 
        return min_rooms



class Solution2(object):
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        tmp = []

        #标记起点终止点
        for inter in intervals:
            tmp.append((inter.start, True))
            tmp.append((inter.end, False))

        tmp = sorted(tmp, key = lambda v: (v[0], v[1]))

        n = 0
        max_num = 0
        for arr in tmp:
            if arr[1]:
                n += 1
            else:
                n -= 1

            max_num = max(n, max_num)
        return max_num
                
        
