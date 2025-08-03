"""renpy
init python:
"""

import random, pygame

class SnakeMinigameCDD(renpy.Displayable):
   def __init__(self, **kwargs):
      super(SnakeMinigameCDD, self).__init__(**kwargs)
      self.reset()
   
   def reset(self):
      global snake_score
      self.snakeBody = [(960,540),(950,540),(940,540)]
      self.blockSize = 10
      self.snakeDirection = (self.blockSize, 0)
      self.snakespeed = 0.05
      self.score = 0
      self.area_size = 800
      self.render_size = (1920, 1080)
      self.foodPositionX = (random.randint(1, 80) * 10)