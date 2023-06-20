# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:49:03 2019

@author: liuga
"""
#从下到上转向水平方向，纵坐标最大的点是关键点。 从上到下转向水平方向，纵坐标第二大的点是关键点。
#当遇到左端点，我们可以直接与当前最高建筑高度比较，判断是否是转折点，当遇到右端点，则需判断是否是转折点。难度在于右端点
import heapq

class Solution:    
    def getSkyline(self, buildings):
        borders = sorted([i[0] for i in buildings] + [i[1] for i in buildings])
        index = 0
        heap = []
        res = [[0, 0]]
        for border in borders:
            while index < len(buildings) and buildings[index][0] == border:
                heapq.heappush(heap, [-buildings[index][2], buildings[index][1]])
                index += 1
            while heap and heap[0][1] <= border: # 最高高度的右边界？
                heapq.heappop(heap)
            height = -heap[0][0] if heap else 0 #堆为空，高度为0右边的点？
            if height != res[-1][1]:
                res.append([border, height])
        return res[1:]


#扫描线算法
class Solution(object):
    def getSkyline(self, building):
        pos_height = []
        for l, r, height in buildings:
            pos_height.append((l, -1*height))
            pos_height.append((r, height))
            
        pos_height.sort(key = lambda x:(x[0], x[1]))

        cur_handle = [0]   #cur_handle = SortedList() cur_hanlder.add(0)
        pre_max_height = 0
        cur_max_height = 0

        res = []
        for pos, height in pos_heght:
            if height < 0 :
                cur_handle.append(-1*height)
            else:
                cur_handle.remove(height)
        
            cur_max_height = max(cur_handle)
            #判断高度转折点，从上往下？
            if pre_max_height != cur_max_height:  #cur_handle[-1]
                res.append([pos, cur_max_height])
                pre_max_height = cur_max_height
        return res
    
#python依次遍历所有建筑的进出点，记录每个变化点的最高值，高度为负数是加入建筑，为正数为删除建筑    
class Solution2(object):
    def getSkyline(self, buildings):
        ans = []
        changes = []
        for left, right, height in buildings:
            #加入建筑的左边点
            heapq.heappush(changes, (left, -height))
            #删除建筑的右边点
            heapq.heappush(changes, (right, height))

        lives = SortedDict()
        #高度为地平线的建筑始终至少有一个
        lives[0] = 1
        while changes:
            #当前的点和高度
            x, h = heapq.heappop(changes)
            #加入建筑
            if h < 0:
                if h in lives:
                    lives[h] += 1
                else:
                    lives[h] = 1
                #最高建筑
                if h == lives.keys()[0]:
                    ans.append([x, -h])

            #删除建筑
            else:
                lives[-h] -= 1
                #高度为-h的建筑全部没了
                if not lives[-h]:
                    lives.pop(-h)
                    #判断最高建筑发生了变化
                    new_max = lives.keys()[0]
                    if -new_max < h:
                        ans.append([x, -new_max])

        return ans
            


class Solution3(object):
    def getSkyline2(self, buildings):
        points = [(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings]
        points.sort()
        ans = [[0, 0]]
        heap = [[0, float('inf')]]
        for x, h, r in points:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if h:
                heapq.heappush(heap, [h, r])
            if ans[-1][1] != -heap[0][0]:
                ans.append([x, -heap[0][0]])
        return ans[1:]

