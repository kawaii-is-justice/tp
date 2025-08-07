image charset hanl = "images/minigame/charset.hanl.png"
image tileset lib  = "images/minigame/tileset.lib.png"

image tileset house = "images/minigame/tileset.house.png"
image charset nuri = "images/minigame/charset.nuri.png"
image nuri down 1 = Crop((0, 0, 40, 80), "charset nuri")
image nuri down 2 = Crop((40, 0, 40, 80), "charset nuri")
image nuri down 3 = Crop((80, 0, 40, 80), "charset nuri")
image nuri left 1 = Crop((0, 80, 40, 80), "charset nuri")
image nuri left 2 = Crop((40, 80, 40, 80), "charset nuri")
image nuri left 3 = Crop((80, 80, 40, 80), "charset nuri")
image nuri up 1 = Crop((0, 160, 40, 80), "charset nuri")
image nuri up 2 = Crop((40, 160, 40, 80), "charset nuri")
image nuri up 3 = Crop((80, 160, 40, 80), "charset nuri")
image nuri right 1 = Crop((0, 240, 40, 80), "charset nuri")
image nuri right 2 = Crop((40, 240, 40, 80), "charset nuri")
image nuri right 3 = Crop((80, 240, 40, 80), "charset nuri")
image nuri walk down:
   "nuri down 1"
   pause 0.25
   "nuri down 2"
   pause 0.25
   "nuri down 3"
   pause 0.25
   "nuri down 2"
   pause 0.25
   repeat
image nuri walk left:
   "nuri left 1"
   pause 0.25
   "nuri left 2"
   pause 0.25
   "nuri left 3"
   pause 0.25
   "nuri left 2"
   pause 0.25
   repeat
image nuri walk up:
   "nuri up 1"
   pause 0.25
   "nuri up 2"
   pause 0.25
   "nuri up 3"
   pause 0.25
   "nuri up 2"
   pause 0.25
   repeat
image nuri walk right:
   "nuri right 1"
   pause 0.25
   "nuri right 2"
   pause 0.25
   "nuri right 3"
   pause 0.25
   "nuri right 2"
   pause 0.25
   repeat

screen minigame_tilestep(id):
   default game = TilestepMinigameCDD(f"map.{id}.dat")
   add game:
      xalign 0.5
      yalign 0.5
      zoom 2.0

screen testScreen():
   # $ snake = SnakeMinigameCDD()
   $ snake = NurigameCDD()
   add snake:
      align (.5,.5)

style SnakeScore_text:
   font "gui/fonts/Galmuri11-Bold.ttf"
   color "#FFF"
   yalign 0.5

label snakeGame:
   show screen testScreen
   pause
   return