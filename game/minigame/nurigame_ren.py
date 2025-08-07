"""renpy
init python:
"""

import random, pygame, time

class NurigameCDD(renpy.Displayable):
   TILE_SIZE = 40
   CHAR_DOWN = renpy.displayable("nuri walk down")
   CHAR_LEFT = renpy.displayable("nuri walk left")
   CHAR_UP = renpy.displayable("nuri walk up")
   CHAR_RIGHT = renpy.displayable("nuri walk right")
   CHAR_GAMEEND = renpy.displayable("nuri down 2")
   ITEM_COLLECTED_DISP = Transform("images/minigame/cookie.png", zoom=0.25)
   ITEM_SPAWNED_DISP = Transform("images/minigame/pie.png", zoom=0.25)
   ITEM_BAD = Transform("images/minigame/pufferfish.png", zoom=0.25)
   BG_DISP = Solid("#777")
   STAGESIZ = 20  # actual field size is 16x16
   STAGEPAD = 4

   def __init__(self, **kwargs):
      super(NurigameCDD, self).__init__(**kwargs)
      self.lw = NurigameCDD.STAGESIZ  # logical width
      self.lh = NurigameCDD.STAGESIZ  # logical height
      self.pad = NurigameCDD.STAGEPAD
      self.tsiz = NurigameCDD.TILE_SIZE
      self.w = self.lw * self.tsiz
      self.h = self.lh * self.tsiz
      self.time_ended = None
      self.game_ended = False
      self.leave_ready = False

      self.char = NurigameCDD.CHAR_RIGHT
      self.icol = NurigameCDD.ITEM_COLLECTED_DISP
      self.ispwn = NurigameCDD.ITEM_SPAWNED_DISP
      self.ibad = NurigameCDD.ITEM_BAD
      self.bg = NurigameCDD.BG_DISP

      self.init_game()

   def init_game(self):
      center_x = (self.lw - self.pad) // 2
      center_y = (self.lh - self.pad) // 2
      self.segments = [[center_x, center_y]]
      self.direction = (1,0)
      self.redraw_time = 0.1   # thus determines the move speed.
      self.item_count = 0
      self.item_pos = (center_x + 2, center_y + 2)
      self.btem_pos = (center_x - 2, center_y - 2)

   def end_game(self):
      self.game_ended = True
      self.char = NurigameCDD.CHAR_GAMEEND
      # renpy.pause(delay=1.0)
      # renpy.timeout(0)

   def spawn_item(self):
      halfpad = self.pad // 2

      while True:
         x = random.randint(halfpad, self.lw - halfpad)
         y = random.randint(halfpad, self.lh - halfpad)

         if (x,y) == self.btem_pos:
            continue
         for segment in self.segments:
            if (x,y) == segment:
               continue
         break
      
      return (x,y)

   def update(self):
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
      xcond = col_pos[0] == 0 or col_pos[0] == self.lw - 1
      ycond = col_pos[1] == 0 or col_pos[1] == self.lh - 1
      if xcond or ycond:
         # self.init_game()
         self.end_game()

      # Check if char has collided with itself.
      if len(self.segments) > 5:
         for segment in self.segments[1:]:
            xcond = col_pos[0] == segment[0]
            ycond = col_pos[1] == segment[1]
            if xcond and ycond:
               # self.init_game()
               self.end_game()

   def gen_map(self):
      tiles = []
      lw = self.lw
      lh = self.lh

      # fill tiles
      for y in range(0, lh):
         line = []
         for x in range(0, lw):
            line.append(12)
         tiles.append(line)
      
      # set corners
      lx = lw - 1
      ilx = lx - 1
      ly = lh - 1
      ily = ly - 1

      tiles[0][0] = 20
      tiles[0][lx] = 23
      tiles[ly][0] = 21
      tiles[ly][lx] = 22

      tiles[1][1] = 3
      tiles[1][ilx] = 2
      tiles[ily][1] = 1
      tiles[ily][ilx] = 0

      # set walls
      for x in range(2, ilx):
         tiles[1][x] = 7
         tiles[ily][x] = 6
      for y in range(2, ily):
         tiles[y][1] = 4
         tiles[y][ilx] = 5

      # manipulate specific tiles
      for segment in self.segments[1:]:
         sx = segment[0]
         sy = segment[1]
         tiles[sy][sx] = 15
      
      itemx = self.item_pos[0]
      itemy = self.item_pos[1]
      tiles[itemy][itemx] = 13

      btemx = self.btem_pos[0]
      btemy = self.btem_pos[1]
      tiles[btemy][btemx] = 14
      print(tiles)
      return tiles

   def ts2crd(self, ts):
      q = ts // 4
      r = ts % 4
      q *= self.tsiz
      r *= self.tsiz
      return (r,q)

   def get_field(self, ts):
      tz = self.tsiz
      lw = self.lw
      lh = self.lh
      w = self.w
      h = self.h

      args = []

      for i in range(lh):
         for j in range(lw):
            x,y = self.ts2crd(ts[i][j])
            w,h = tz,tz
            args.append((j * tz, i * tz))
            args.append(Crop((x,y,w,h), "tileset house"))

      return Flatten(Composite((w,h), *args), drawable_resolution=False)


   def render(self, width, height, st, at):
      if not self.game_ended:
         self.update()

      # Render
      text = Text(f"Score: {self.item_count}", size=gui.rfsiz)
      char = self.char
      icol = self.icol
      ispwn = self.ispwn
      ibad = self.ibad
      bg = self.get_field(self.gen_map())

      s = self.tsiz
      c = self.segments[0]

      rdmain = renpy.Render(self.w, self.h)
      rdtext = renpy.render(text, width, height, st, at)
      rdchar = renpy.render(char, width, height, st, at)
      rdicol = renpy.render(icol, width, height, st, at)
      rdispwn = renpy.render(ispwn, width, height, st, at)
      rdibad = renpy.render(ibad, width, height, st, at)
      rdbg = renpy.render(bg, self.w, self.h, st, at)

      rdmain.blit(rdbg, (0, 0))
      rdmain.blit(rdtext, (0, 0))
      for segment in self.segments[1:]:
         rdmain.blit(rdicol, tuple(s * n for n in segment))
      rdmain.blit(rdispwn, tuple(s * n for n in self.item_pos))
      rdmain.blit(rdibad, tuple(s * n for n in self.btem_pos))
      # rdmain.blit(rdchar, tuple(s * n for n in self.segments[0]))
      rdmain.blit(rdchar, (s * c[0], s * (c[1] - 1)))
      
      renpy.redraw(self, self.redraw_time)

      if self.game_ended:
         now = time.time()
         te = self.time_ended

         if te is None:
            self.time_ended = now
         elif now - te >= 1.0:
               self.leave_ready = True
               renpy.timeout(0)

      return rdmain

   def event(self, e, x, y, st):
      if self.leave_ready:
         return self.item_count
      if self.game_ended:
         raise renpy.IgnoreEvent()

      if e.type != pygame.KEYDOWN:
         return
      
      if e.key == pygame.K_UP:
         if self.direction == (0,1): return
         self.direction = (0,-1)
         self.char = NurigameCDD.CHAR_UP
      elif e.key == pygame.K_DOWN:
         if self.direction == (0,-1): return
         self.direction = (0,1)
         self.char = NurigameCDD.CHAR_DOWN
      elif e.key == pygame.K_LEFT:
         if self.direction == (1,0): return
         self.direction = (-1,0)
         self.char = NurigameCDD.CHAR_LEFT
      elif e.key == pygame.K_RIGHT:
         if self.direction == (-1,0): return
         self.direction = (1,0)
         self.char = NurigameCDD.CHAR_RIGHT