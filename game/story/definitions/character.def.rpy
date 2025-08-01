# Character definitions
# Note: refer to https://www.renpy.org/doc/html/dialogue.html#the-character-store
define narrator = Character( \
    name=None, \
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

# protagonist
define character.p = Character( \
    "prtname", dynamic=True, color="#AAAAAA",
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.n = Character( \
    "누리", color="#FFAEC9",
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.h = Character( \
    "하늘", color="#99D9EA",
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.p_noname = Character( \
    "주인공", color="#AAAAAA", \
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.stranger = Character( \
    "???", color="#777777", \
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.pe_teacher = Character( \
    "체육 선생님", color="#777777",
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.school_nurse = Character( \
    "보건 선생님", color="#777777",
    ctc="ctc usual", \
    ctc_pause="ctc pause", \
    ctc_timedpause="ctc timedpause", \
    ctc_position="nestled-close")

define character.syswarn = Character("시스템 경고", color="#FF0000")