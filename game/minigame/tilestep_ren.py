"""renpy
init python:
"""

import pygame, time, copy, pickle

TILE_SIZE = 40

# Actual position to logical position
# ex: (40px, 80px) => (1, 2)
def ap2lp(ax, ay):
    lx = int(ax / TILE_SIZE)
    ly = int(ay / TILE_SIZE)
    return [lx, ly]

# Reverse of `ap2lp`
def lp2ap(lx, ly):
    ax = int(lx * TILE_SIZE)
    ay = int(ly * TILE_SIZE)
    return [ax, ay]

# Returns the number of columns and rows
# ex: [[1,2,3], [1,2,3]] => (3, 2)
def get_stage_size(list):
    return (len(list[0]), len(list))

class TilestepCharacter:
    WALK_DELAY = 0.12 # sec
    WALK_UNIT = TILE_SIZE # px
    WIDTH = 40
    HEIGHT = 80

    def __init__(self, init_pos):
        self.display = Null()
        self.w = TilestepCharacter.WIDTH
        self.h = TilestepCharacter.HEIGHT
        self.x, self.y = lp2ap(init_pos[0], init_pos[1] - 1) # at character feet
        self.elapse = None # keeps track of the time after the last walk
        self.direction = None
        self.last_direction = pygame.K_DOWN
        self.first_frame = True
        # self.first_item = True
        self.walking = False
        # self.actable = False
        # self.swappable = True
        self.step_count = 0
        self.walk_delay = TilestepCharacter.WALK_DELAY
        self.walk_unit = TilestepCharacter.WALK_UNIT

    def handle_event(self, evt, x, y, st):
        self.handle_move_keys(evt)
        # self.handle_act_keys(evt)

    def handle_move_keys(self, evt):
        d = self.direction
        e = self.elapse

        valid_evts = [pygame.KEYUP, pygame.KEYDOWN]
        valid_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

        if evt.type not in valid_evts or evt.key not in valid_keys:
            return

        if evt.type == pygame.KEYDOWN:
            if d is None or d != evt.key:
                self.direction = evt.key
                self.elapse = self.walk_delay
        elif evt.type == pygame.KEYUP:
            if d == evt.key:
                self.last_direction = self.direction
                self.direction = None
                self.elapse = None

   #  def handle_act_keys(self, evt):
   #      valid_evts = [pygame.KEYUP, pygame.KEYDOWN]
   #      valid_keys = [pygame.K_e, pygame.K_SPACE]

   #      if evt.type not in valid_evts or evt.key not in valid_keys:
   #          return
        
   #      if evt.type == pygame.KEYDOWN:
   #          if evt.key == pygame.K_e:
   #              self.swap_item()
   #          elif evt.key == pygame.K_SPACE:
   #              self.actable = True
   #      elif evt.type == pygame.KEYUP:
   #          if evt.key == pygame.K_e:
   #              self.swappable = True

    def update(self, master):
        dt = master.dt
        ts = master.stage.tile_state

        self.place(dt,ts)
        self.animate()

        x, y = ap2lp(self.x, self.y)
        y += 1  # at character feet

        self.walk_on_tile(x,y,ts)
        # self.act_on_tile(x,y,ts)

    def place(self, dt, tile_state):
        d = self.direction
        unit = self.walk_unit
        x, y = self.x, self.y
        ts = tile_state

        # no keydown is triggered
        if d is None:
            return
        
        # too early to make a walk
        if self.elapse < self.walk_delay:
            self.elapse += dt
            return

        # now it's enough to make a walk
        self.elapse = 0.0

        if not self.movable(d,x,y,ts):
            renpy.sound.play("audio/sfx/minigame/collide.wav")
            return

        if   d == pygame.K_UP:    self.y -= unit
        elif d == pygame.K_DOWN:  self.y += unit
        elif d == pygame.K_LEFT:  self.x -= unit
        elif d == pygame.K_RIGHT: self.x += unit

        self.walking = True
        renpy.sound.play("audio/sfx/minigame/move.wav")
        self.step_count += 1
        # renpy.restart_interaction() # updates the screen

    def movable(self, d, ax, ay, tile_state):
        lx, ly = ap2lp(ax, ay)
        ly += 1 # at character feet

        if   d == pygame.K_UP:    ly -= 1
        elif d == pygame.K_DOWN:  ly += 1
        elif d == pygame.K_LEFT:  lx -= 1
        elif d == pygame.K_RIGHT: lx += 1

        ts = tile_state[ly][lx]
        if not (0x0D <= ts and ts <= 0x12):
            return False
        return True

    def animate(self):
        # when keyup or initialized
        if self.elapse is None:
            self.display = self.get_display(1)
        
        # while keydown
        elif self.elapse == 0.0:
            self.display = self.get_display(0) if self.first_frame else self.get_display(2)
            self.first_frame = not self.first_frame

    def get_display(self, index):
        sw = self.w
        sh = self.h
        d = self.last_direction if self.direction is None else self.direction

        x = sw * index
        y = sh
        w = sw
        h = sh
        
        if   d == pygame.K_UP:    y *= 2
        elif d == pygame.K_DOWN:  y *= 0
        elif d == pygame.K_LEFT:  y *= 1
        elif d == pygame.K_RIGHT: y *= 3

        return Crop((x,y,w,h), "charset hanl")

    def walk_on_tile(self, x, y, tile_state):
        if not self.walking:
            return

        ts = tile_state
        t = ts[y][x]

        if t == 0x12:
            ts[y][x] = 0x11
        elif t == 0x11:
            ts[y][x] = 0x10
        elif t == 0x10:
            ts[y][x] = 0x0F
      #   elif t == 8 or t == 9:
      #       ts[y][x] = 3

        self.walking = False

   #  def act_on_tile(self, x, y, tile_state):
   #      if not self.actable:
   #          return
        
   #      self.actable = False
   #      ts = tile_state

   #      if ts[y][x] != 2:
   #          return
        
   #      item = 8 if self.first_item else 9
   #      ts[y][x] = item

   #  def swap_item(self):
   #      if not self.swappable:
   #          return

   #      self.first_item = not self.first_item
   #      self.swappable = False
        
   #      renpy.restart_interaction() # updates the screen

