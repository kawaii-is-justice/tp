"""renpy
init python:
"""

import random, pygame

class NurigameCDD(renpy.Displayable):
   TILE_SIZE = 40
   CHAR_DISP = renpy.displayable("nuri walk down")
   CHAR_GAMEEND = renpy.displayable("nuri walk down 2")
   ITEM_COLLECTED_DISP = Transform("images/minigame/cookie.png", zoom=0.25)
   ITEM_SPAWNED_DISP = Transform("images/minigame/pie.png", zoom=0.25)
   ITEM_BAD = Transform("images/minigame/pufferfish.png", zoom=0.25)
   BG_DISP = Solid("#777")

   def __init__(self, **kwargs):
      super(NurigameCDD, self).__init__(**kwargs)
      self.lw = 12  # logical width
      self.lh = 12  # logical height
      self.tsiz = NurigameCDD.TILE_SIZE
      self.w = self.lw * self.tsiz
      self.h = self.lh * self.tsiz
      self.time_ended = None
      self.game_ended = False
      self.leave_ready = False

      self.char = NurigameCDD.CHAR_DISP
      self.icol = NurigameCDD.ITEM_COLLECTED_DISP
      self.ispwn = NurigameCDD.ITEM_SPAWNED_DISP
      self.ibad = NurigameCDD.ITEM_BAD
      self.bg = NurigameCDD.BG_DISP

      self.init_game()

   def init_game(self):
      self.segments = [[3,3]]
      self.direction = (1,0)
      self.redraw_time = 0.25   # thus determines the move speed.
      self.item_count = 0
      self.item_pos = self.spawn_item()
      self.btem_pos = self.spawn_item()

   def end_game(self):
      self.game_ended = True
      self.char = NurigameCDD.CHAR_GAMEEND
      renpy.pause(delay=1.0)
      renpy.timeout(0)

   def spawn_item(self):
      x = random.randint(1, self.lw - 2)
      y = random.randint(1, self.lh - 2)
      return (x,y)

   def render(self, width, height, st, at):
      # Update first before drawing.
      tail = self.segments[-1]
      head = self.segments[0]

      prev_x = head[0]
      prev_y = head[1]
      for segment in self.segments[1:]:
         # Pass the coords onto the next segment.
         temp_x = segment[0]
         temp_y = segment[1]
         segment[0] = prev_x
         segment[1] = prev_y
         prev_x = temp_x
         prev_y = temp_y

      head[0] += self.direction[0]
      head[1] += self.direction[1]

      # Check if char has collided with item.
      col_pos = (head[0], head[1])  # char = 80px, tile = 40px

      if col_pos == self.item_pos:
         self.segments.insert(len(self.segments), [tail[0], tail[1]])

         self.item_pos = self.spawn_item()
         self.item_count += 1

         # if self.redraw_time > 0.15:
         #    self.redraw_time -= 0.01

      # Check if char has collided with bad item.
      if col_pos == self.btem_pos:
         if len(self.segments) == 1:
            # self.init_game()
            self.end_game()
         else:
            self.segments.pop()
            self.btem_pos = self.spawn_item()
            self.item_count -= 1
      
      # Check if char has collided with walls.
      xcond = col_pos[0] == 0 or col_pos[0] == 11
      ycond = col_pos[1] == 0 or col_pos[1] == 11
      if xcond or ycond:
         # self.init_game()
         self.end_game()

      # Check if char has collided with itself.
      if len(self.segments) > 2:
         for segment in self.segments[1:]:
            xcond = col_pos[0] == segment[0]
            ycond = col_pos[1] == segment[1]
            if xcond and ycond:
               # self.init_game()
               self.end_game()

      # Render
      text = Text(f"Score: {self.item_count}", size=gui.rfsiz)
      char = self.char
      icol = self.icol
      ispwn = self.ispwn
      ibad = self.ibad
      bg = self.bg

      s = self.tsiz
      c = self.segments[0]

      rdmain = renpy.Render(self.w, self.h)
      rdtext = renpy.render(text, width, height, st, at)
      rdchar = renpy.render(char, width, height, st, at)
      rdicol = renpy.render(icol, width, height, st, at)
      rdispwn = renpy.render(ispwn, width, height, st, at)
      rdibad = renpy.render(ibad, width, height, st, at)
      rdbg = renpy.render(bg, 480, 480, st, at)

      rdmain.blit(rdbg, (0, 0))
      rdmain.blit(rdtext, (0, 0))
      for segment in self.segments[1:]:
         rdmain.blit(rdicol, tuple(s * n for n in segment))
      rdmain.blit(rdispwn, tuple(s * n for n in self.item_pos))
      rdmain.blit(rdibad, tuple(s * n for n in self.btem_pos))
      # rdmain.blit(rdchar, tuple(s * n for n in self.segments[0]))
      rdmain.blit(rdchar, (s * c[0], s * (c[1] - 1)))
      
      renpy.redraw(self, self.redraw_time)
      return rdmain

   def event(self, e, x, y, st):
      if self.game_ended == True:
         return self.score

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