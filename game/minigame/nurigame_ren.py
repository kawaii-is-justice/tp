"""renpy
init python:
"""

import random, pygame

class NurigameCDD(renpy.Displayable):
   TILE_SIZE = 40

   def __init__(self, **kwargs):
      super(NurigameCDD, self).__init__(**kwargs)
      self.lw = 12  # logical width
      self.lh = 12  # logical height
      self.tsiz = NurigameCDD.TILE_SIZE
      self.w = self.lw * self.tsiz
      self.h = self.lh * self.tsiz

      self.init_game()

   def init_game(self):
      self.segments = [[3,3]]
      self.direction = (1,0)
      self.redraw_time = 0.2   # thus determines the move speed.
      self.item_count = 0
      self.item_pos = self.spawn_item()

   def spawn_item(self):
      x = random.randint(1, self.lw - 2)
      y = random.randint(1, self.lh - 2)
      return (x,y)

   def render(self, width, height, st, at):
      # Update first before drawing.
      tail = self.segments[-1]
      head = self.segments[0]

      #prev = head
      px = head[0]
      py = head[1]
      for segment in self.segments[1:]:
         # Pass the coords onto the next segment.
         tx = segment[0]
         ty = segment[1]
         segment[0] = px
         segment[1] = py
         px = tx
         py = ty
         #temp = segment
         #segment = prev
         #prev = temp

      head[0] += self.direction[0]
      head[1] += self.direction[1]

      # Check if char has collided with item.
      col_pos = (head[0], head[1] + 1)  # char = 80px, tile = 40px

      if col_pos == self.item_pos:
         self.segments.insert(len(self.segments), [tail[0], tail[1]])
         #self.segments.insert(len(self.segments), tail)

         self.item_pos = self.spawn_item()
         self.item_count += 1

         if self.redraw_time > 0.1:
            self.redraw_time -= 0.02
      
      # Check if char has collided with walls.
      xcond = col_pos[0] == 0 or col_pos[0] == 11
      ycond = col_pos[1] == 0 or col_pos[1] == 11
      if xcond or ycond:
         self.init_game()

      # Check if char has collided with itself.
      for segment in self.segments[1:]:
         if col_pos == segment:
            self.init_game()

      # Render
      text = Text(f"Score: {self.item_count}", size=gui.rfsiz)
      char = Image("gui/title_screen/hanl.png")
      item = Transform("images/minigame/cookie.png", zoom=0.25)
      food = Transform("images/minigame/pie.png", zoom=0.25)
      bg = Solid("#777")

      rdmain = renpy.Render(self.w, self.h)
      rdtext = renpy.render(text, width, height, st, at)
      rdchar = renpy.render(char, width, height, st, at)
      rditem = renpy.render(item, width, height, st, at)
      rdfood = renpy.render(food, width, height, st, at)
      rdbg = renpy.render(bg, 480, 480, st, at)

      rdmain.blit(rdbg, (0, 0))
      rdmain.blit(rdtext, (0, 0))
      for segment in self.segments[1:]:
         rdmain.blit(rditem, tuple(self.tsiz * n for n in segment))
      rdmain.blit(rdfood, tuple(self.tsiz * n for n in self.item_pos))
      rdmain.blit(rdchar, tuple(self.tsiz * n for n in self.segments[0]))
      
      renpy.redraw(self, self.redraw_time)
      return rdmain

   def event(self, e, x, y, st):
      if e.type != pygame.KEYDOWN:
         return
      
      if e.key == pygame.K_UP:
         if self.direction == (0,1): return
         self.direction = (0,-1)
      elif e.key == pygame.K_DOWN:
         if self.direction == (0,-1): return
         self.direction = (0,1)
      elif e.key == pygame.K_LEFT:
         if self.direction == (1,0): return
         self.direction = (-1,0)
      elif e.key == pygame.K_RIGHT:
         if self.direction == (-1,0): return
         self.direction = (1,0)