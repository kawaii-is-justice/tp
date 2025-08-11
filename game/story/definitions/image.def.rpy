# Splash screen
image splscr_txt_presented_by = Text("presented by", size=72, color="#777", font="fonts/Galmuri11-Bold.ttf", xycenter=(0.5,0.4), yoffset=-30)
image splscr_txt_team_name = Text("귀여움은 정의다", size=128, color="#333", font="fonts/Galmuri11-Bold.ttf", xycenter=(0.5,0.5))
image splscr_txt_combined = Fixed("splscr_txt_presented_by", "splscr_txt_team_name")

# Background image definitions
image bg school classroom morning = ("bg/School_Classroom_Morning.png")
image bg school classroom midday = ("bg/School_Classroom_Midday.png")
image bg school classroom afternoon = ("bg/School_Classroom_Afternoon.png")
image bg school cafeteria = ("bg/School_Cafeteria.png")
image bg school yard = ("bg/School_Yard.png")
image bg school hallway = ("bg/School_Hallway.png")
image bg school library morning = ("bg/School_Library_Bright.png")
image bg school library afternoon = ("bg/School_Library_Dark.png")
image bg school nurseoffice = ("bg/School_Nurseoffice.png")
image bg school rooftop = ("bg/School_Rooftop.png")
image bg cafe lateafternoon = ("bg/Cafe_Afternoon.png")
image bg home bedroom night = ("bg/Home_Bedroom_Night.png")
image bg home kitchen = ("bg/Home_Kitchen_Night.png")
image bg white screen = ("bg/White_Screen.jpg")
image bg black screen = ("bg/Black_Screen.jpg")
image bg hospital = ("bg/Hospital.png")

# Character sprites image definitions
image nuri = Crop((0, -200, 1500, 1000), "images/nuri/nuri_base.png", zoom= 1.3)
image nuri say = Crop((0, -200, 1500, 1000),"images/nuri/nuri_say.png", zoom= 1.3)
image nuri smile = Crop((0, -200, 1500, 1000),"images/nuri/nuri_smile.png", zoom= 1.3)
image nuri smile blush = Crop((0, -200, 1500, 1000),"images/nuri/nuri_smile_blush.png", zoom= 1.3)
image nuri disappointed = Crop((0, -200, 1500, 1000),"images/nuri/nuri_disappointed.png", zoom= 1.3)
image nuri sad = Crop((0, -200, 1500, 1000),"images/nuri/nuri_sad.png", zoom= 1.3)
image nuri shy = Crop((0, -200, 1500, 1000),"images/nuri/nuri_shy.png", zoom= 1.3)
image nuri frown = Crop((0, -200, 1500, 1000),"images/nuri/nuri_frown.png", zoom= 1.3)
image nuri angry = Crop((0, -200, 1500, 1000),"images/nuri/nuri_angry.png", zoom= 1.3)
image nuri embarrassed = Crop((0, -200, 1500, 1000),"images/nuri/nuri_embarrassed.png", zoom= 1.3)

image hanl = Crop((0, -200, 1500, 1000),"images/hanl/hanl_base.png", zoom= 1.3)
image hanl say = Crop((0, -200, 1500, 1000),"images/hanl/hanl_say.png", zoom= 1.3)
image hanl smile = Crop((0, -200, 1500, 1000),"images/hanl/hanl_smile.png", zoom= 1.3)
image hanl smile blush = Crop((0, -200, 1500, 1000),"images/hanl/hanl_smile_blush.png", zoom= 1.3)
image hanl disappointed = Crop((0, -200, 1500, 1000),"images/hanl/hanl_disappointed.png", zoom= 1.3)
image hanl sad = Crop((0, -200, 1500, 1000),"images/hanl/hanl_sad.png", zoom= 1.3)
image hanl shy = Crop((0, -200, 1500, 1000),"images/hanl/hanl_shy.png", zoom= 1.3)
image hanl frown = Crop((0, -200, 1500, 1000),"images/hanl/hanl_frown.png", zoom= 1.3)
image hanl angry = Crop((0, -200, 1500, 1000),"images/hanl/hanl_angry.png", zoom= 1.3)
image hanl embarrassed = Crop((0, -200, 1500, 1000),"images/hanl/hanl_embarrassed.png", zoom= 1.3)

# Effects
image solid white = Solid("#FFFFFF")
image solid gray tp = Solid("#7F7F7F7F")

# Used in interlude
image nuri_char = "nuri down 2"
image nuri_char anim  = "nuri walk down"
image nuri_char anim2 = "nuri walk left"

image hanl_char   = Crop((40, 0, 40, 80), "charset hanl")
image hanl_char 1 = Crop(( 0, 0, 40, 80), "charset hanl")
image hanl_char 3 = Crop((80, 0, 40, 80), "charset hanl")
image hanl_char anim:
   "hanl_char 1"
   pause 0.25
   "hanl_char"
   pause 0.25
   "hanl_char 3"
   pause 0.25
   "hanl_char"
   pause 0.25
   repeat
image hanl_char 4 = Crop(( 0, 240, 40, 80), "charset hanl")
image hanl_char 5 = Crop((40, 240, 40, 80), "charset hanl")
image hanl_char 6 = Crop((80, 240, 40, 80), "charset hanl")
image hanl_char anim2:
   "hanl_char 4"
   pause 0.25
   "hanl_char 5"
   pause 0.25
   "hanl_char 6"
   pause 0.25
   "hanl_char 5"
   pause 0.25
   repeat