image charset hanl = "images/minigame/charset.hanl.png"
image tileset lib  = "images/minigame/tileset.lib.png"

image charset nuri = "images/minigame/charset.nuri.png"
image nuri down 1 = Crop((0, 0, 40, 80), "charset nuri")
image nuri down 2 = Crop((40, 0, 40, 80), "charset nuri")
image nuri down 3 = Crop((80, 0, 40, 80), "charset nuri")
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

screen minigame_tilestep(id):
   default game = TilestepMinigameCDD(f"map.{id}.dat")
   add game:
      xalign 0.5
      yalign 0.5
      zoom 1.0

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