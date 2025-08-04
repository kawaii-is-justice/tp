init offset = -1

##########
# STYLES #
##########
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

##############
# SAY SCREEN #
##############
screen say(who, what):
    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
            
        text what id "what":
            # Narrator
            if who is None:
                ypos gui.dialogue.top_narrator

    if quick_menu:
        use quick_menu()

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox.yalign
    ysize gui.textbox.height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name.xpos
    xanchor gui.name.xalign
    xsize gui.namebox.width
    ypos gui.name.ypos
    ysize gui.namebox.height

    background Frame("gui/namebox.png", gui.namebox.borders, tile=gui.namebox.tile, xalign=gui.name.xalign)
    padding gui.namebox.borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name.xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue.left
    xsize gui.dialogue.width
    ypos gui.dialogue.top

    adjust_spacing False
    line_spacing gui.dialogue.linespace

##############
# QUICK MENU #
##############
# Note: `quick_menu` screen is used inside the say screen.
# It uses 3 screens: qm_hist_tooltip, qm_pref_tooltip, qm_save_tooltip.
screen quick_menu():
    imagebutton:
        action [Hide("qm_hist_tooltip"), ShowMenu('history')]
        auto "gui/quick_menu/histbtn.%s.png"
        xpos gui.quickmenu.btn.left
        ypos gui.quickmenu.histbtn.top
        hovered Show("qm_hist_tooltip")
        unhovered Hide("qm_hist_tooltip")
    
    imagebutton:
        action [Hide("qm_save_tooltip"), ShowMenu('save')]
        auto "gui/quick_menu/savebtn.%s.png"
        xpos gui.quickmenu.btn.left
        ypos gui.quickmenu.savebtn.top
        hovered Show("qm_save_tooltip")
        unhovered Hide("qm_save_tooltip")

    imagebutton:
        action [Hide("qm_pref_tooltip"), ShowMenu('preferences')]
        auto "gui/quick_menu/prefbtn.%s.png"
        xpos gui.quickmenu.btn.left
        ypos gui.quickmenu.prefbtn.top
        hovered Show("qm_pref_tooltip")
        unhovered Hide("qm_pref_tooltip")

# Note: used in the quick_menu screen
screen qm_hist_tooltip():
    frame:
        xsize gui.quickmenu.histbtntooltip.width
        ysize gui.quickmenu.histbtntooltip.height
        xpos  gui.quickmenu.histbtntooltip.left
        ypos  gui.quickmenu.histbtntooltip.top
        background "#000000dc"

    text "지난 대화":
        xpos gui.quickmenu.histbtntooltip.textleft
        ypos gui.quickmenu.histbtntooltip.texttop
        size gui.rfsiz

# Note: used in the quick_menu screen
screen qm_save_tooltip():
    frame:
        xsize gui.quickmenu.savebtntooltip.width
        ysize gui.quickmenu.savebtntooltip.height
        xpos  gui.quickmenu.savebtntooltip.left
        ypos  gui.quickmenu.savebtntooltip.top
        background "#000000dc"

    text "저장":
        xpos gui.quickmenu.savebtntooltip.textleft
        ypos gui.quickmenu.savebtntooltip.texttop
        size gui.rfsiz

# Note: used in the quick_menu screen
screen qm_pref_tooltip():
    frame:
        xsize gui.quickmenu.prefbtntooltip.width
        ysize gui.quickmenu.prefbtntooltip.height
        xpos  gui.quickmenu.prefbtntooltip.left
        ypos  gui.quickmenu.prefbtntooltip.top
        background "#000000dc"

    text "환경설정":
        xpos gui.quickmenu.prefbtntooltip.textleft
        ypos gui.quickmenu.prefbtntooltip.texttop
        size gui.rfsiz

#########
# INPUT #
#########
screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue.text_xalign
            xpos gui.dialogue.left
            xsize gui.dialogue.width
            ypos gui.dialogue.top

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue.text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue.text_xalign
    xmaximum gui.dialogue.width
    color gui.hover_color

###############
# CHOICE MENU #
###############
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 400
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

##############
# NAVIGATION #
##############
# Note: 9 textbuttons at most
screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos
        xsize gui.nav_width
        spacing gui.navigation_spacing
        
        if main_menu:
            textbutton _("처음부터"):
                action Start()
        else:
            textbutton _("지난 대화"):
                action ShowMenu("history")
            textbutton _("저장하기"):
                action ShowMenu("save")

        textbutton _("불러오기"):
            action ShowMenu("load")
        textbutton _("환경설정"):
            action ShowMenu("preferences")

        if _in_replay:
            textbutton _("리플레이 종료"):
                action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("시작 화면"):
                action MainMenu()

        textbutton _("게임 정보"):
            action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("조작 방법"):
                action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("종료하기"):
                action Quit(confirm=not main_menu)

        textbutton _("돌아가기"):
            action Return()

