image charset hanl = "images/minigame/charset.hanl.png"
image tileset lib  = "images/minigame/tileset.lib.png"

screen minigame_tilestep(id):
   default game = TilestepMinigameCDD(f"map.{id}.dat")
   add game:
      xalign 0.5
      yalign 0.5
      zoom 1.0