"""renpy
init python:
"""

import random, pygame

class SnakeMinigameCDD(renpy.Displayable):
   def __init__(self, **kwargs):
      super(SnakeMinigameCDD, self).__init__(**kwargs)
      self.reset()

   def render(self, width, height, st, at):
      render = renpy.Render(*self.render_size)
      render_canvas = render.canvas()
      area_rect = pygame.Rect(((render.get_size()[0] - self.area_size) // 2 - 20, (render.get_size()[1] - self.area_size) // 2 - 80), (self.area_size + 40, self.area_size + 100))
      playable_area = pygame.Rect(((render.get_size()[0] - self.area_size) // 2, (render.get_size()[1] - self.area_size) // 2), (self.area_size, self.area_size))
      foodRect = pygame.Rect((self.foodPositionX, self.foodPositionY), (self.blockSize, self.blockSize))
      
      render_canvas.rect((50,50,200,255), area_rect)
      render_canvas.rect((25,25,100,255), playable_area)
      render_canvas.rect((250,0,0), foodRect)

      score_text = Text("Score: {}".format(self.score), size=30)
      score_render = renpy.render(score_text, width, height, st, at)
      render.blit(score_render, self.scoreX, 75)

      for segment in self.snakeBody:
         render_canvas.rect((255,255,0), [segment[0], segment[1], self.blockSize, self.blockSize])
      newHead = tuple(map(lambda i, j: i+j, self.snakeBody[0], self.snakeDirection))
      self.snakeBody.insert(0, newHead)

      headRect = pygame.rect((self.snakeBody[0]), (self.blockSize, self.blockSize))

      if headRect.colliderect(foodRect):
         self.foodPositionX = (random.randint(1, 80) * 10) + (self.render_size[0] - self.area_size) // 2
         self.foodPositionY = (random.randint(1, 80) * 10) + (self.render_size[1] - self.area_size) // 2
         self.speed -= 0.001
         self.score += 10
         if self.speed <= 0.001:
            self.speed = 0.001
      else:
         self.snakeBody.pop()

      if not headRect.colliderect(playable_area):
         self.reset()

      renpy.redraw(self, self.speed)
         return render

   def event(self, ev, x, y, st):
      if ev.type == pygame.KEYDOWN:
         if ev.key == pygame.K_UP:
            if self.snakeDirection != (0,10):
               self.snakeDirection = (0,-10)
         if ev.key == pygame.K_DOWN:
            if self.snakeDirection != (0,-10):
               self.snakeDirection = (0,10)
         if ev.key == pygame.K_LEFT:
            if self.snakeDirection != (10,0):
               self.snakeDirection = (-10,0)
         if ev.key == pygame.K_RIGHT:
            if self.snakeDirection != (-10,0):
               self.snakeDirection = (10,0)
   
   def reset(self):
      global snake_score
      
      self.snakeBody = [(960,540),(950,540),(940,540)]
      self.blockSize = 10
      self.snakeDirection = (self.blockSize, 0)
      self.snakespeed = 0.05
      self.score = 0
      self.area_size = 800
      self.render_size = (1920, 1080)
      self.foodPositionX = (random.randint(1, 80) * 10) + (self.render_size[0] - self.area_size) // 2
      self.foodPositionY = (random.randint(1, 80) * 10) + (self.render_size[1] - self.area_size) // 2
      self.scoreX = self.render_size[0] // 2
      
      snake_score = 0