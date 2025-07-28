label splashscreen:
    scene expression Solid("#FFF")
    with dissolve
    pause 1.0

    play sound "audio/sfx/splash_screen/in.wav" volume 0.5 fadein 0.05

    show splscr_txt_presented_by with ComposeTransition(dissolve, after=easeintop)
    pause 1.0

    play sound "audio/sfx/splash_screen/title.wav"

    show splscr_txt_team_name with Dissolve(0.3)
    pause 1.5

    play sound "audio/sfx/splash_screen/out.wav" volume 0.5 fadeout 0.1

    hide splscr_txt_presented_by
    hide splscr_txt_team_name
    
    # With these uncommented, the two texts would move
    # as if they were in one shape.

    # show splscr_txt_combined
    # with None
    # hide splscr_txt_combined
    
    with ComposeTransition(dissolve, before=easeoutbottom)
    pause 1.0

    return

label start:
    stop music
    jump loop_0