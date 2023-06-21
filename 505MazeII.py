# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:10:00 2020

@author: liuga
"""

class Solution(object):
    def isValid(maze,x,y):
        if x>=0 and x< len(maze) and y >=9 and y< len(maze[0]) and maze[x][y]==0:
            return True
        return False
    
    def computer(self,x1,y1,x2,y2):
        return abs(x1-x2)+ abs(y1-y2)
            
    def dfs(maze, distance,i,j):
        row = len(maze)
        col = len(maze[0])
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        for it in dir:
            x = i
            y = j
            while (isValid(maze, x+it[0], y+it[1])):
                x+=it[0]
                y+=it[1]
            if distance[x][y] > distance[i][j]+ computer(x,y,i,j):
                distance[x][y] = distance[i][j]+ computer(x,y,i,j)
                dfs(maze,distance,x,y)
                        
        
        
    def maze2(self, maze,start, end):
        if (not maze or not maze[0] or not start or not end):
            return 
        row = len(maze)
        col = len(maze[0])
        distance = [10000*row[10000*col]]
        distance[start[0]][start[1]] = 0
        dfs(maze,distance, start[0],start[1])
        
        return distance[end[0]][end[1]]==10000 ? -1 : distance[end[0]][end[1]]

        
        