style navigation_button is gui_button
style navigation_button:
    properties gui.button_properties("navigation_button")
    xalign 0.5

style navigation_button_text is gui_button_text
style navigation_button_text:
    properties gui.text_properties("navigation_button")
    idle_color "#EAEAEA"
    hover_color "#069997"
    selected_color "#CC254F"

#############
# MAIN MENU #
#############
screen main_menu():
    default titlescreen = TitleScreenCDD((gui.vpw, gui.vph))

    tag menu

    add gui.ts.bg
    add Solid(gui.ts.bg_tint)
    add Frame(gui.ts.lb.top, xysize=gui.ts.lb.dim)
    add Frame(gui.ts.lb.btm, yalign=1.0, xysize=gui.ts.lb.dim)
    add titlescreen
    add gui.ts.hanl:
        zoom 2.0
        xpos gui.ts.hanl_left
        ypos gui.ts.hanl_top
    add gui.ts.nuri:
        zoom 2.0
        xpos gui.ts.nuri_left
        ypos gui.ts.nuri_top

#############
# GAME MENU #
#############
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    add gui.gm.bg

    frame:  # This is the container that holds everything
        style "game_menu_outer_frame"

        hbox:
            frame:  # This frame makes a room for the navigation screen
                style "game_menu_navigation_frame"
            
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing
                        transclude

                else:
                    transclude

    use navigation

    add gui.gm.title.im:
        xpos gui.gm.title.left
        ypos gui.gm.title.top

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background gui.gm.overlay

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos gui.nav.label.left
    ypos gui.nav.label.top
    xsize gui.nav.label.width
    ysize gui.title_text_size

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    xalign 0.5

#########
# ABOUT #
#########
screen about():
    tag menu

    use game_menu(_("게임 정보"), scroll="viewport"):
        style_prefix "about"

        vbox:
            label "[config.name!t]"
            text _("v. {color=#069997}[config.version!t]{/color}\n")

            if gui.about:
                text "[gui.about!t]\n"

            text _("{a=https://www.renpy.org/}{color=#66C1FF}Ren'Py{/color}{/a} [renpy.version_only]\n\n[renpy.license!t]")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

###############
# SAVE & LOAD #
###############
screen save():
    tag menu
    use file_slots(_("저장하기"))

