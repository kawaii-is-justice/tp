init python:
    # `set_name` prompts a user to input a name.
    def set_name():
        global prtname
        global banned_names

        while True:
            # refer to https://www.renpy.org/doc/html/input.html
            prtname = renpy.input("당신의 이름은?", length=16)
            prtname = prtname.strip()

            if prtname in banned_names:
                narrator("적절한 이름이 아닙니다.")
                continue
            
            # refer to https://www.renpy.org/doc/html/statement_equivalents.html
            narrator("[prtname], 이 이름이 맞습니까?", interact=False)
            result = renpy.display_menu([("그렇다", "y"), ("아니다", "n")])

            if result == "y":
                break