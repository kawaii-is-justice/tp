# `shade` gives a displayable a gradual darken
transform shade:
    linear 0.5 matrixcolor TintMatrix("#777777")

# `light` gives a displayable a gradual lighten
transform light:
    linear 0.5 matrixcolor TintMatrix("#FFFFFF")

# `ishade` gives a displayable a instant darken
transform ishade:
    matrixcolor TintMatrix("#777777")

# `ilight` gives a displayable a instant lighten
transform ilight:
    matrixcolor TintMatrix("#FFFFFF")

# Note. `chls` and `chrs` are the same except the xpos value.
#       However, if we made it a function, we couldn't use
#       it in a ATL block, e.g.
#           show charles:
#               ch_xpos(0.3)
#       since we would get an error saying "too complicated."
#
# Note. `chls` and `chrs` are intended to be used in tandem
#       with a character image such as `charles happy`.

# `chls` places a displayable at xcenter=0.3.
transform chls:    # character at left side
    xcenter 0.3
    yalign 1.0

# `chrs` places a displayable at xcenter=0.7.
transform chrs:   # character at right side
    xcenter 0.7
    yalign 1.0

# `disappear` makes a displayable disappear gradually.
transform disappear:
    linear 0.5 alpha 0.0

# `appear` makes a displayable appear gradually.
transform appear:
    linear 0.5 alpha 1.0

# `doup` gives a displayable a down-and-up motion.
transform doup:     # down up, which is too long to type in.
    easein  0.3 yoffset 30
    easeout 0.3 yoffset 0