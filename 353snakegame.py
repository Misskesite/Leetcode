# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:54:52 2020

@author: liuga
"""

class Solution(object):
    def _init_(self, width, height,food):
         self.width = width
         self.height = height
         self.food = food
         self.snake = [[0,0]]
         self.score = 0
         
    def move(self, direction):
        
        x, y = self.snake(-1)
        if direction == 'U':
            x -= 1
        elif direction == "L":
            y -= 1
        elif direction == "R":
            y += 1
        elif direction == "D":
            x += 1
        return self.count(x,y)
    
    def count(self, x, y):
        if x < 0 or x >= self.height or y < 0 or y >= self.width or [x, y] in self.snake[1:]:
            return -1
        if self.food and x == self.food[0][0] and y == self.food[0][1]:
            self.food.pop(0) 
            self.score += 1   #eat food, length increases by 1
        else:
            self.snake.pop(0) # length remain the same
        self.snake.append([x, y])
        return self.score


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([[0,0]])    # snake head is at the front
        self.width = width
        self.height = height
        self.food = deque(food)
        self.direct = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
    

    def move(self, direction: str) -> int:
        newHead = [self.snake[0][0] + self.direct[direction][0], self.snake[0][1] + self.direct[direction][1]]
    
        # notice that the newHead can be equal to self.snake[-1]
        if (newHead[0] < 0 or newHead[0] >= self.height) or (newHead[1] < 0 or newHead[1] >= self.width): 
            return -1

        if self.food and self.food[0] == newHead:  # eat food, because food not appear on a block occupied by the snake. so after eat fod, it will not bump its body
            self.snake.appendleft(newHead)   # just make the food be part of snake
            self.food.popleft()   # delete the food that's already eaten
        else:   # not eating food: append head and delete tail                 
              
            self.snake.pop()   
            if newHead in self.snake:  #检测蛇头和蛇身是否碰撞? its head occupies a space that its body occupies 
                return -1
            else:
                self.snake.appendleft(newHead) 
            
        return len(self.snake)-1
