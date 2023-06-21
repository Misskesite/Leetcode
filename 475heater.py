# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:19:05 2020

@author: liuga
"""
#house[1 2 3 4] heat[1, 4]输出1 
class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        ans = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos +=1
            r = min(house-heaters[pos-1], heaters[pos]-house)
            ans = max(ans, r)
        return ans
    
    #改写 双指针, 稍微快一些 houses[1,2,3], heaters[2] 输出1
    def findRadius(self, houses, heaters):
        ans = 0
        d = float("inf")
        houses.sort()
        heaters.sort()
        j = 0
        for i in range(len(houses)):
            while j < len(heaters) and heaters[j] < houses[i]:
                j += 1

            if j == 0:
                d = heaters[0] - houses[i]
            elif j == len(heaters):
                d = houses[i] - heaters[j-1]
            else:
                d = min(heaters[j] - houses[i], houses[i] - heaters[j-1])
            ans = max(ans, d)
        return ans
        
    
#每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for house in houses:
            j = bisect_right(heaters, house)
            i = j - 1
            rightDistance = heaters[j] - house if j < len(heaters) else float('inf') #没找到
            leftDistance = house - heaters[i] if i >= 0 else float('inf')
            curDistance = min(leftDistance, rightDistance)
            ans = max(ans, curDistance)
        return ans


#house[1 2 3 4] heat[1, 4]输出1     
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r
