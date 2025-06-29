# `shadow` makes a displayable darken
transform shadow:
    matrixcolor TintMatrix("#FFFFFF") * SaturationMatrix(1.0)
    linear 0.5 matrixcolor TintMatrix("#4E4E4E") * SaturationMatrix(1.0)

# `light` makes a displayable lighten
transform light:
    linear 0.5 matrixcolor TintMatrix("#FFFFFF") * SaturationMatrix(1.0)

# Note. `chls` and `chrs` are the same except the xpos value.
#       However, if we made it a function, we couldn't use
#       it in a ATL block, e.g.
#           show charles:
#               ch_xpos(0.3)
#       since we would get an error saying "too complicated."
#
# Note. `chls` and `chrs` are intended to be used in tandem
#       with a character image such as `charles happy`.

# `chls` places a displayable at xpos=0.3.
transform chls:    # character at left side
    xpos 0.3 xanchor 0.5
    yalign 1.0

# `chrs` places a displayable at xpos=0.7.
transform chrs:   # character at right side
    xpos 0.7 xanchor 0.5
    yalign 1.0

# `disappear` makes a displayable disappear gradually.
transform disappear:
    linear 0.5 alpha 0.0

# `downup` gives a displayable a down-and-up motion.
transform downup:
    easein 0.3 yoffset 30
    easeout 0.3 yoffset 0

# `doup` is an alias of `downup`, since 'downup' is too long to type in.
transform doup:
    downup