class TilestepStage:
    def __init__(self, init_stage):
        self.display = Null()
        self.tile_size = TILE_SIZE
        self.lw, self.lh = get_stage_size(init_stage)
        self.w = self.lw * self.tile_size
        self.h = self.lh * self.tile_size
        self.tile_state = copy.deepcopy(init_stage)
        # self.elapse = 0.0
        # self.first_frame = False
        # self.anim_delay = 0.5

   #  def handle_event(self, evt, x, y, st):
   #      valid_evts = [pygame.KEYDOWN]
   #      valid_keys = [pygame.K_SPACE]

   #      if evt.type not in valid_evts or evt.key not in valid_keys:
   #          return
   #      pass
    
    def update(self, master):
        self.draw(master.dt)
        if master.game_end:
            return
        if self.check_game_end(master):
            master.game_end = True
            c = master.char
            c.last_direction = pygame.K_DOWN
            c.direction = None
            c.elapse = None
    
    def check_game_end(self, master):
        char = master.char
        end_stage = master.end_stage
        x, y = ap2lp(char.x, char.y)
        y += 1 # tile at character feet

        if [x,y] != master.end_char_pos:
            return False
        
        diff_counter = 0
        for i in range(self.lh):
            for j in range(self.lw):
                if master.end_stage[i][j] != self.tile_state[i][j]:
                    diff_counter += 1
        
        if diff_counter == 0:
            master.game_result = "perfect"
        elif diff_counter <= 3:
            master.game_result = "not bad"
        else:
            master.game_result = "bad"

        return True

    def draw(self, dt):
        tsiz = self.tile_size
        # ff = self.first_frame
        lw, lh = get_stage_size(self.tile_state)
        tiles = []

        # animate tiles
        # if self.elapse < self.anim_delay:
        #     self.elapse += dt
        # else:
        #     self.elapse = 0.0
        #     self.first_frame = not ff
        
        for i in range(lh):
            for j in range(lw):
                x,y = self.ts2crd(self.tile_state[i][j])
                # x = tsiz * self.tile_state[i][j]
                # y = 0 if not ff else tsiz
                w = tsiz
                h = tsiz
                
                tiles.append((j * tsiz, i * tsiz))
                tiles.append(Crop((x,y,w,h), "tileset lib"))
        
        self.display = Flatten(Composite((tsiz * lw, tsiz * lh), *tiles), drawable_resolution=False)

    # `ts2crd` maps a tile state to a coordinate in a tileset.
    def ts2crd(self, ts):
        q = ts // 4
        r = ts % 4
        return (r * 40, q * 40)
        
class TilestepMinigameCDD(renpy.Displayable):
    def __init__(self, map_file, **kwargs):
        super(TilestepMinigameCDD, self).__init__(**kwargs)

        with renpy.open_file(f"minigame/map/{map_file}") as file:
            dict = pickle.load(file)
            self.init_stage, \
            self.end_stage, \
            self.init_char_pos, \
            self.end_char_pos = dict.values()
        
        self.oldst = None
        self.dt = None
        self.game_end = False
        self.game_result = ""
        self.time_ended = None
        self.leave_ready = False
        self.lw, self.lh = get_stage_size(self.init_stage)
        self.w, self.h = self.lw * TILE_SIZE, self.lh * TILE_SIZE

        # displayables
        self.stage = TilestepStage(self.init_stage)
        self.char = TilestepCharacter(self.init_char_pos)

    def render(self, width, height, st, at):
        # sets dt, oldst
        if self.oldst is None:
            self.oldst = st
        self.dt = st - self.oldst
        self.oldst = st
        
        # updates before drawing
        self.stage.update(self)
        self.char.update(self)

        # draws displayables
        main_render = renpy.Render(self.w, self.h)
        stage_render = renpy.render(self.stage.display, self.stage.w, self.stage.h, st, at)
        char_render = renpy.render(self.char.display, self.char.w, self.char.h, st, at)

        main_render.blit(stage_render, (0, 0))
        main_render.blit(char_render, (self.char.x, self.char.y))

        # causes next draw
        renpy.redraw(self, 0)

        if self.game_end:
            now = time.time()
            te = self.time_ended

            if te is None:
                self.time_ended = now
            elif now - te >= 1.0:
                self.leave_ready = True
                renpy.timeout(0)    # causes `event()`

        return main_render
    
    def event(self, evt, x, y, st):
        if self.leave_ready:
            return { 'res': self.game_result, 'cnt': self.char.step_count }
        if self.game_end:
            raise renpy.IgnoreEvent()

        # Processes the event in the way each object wants.
        # self.stage.handle_event(evt, x, y, st)
        self.char.handle_event(evt, x, y, st)

        # Propagates the event to the child displayables.
        # for disp in self.visit():
        #     disp.event(evt, x, y, st)
        return None

    # Note: `visit` returns displayables.
    def visit(self):
        return [self.stage.display, self.char.display]