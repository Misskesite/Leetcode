# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:17:41 2020

@author: liuga
"""
#ax + by = z 有解，当且仅当z是x,y 最大公约数的倍数 
class Solution(object):
    def canWearWater(self, x, y, z):
        
        return z ==0 or (x+y >=z and z % self.gcd(x,y) == 0)
    
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x%y) #gcd(a,b) = gcd(b, a mod b)

    def canMearsureWater(self, x, y, z):
        if z == 0:
            return True
        if z > x + y:
            return False
        mi = min(x,y)
        ma = max(x,y)

        flag = [False] *ma  #记录是否出现一个周期(循环)
        remain = 0
        while not flag[remain]:
            flag[remain] = True
            remain = (remain + mi)%ma
            if remain == z or remain + ma == z:
                return True
        return False
            
              
            
        

#栈模拟递归 状态最多有(x+1)(y+1)种，时间复杂度O(xy)
#装满小桶，往大桶倒，直到大桶满，小桶剩下remain,把大桶清空，小桶把remain倒入大桶
class Solution(object):
    def canMersureWater(self, x, y, z):
        stack = [0,0]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True

            if(remain_x, remain_y) in self.seen:
                continue

            self.seen.add((remain_x, remain_y))
            #X灌满
            stack.append((x, remain_y))
            #Y灌满
            stack.append((remain_x, y))
            #X倒空
            stack.append((0, remain_y))
            #Y倒空
            stack.append((remain_x, 0))

            #把x壶灌进y壶，直到灌满或倒空
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y))

            #把Y壶灌进X壶，直到灌满或倒空
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x))
        return False
            
            
'''
z = m * x + n * y
m，n为舀水和倒水的次数，正数表示往里舀水，负数表示往外倒水，那么题目中的例子可以写成: 4 = (-2) * 3 + 2 * 5，即3升的水罐往外倒了两次水，5升水罐往里舀了两次水。那么问题就变成了对于任意给定的x,y,z，存不存在m和n使得上面的等式成立
'''
from collections import deque
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        """
        1)Check edge case if the capacity is less than the target capacity. We will never be able to measure it.
        2) Initalize visited set, and q with zero as the intital capacity is zero
        3) Initialize direction of the queue is +x, -x, +y, -y (x= jug1Capacity, y = jug2Capacity )
        note the direction can only be +x, -x, +y, -y as these are the only operation you can do in the jug either you can remove the water or add the water. and you can only add fix amount of waters which is equivalent to their capacities. 
        4) do Bfs, pop the node, explore the direction
        5) check the boundary condtion which is if the capacity goes to negative or it exceeds the target capacity.
        6) Check visited, if not added check if the value equal to target and also add  it to the queue and visited
        7) return False if unable to reach
        """
        
        #edge case 
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        
        # Initialize directions q and visited
        direction = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity ]
        q = deque([0]) #intital capacity 0
        visited = set()
        visited.add(0)
        
        #bfs
        while q:
            x = q.popleft()
            for value in direction:
                nx =  x + value
                # check boundary conditions
                if nx > 0 and nx <= jug1Capacity + jug2Capacity:
                    #check visited
                    if nx not in visited:
                        if nx == targetCapacity:
                            return True
                        q.append(nx)
                        visited.add(nx)
        
        return False
