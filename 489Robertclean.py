# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:58:21 2020

@author: liuga
"""
#位置确认麻烦，任意放一个初始位置，定为(0,0) 往左坐标-1, 往右坐标+1 转移方向，先要改变朝向
#走到死胡同，需要转向(180)，原路返回，类似于回溯

#Time: O(n - |obstacles|), where n = ∣cells∣
#Space: O(n - |obstacles|)
class Solution(object):
    def cleanroom(self,robot):
        directions = [(-1,0),(0,1),(1,0),(0,-1)] # go up,go right,, go left, go down
        visit = set()
        
        #机器人转的方向固定，要么顺时针，要么逆时针
        def goback(): # flip direction
            
            robot.turnRight()
            robot.turnRight()
            robot.move() #move 函数来确定新位置是否可以到达
            
            robot.turnRight()#这两步，回到原来的方向
            robot.turnRight()
            
        def backtrack(x,y, direction):
             
            visit.add((x,y))
            
            robot.clean()
            for i in range(4):
                new_direction = (direction + i) % 4
                new_x = x  + directions[new_direction][0]
                new_y = y  + directions[new_direction][1]
                if (new_x, new_y) not in visit and robot.move():
                    backtrack(new_x, new_y,new_direction) 
                    goback()  #要回到调用之前的状态
                robot.turnRight() #有障碍物，转个方向
                
        backtrack(0, 0, 0)
        
        
'''
后退的方法就是，旋转 180 度，前进一步，再转回到原来的方向
0 -> go up
1 go right
2 go down
3 go right
'''


class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        visited = set()
        self.backtracking(robot, (0, 0), 0, visited)
        
    def backtracking(self, robot, cell, direction, visited):
        if cell in visited:
            return
        
        visited.add(cell)
        robot.clean()
        
        for i in range(4):

            if robot.move():  
                new_direction = (direction + i) % 4 #保证余值都在0-3以内，四个方向
                new_cell = (cell[0] + self.directions[new_direction][0], 
                            cell[1] + self.directions[new_direction][1])
                                        

                self.backtracking(robot, new_cell, new_direction, visited)
                self.go_back(robot)
                
            robot.turnRight() #每次都要右转一下 move 函数只能探测前方是否能到达，所以我们必须让机器人转到正确的方向，才能正确的调用 move 函数。
            
    def go_back(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
	robot.turnLeft()
