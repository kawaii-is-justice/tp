"""renpy
init python:
"""

import pygame

class TitleScreenCDD(renpy.Displayable):
    def __init__(self, vpsiz, **kwargs):
        super(TitleScreenCDD, self).__init__(**kwargs)

        self.w, \
        self.h = vpsiz  # vpsiz = viewport size

        # Uses a canvas
        # self.bg = TitleScreenBackground()

        # Displayables
        # self.lb = TitleScreenLetterBox()
        # self.grid = TitleScreenGrid()
        self.title = TitleScreenTitle()
        self.menu = TitleScreenMenu()

    def render(self, width, height, st, at):
        # Update
        # self.grid.update(st)
        self.menu.update()

        # Render
        rdmain = renpy.Render(self.w, self.h)
        # rdgrid = renpy.render(self.grid.display, self.grid.w, self.grid.h, st, at)
        # rdlb = renpy.render(self.lb.display, self.lb.w, self.lb.h, st, at)
        rdtitle = renpy.render(self.title.display, self.title.w, self.title.h, st, at)
        rdmenu = renpy.render(self.menu.display, self.menu.w, self.menu.h, st, at)
        # cvs = rdmain.canvas()

        # self.bg.draw(cvs)
        # rdmain.blit(rdgrid, (0, 0))
        # rdmain.blit(rdlb, (0, 0))
        rdmain.blit(rdtitle, (self.title.left, self.title.top))
        rdmain.blit(rdmenu, (self.menu.left, self.menu.top))

        # Causes the next render
        renpy.redraw(self, 0)
        return rdmain
    
    def event(self, evt, x, y, st):
        self.menu.handle_event(evt, x, y, st)

        for disp in self.visit():
            disp.event(evt, x, y, st)
        return None

    def visit(self):
        return [self.menu.display]

class TitleScreenBackground:
    COLOR = "#FFDE63"

    def __init__(self):
        self.hue = TitleScreenBackground.COLOR
    
    def draw(self, cvs):
        coords = pygame.Rect(0, 0, gui.vpw, gui.vph)
        cvs.rect(self.hue, coords)

class TitleScreenLetterBox:
    LB_H = 100

    def __init__(self):
        self.w = gui.vpw
        self.h = TitleScreenLetterBox.LB_H

        self.topbox = Image("gui/title_screen/letbox.top.png")
        self.btmbox = Image("gui/title_screen/letbox.btm.png")
        self.display = Flatten(Composite((gui.vpw, gui.vph), (0, 0), self.topbox, (0, gui.vph - self.h), self.btmbox), drawable_resolution=False)

class TitleScreenTitle:
    DIMENSION = (700, 410)

    def __init__(self):
        self.w, \
        self.h = TitleScreenTitle.DIMENSION
        self.left = (gui.vpw - self.w) // 2
        self.top = 150
        self.display = Image("gui/title_screen/title.png")
        
class TitleScreenGrid:
    DELAY = 0.1
    CELL_SIZE = 40
    LAST_FRAME = 9

    def __init__(self):
        self.spritesheet = Image("gui/title_screen/gridcell.sprite.png")
        self.w = gui.vpw
        self.h = gui.vph
        self.csiz = TitleScreenGrid.CELL_SIZE
        self.lw = self.w // self.csiz
        self.lh = self.h // self.csiz
        self.delay = TitleScreenGrid.DELAY
        self.lf = TitleScreenGrid.LAST_FRAME
        self.cf = 0
        self.oldst = None
        self.dt = 0
        self.elapse = 0
        self.display = self.draw()

    def update(self, st):
        self.display = self.draw()
        self.manage_time(st)

    def manage_time(self, st):
        if self.oldst is None:
            self.oldst = st
        self.dt = st - self.oldst
        self.oldst = st

        if self.elapse < self.delay:
            self.elapse += self.dt
        else:
            self.elapse = 0
            if self.cf == self.lf:
                self.cf = 0
            else:
                self.cf += 1

    def draw(self):
        csiz = self.csiz
        cells = []
        
        for i in range(self.lh):
            for j in range(self.lw):
                x = csiz * self.cf
                y = 0
                w = csiz
                h = csiz

                pos = (j * csiz, i * csiz)
                frame = Crop((x,y,w,h), self.spritesheet)

                cells.extend([pos, frame])

        return Flatten(Composite((csiz * self.lw, csiz * self.lh), *cells), drawable_resolution=False)

class TitleScreenMenu:
    DIMENSION = (236, 260)

    def __init__(self):
        self.w, \
        self.h = TitleScreenMenu.DIMENSION
        self.left = (gui.vpw - self.w) // 2
        self.top = 670
        self.btns = [TitleScreenMenuBtn("start", 0), \
                     TitleScreenMenuBtn("load",  1), \
                     TitleScreenMenuBtn("pref",  2), \
                     TitleScreenMenuBtn("quit",  3)]
        self.display = self.make_display()
        self.hotspot = self.get_hotspot()

    def handle_event(self, evt, x, y, st):
        # hover check
        hovered = -1
        for i in range(len(self.btns)):
            hs = self.hotspot[i]
            xcond = hs['x0'] <= x and x <= hs['x1']
            ycond = hs['y0'] <= y and y <= hs['y1']
            if xcond and ycond:
                btn = self.btns[i]
                if btn.state != "hover":
                    renpy.sound.play("sfx/btn/hover.wav")
                btn.state = "hover"
                hovered = i
            else:
                self.btns[i].state = "idle"
        
        if hovered == -1:
            return
        
        if evt.type == pygame.MOUSEBUTTONUP:
            renpy.sound.play("sfx/btn/click.wav")
            if hovered == 0:
                renpy.run(Start())
            elif hovered == 1:
                renpy.run(ShowMenu('load'))
            elif hovered == 2:
                renpy.run(ShowMenu('preferences'))
            elif hovered == 3:
                renpy.run(Quit(confirm=False))
    
    def get_hotspot(self):
        hotspots = []
        
        for btn in self.btns:
            x0 = self.left + btn.left
            y0 = self.top  + btn.top
            x1 = x0 + TitleScreenMenuBtn.W
            y1 = y0 + TitleScreenMenuBtn.H
            hotspots.append({ 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'idx': btn.idx })
        
        return hotspots
    
    def make_display(self):
        menuframe = Image("gui/title_screen/menuframe.png")
        rootpos = (0,0)
        elem = [rootpos, menuframe]
        for btn in self.btns:
            btn.update_display()
            elem.extend([btn.pos, btn.disp])
        
        assembly = Flatten(Composite((self.w, self.h), *elem), drawable_resolution=False)

        return assembly

    def update(self):
        self.display = self.make_display()

class TitleScreenMenuBtn:
    W = 212
    H = 56
    XPAD = 12   # x dist. b/w the frame and this btn
    YPAD = 12   # y dist. b/w the frame and this btn
    SPAN = 4    # dist. b/w two btns

    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        self.left = TitleScreenMenuBtn.XPAD
        self.top = TitleScreenMenuBtn.YPAD + \
                   TitleScreenMenuBtn.H * idx + \
                   TitleScreenMenuBtn.SPAN * idx
        self.pos = (self.left, self.top)
        self.disp = Null()
        self.state = "idle"
    
    def update_display(self):
        self.disp = Image(f"gui/title_screen/menubtn.{self.name}.{self.state}.png")