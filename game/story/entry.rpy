label splashscreen:
    scene expression Solid("#FFF")
    with dissolve
    pause 1.0

    show splashscreen_text "귀여움은 정의다" at truecenter with ComposeTransition(dissolve, after=easeintop)
    pause 1.5

    hide splashscreen_text with ComposeTransition(dissolve, before=easeoutbottom)
    pause 1.0

    return

label start:
    jump loop_0