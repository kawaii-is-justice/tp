# BGM
define audio.general1 = "audio/music/general1.mp3"
define audio.general2 = "audio/music/general2.mp3"
define audio.event = "audio/music/event.mp3"
define audio.end = "audio/music/end.mp3"

# SFX
define audio.car_accident = "audio/sfx/story/car_accident.wav"
define audio.dish_break = "audio/sfx/story/dish_break.wav"
define audio.rain = "audio/sfx/story/rain.mp3"

# Sound Channels
init python:
   renpy.music.register_channel("environment", loop=True)