screen load():
    tag menu
    use file_slots(_("불러오기"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("페이지 {}"), auto=_("자동 저장"), quick=_("빠른 저장"))

    use game_menu(title):
        fixed:
            # So that the input element can be reacted to Enter first.
            order_reverse True

            # A page title can be edited.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            # File slot grid
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot):
                            xalign 0.5
                        null:
                            height 10
                        text FileTime(slot, format=_("%Y년 %B %d일 %A %H시 %M분"), empty=_("데이터 없음")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            # Pagenation button
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("자동") action FilePage("auto")
                    if config.has_quicksave:
                        textbutton _("퀵") action FilePage("quick")
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("동기화 업로드"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("동기화 다운로드"):
                            action DownloadSync()
                            xalign 0.5

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    idle_color gui.selected_color
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

###############
# PREFERENCES #
###############
screen preferences():
    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("화면 크기")
                        textbutton _("창모드") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("대사 건너뛰기")
                    textbutton _("읽지 않은 대사") action Preference("skip", "toggle")
                    textbutton _("선택지 이후") action Preference("after choices", "toggle")
                    textbutton _("화면 전환 효과") action InvertSelected(Preference("transitions", "toggle"))

            null:
                height gui.pref_spacing * 4

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("텍스트 재생 속도")
                    null:
                        height gui.slider_span
                    bar value Preference("text speed")

                    label _("자동 진행 시간")
                    null:
                        height gui.slider_span
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("배경음 음량")
                        null:
                            height gui.slider_span
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("효과음 음량")
                        null:
                            height gui.slider_span
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("음성 음량")
                        null:
                            height gui.slider_span
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null:
                            height gui.pref_spacing
                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

###########
# HISTORY #
###########
screen history():
    tag menu
    predict False

    use game_menu(_("지난 대화"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):
        style_prefix "history"

        for h in _history_list:
            window:
                # if history_height is None
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        # Reflects the color of the speaking character.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("지난 대화가 없습니다.")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True
    ysize gui.vph - 180 - 45 - 15
    # 180 = gm.outerframe.pad.top
    # 45 = gm.outerframe.pad.btm
    # 15 = gm.contentframe.margin.top

style history_label_text:
    xalign 0.5
    yalign 0.5
    color "#069997"

########
# HELP #
########
screen help():
    tag menu
    default device = "keyboard"

    use game_menu(_("조작 방법"), scroll="viewport"):
        style_prefix "help"

        vbox:
            spacing 23
            hbox:
                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("Enter")
        text _("(1) 다음 대사로 진행하기\n(2) UI 선택하기 (선택지 포함)")

    hbox:
        label _("Space")
        text _("다음 대사로 진행하기\n(단, 선택지는 선택되지 않음)")

    hbox:
        label _("화살표 키")
        text _("UI 사이에서 이동하기")

    hbox:
        label _("Esc")
        text _("게임 메뉴 열기")

    hbox:
        label _("Ctrl")
        text _("누르고 있는 동안 대사 건너뛰기")

    hbox:
        label _("Tab")
        text _("대사 건너뛰기 켜기 / 끄기")

    hbox:
        label _("Page Up")
        text _("이전 대사로 돌아가기")

    hbox:
        label _("Page Down")
        text _("이후 대사로 나아가기")

    hbox:
        label "H"
        text _("UI 숨기기")

    hbox:
        label "S"
        text _("스크린샷 저장하기")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}{color=#66C1FF}대사 읽어주기 기능{/color}{/a} 토글.")

    hbox:
        label "Shift + A"
        text _("접근성 메뉴 열기")

screen mouse_help():
    hbox:
        label _("좌클릭")
        text _("(1) 다음 대사로 진행하기\n(2) UI 선택하기")

    hbox:
        label _("휠버튼")
        text _("UI 숨기기")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 열기")

    hbox:
        label _("휠 위로")
        text _("이전 대사로 돌아가기")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 나아가기")

screen gamepad_help():
    hbox:
        label _("오른쪽 트리거 (RT)\nA 버튼\n아래 버튼")
        text _("(1) 다음 대사로 진행하기\n(2) UI 선택하기")

    hbox:
        label _("왼쪽 트리거\n왼쪽 어깨")
        text _("이전 대사로 돌아가기")

    hbox:
        label _("오른쪽 범퍼 (RB)")
        text _("이후 대사로 나아가기")

    hbox:
        label _("D-Pad\n아날로그 스틱")
        text _("UI 사이에서 이동하기")

    hbox:
        label _("Start\nGuide\nB 버튼\nRight Button")
        text _("게임 메뉴 열기")

    hbox:
        label _("Y 버튼\n위 버튼")
        text _("UI 숨기기")

    textbutton _("게임패드 조정하기") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

###########
# CONFIRM #
###########
screen confirm(message, yes_action, no_action):
    style_prefix "confirm"
    modal True
    zorder 200

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("예")    action yes_action
                textbutton _("아니오") action no_action

    # It is as same as no_action that an escape press or right mouse click.
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")

##################
# SKIP INDICATOR #
##################
screen skip_indicator():
    style_prefix "skip"
    zorder 100

    frame:
        hbox:
            spacing 0

            text _("대사 건너뛰는 중")
            null:
                width 12
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha 0.5
    pause delay
    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    xpos gui.skip_xpos
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font gui.deffont

#######
# CTC #
#######
style ctc_text:
    font  gui.deffont
    color gui.idle_color
    size  gui.rfsiz

define ctc.usual = Text("▸", style="ctc_text")
define ctc.pause = ctc.usual
define ctc.timedpause = ctc.usual

transform ctc.anim.usual:
    alpha 0.25
    block:
        easein  0.75 alpha 1.0
        pause 0.1
        easeout 0.75 alpha 0.25
        pause 0.1
        repeat

transform ctc.anim.pause:
    ctc.anim.usual

transform ctc.anim.timedpause:
    alpha 0.5

image ctc usual = At(ctc.usual, ctc.anim.usual)
image ctc pause = At(ctc.pause, ctc.anim.pause)
image ctc timedpause = At(ctc.timedpause, ctc.anim.timedpause)

##########
# NOTIFY #
##########
screen notify(message):
    style_prefix "notify"
    zorder 100

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    xpos gui.notify_xpos
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## NVL 스크린 #####################################################################
##
## NVL모드 대사와 선택지를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## vpgrid나 vbox 내에 대사를 출력합니다.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 주어진 경우 메뉴를 표시합니다. config.narrator_menu가 True로 설정된
        ## 경우 메뉴가 잘못 표시될 수 있습니다.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 동시에 출력될 수 있는 NVL 대사의 최대치를 조정합니다.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## 말풍선 화면은 말풍선을 사용할 때 플레이어에게 대화를 표시하는 데 사용됩니다.
## 말풍선 화면은 말풍선 화면과 동일한 매개변수를 사용하며, "what" 아이디로 표시
## 가능 항목을 생성해야 하며, "namebox", "who", "window" 아이디로 표시 가능 항목
## 을 생성할 수 있습니다.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## 모바일 버전
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## 마우스가 없고 화면이 작을 가능성이 높으므로, 퀵메뉴 버튼의 크기를 키우고 가짓
## 수를 줄입니다.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
