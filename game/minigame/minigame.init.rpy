image charset hanl = "images/minigame/charset.hanl.png"
image tileset lib  = "images/minigame/tileset.lib.png"

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