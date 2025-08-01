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