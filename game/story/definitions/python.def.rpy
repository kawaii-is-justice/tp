init python:
    # `get_name` prompts a user to input a name.
    # banlist: an array of strings which can't be a name.
    def get_name(banlist):
        while True:
            # Note: refer to https://www.renpy.org/doc/html/input.html
            tempname = renpy.input(prompt="당신의 이름은?", default="길동", length=16)
            tempname = tempname.strip()

            if tempname in banlist:
                msg = "\n{color=%s}%s{/color}\n적절한 이름이 아닙니다." % (gui.accent_color, tempname)
                narrator(msg)
                continue
            
            # Note: refer to https://www.renpy.org/doc/html/statement_equivalents.html
            msg = "\n{color=%s}%s{/color}\n이 이름이 맞습니까?" % (gui.selected_color, tempname)
            narrator(msg, interact=False)
            result = renpy.display_menu([("그렇다", "y"), ("아니다", "n")])

            if result == "y":
                break
            else:
                pass
        
        return tempname

    def disable_save():
        global quick_menu, _game_menu_screen, config
        quick_menu = False
        _game_menu_screen = None  # disable esc
        config.rollback_enabled = False
        renpy.clear_keymap_cache()
        config.keymap['skip'].remove('anymod_K_LCTRL')
        config.keymap['skip'].remove('anymod_K_RCTRL')

    def enable_save():
        global quick_menu, _game_menu_screen, config
        renpy.block_rollback()
        config.rollback_enabled = True
        _game_menu_screen = "save"
        quick_menu = True
        renpy.clear_keymap_cache()
        config.keymap['skip'].append('anymod_K_LCTRL')
        config.keymap['skip'].append('anymod_K_RCTRL')