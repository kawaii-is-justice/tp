init offset = -2

init python:
    gui.vpw = 1920  # viewport width
    gui.vph = 1080  # viewport height
    gui.init(gui.vpw, gui.vph)

define config.check_conflicting_properties = True

#########
# COLOR #
#########
define gui.accent_color = "#CC254F"
define gui.idle_color = "#EAEAEA"
define gui.idle_small_color = "#FFFFFF"
define gui.hover_color = "#069997"
define gui.selected_color = "#7FFF00"
define gui.insensitive_color = "#8B8B8B"

define gui.text_color = "#EAEAEA"
define gui.interface_text_color = gui.text_color

define gui.muted_color = '#66c1ff'
define gui.hover_muted_color = '#99d6ff'

######################
# FONT AND FONT SIZE #
######################
define gui.rfsiz = 40   # Root font size
define gui.deffont = "fonts/Galmuri9.ttf"   # Default font

define gui.text_font = gui.deffont
define gui.name_text_font = gui.deffont
define gui.interface_text_font = gui.deffont

define gui.text_size = gui.rfsiz
define gui.name_text_size = gui.rfsiz
define gui.interface_text_size = gui.rfsiz
define gui.label_text_size = gui.rfsiz
define gui.notify_text_size = gui.rfsiz
define gui.title_text_size = int(gui.rfsiz * 1.25)

################
# TITLE SCREEN #
################
define gui.ts.bg = Image("gui/title_screen/background.jpg")
define gui.ts.bg_tint = "#FFFFFF7F"
define gui.ts.lb.top = "gui/title_screen/letbox.top.png"
define gui.ts.lb.btm = "gui/title_screen/letbox.btm.png"
define gui.ts.lb.dim = (1920,50)
define gui.ts.hanl = Image("gui/title_screen/hanl.png")
define gui.ts.hanl_left = 670
define gui.ts.hanl_top = 390

##############
# GAME MENU  #
# NAVIGATION #
##############
define gui.nav_lmargin = 12
define gui.nav_tmargin = gui.nav_lmargin
define gui.nav_lpad = 40
define gui.nav_rpad = gui.nav_lpad 
define gui.nav_num_elem = 9
define gui.navigation_spacing = 8
define gui.nav_width = 320
define gui.nav_height = gui.rfsiz * (gui.nav_num_elem + gui.navigation_spacing) - gui.navigation_spacing
define gui.nav_fullwidth = gui.nav_lpad + gui.nav_width + gui.nav_rpad
define gui.nav.label.width = int(gui.title_text_size * 6.5)  # 리플레이 종료 = 6.5 characters long
define gui.nav.label.left = gui.nav_lmargin + (gui.nav_fullwidth - gui.nav.label.width) // 2
define gui.nav.label.top = gui.nav_tmargin + 32

define gui.gm.bg = "gui/game_menu/base.png"
define gui.gm.title.im = "gui/game_menu/logo.png"
define gui.gm.overlay = "gui/game_menu/overlay.png"
define gui.gm.title.w = 1000 // 4
define gui.gm.title.h = 820 // 4
define gui.gm.title.left = gui.nav_tmargin + (gui.nav_fullwidth - gui.gm.title.w) // 2
define gui.gm.title.top = gui.gm.title.left

define gui.navigation_xpos = gui.nav_lmargin + gui.nav_lpad
define gui.navigation_ypos = gui.gm.title.top + gui.gm.title.h + 75

##############################
# TEXTBOX, NAMEBOX, DIALOGUE #
##############################
init python:
    config.character_id_prefixes.append('namebox')

# Note: textbox.png is (1920, 270)px long and
# it has a left and right margin with the same length.
define gui.textbox.actualwidth = 1240
define gui.textbox.actualheight = 232
define gui.textbox.marginleft = int((gui.vpw - gui.textbox.actualwidth) / 2)  # 340px
define gui.textbox.span = gui.textbox.marginleft + gui.textbox.actualwidth
define gui.textbox.paddingleft = 60
define gui.textbox.paddingright = gui.textbox.paddingleft
define gui.textbox.paddingtop = 24
define gui.textbox.height = 270
define gui.textbox.ypos = gui.vph - gui.textbox.height
define gui.textbox.yalign = 1.0

# Note: left, top = initial x, y of the first dialogue line
# Note: the namebox is above the first dialogue line.
define gui.dialogue.linespace = 4
define gui.dialogue.left = gui.textbox.marginleft + gui.textbox.paddingleft  # 400px
define gui.dialogue.top = gui.textbox.paddingtop + gui.text_size + gui.dialogue.linespace # 68px
define gui.dialogue.width = gui.textbox.actualwidth - (gui.textbox.paddingleft + gui.textbox.paddingright) # 1120px
define gui.dialogue.text_xalign = 0.0
define gui.dialogue.top_narrator = gui.dialogue.top - gui.rfsiz

define gui.namebox.iconheight = 24  # size of `>` icon
define gui.namebox.width = gui.dialogue.width - gui.namebox.iconheight
define gui.namebox.height = gui.text_size
define gui.namebox.borders = Borders(gui.namebox.iconheight,0,0,0)
define gui.namebox.tile = False

define gui.name.xpos = gui.dialogue.left
define gui.name.ypos = gui.textbox.paddingtop
define gui.name.xalign = 0.0

##############
# QUICK MENU #
##############
# `quick_menu` variable controls the show/hide of this quick menu.
default quick_menu = True

define gui.quickmenu.margin = 20   # span between quick menu elements

define gui.quickmenu.btn.width = 50
define gui.quickmenu.btn.height = gui.quickmenu.btn.width
define gui.quickmenu.btn.left = gui.textbox.span + gui.quickmenu.margin

define gui.quickmenu.span = gui.quickmenu.btn.height + gui.quickmenu.margin
define gui.quickmenu.padding = int((gui.textbox.actualheight - (gui.quickmenu.btn.height * 3 + gui.quickmenu.margin * 2)) / 2)

define gui.quickmenu.histbtn.left = gui.quickmenu.btn.left
define gui.quickmenu.histbtn.top = gui.textbox.ypos + gui.quickmenu.padding

define gui.quickmenu.savebtn.left = gui.quickmenu.btn.left
define gui.quickmenu.savebtn.top = gui.quickmenu.histbtn.top + gui.quickmenu.span

define gui.quickmenu.prefbtn.left = gui.quickmenu.btn.left
define gui.quickmenu.prefbtn.top = gui.quickmenu.savebtn.top + gui.quickmenu.span

define gui.quickmenu.histbtntooltip.width = 183
define gui.quickmenu.histbtntooltip.height = gui.quickmenu.btn.height
define gui.quickmenu.histbtntooltip.left = gui.quickmenu.histbtn.left + gui.quickmenu.btn.width
define gui.quickmenu.histbtntooltip.top = gui.quickmenu.histbtn.top
define gui.quickmenu.histbtntooltip.textleft = gui.quickmenu.histbtntooltip.left + 4
define gui.quickmenu.histbtntooltip.texttop = gui.quickmenu.histbtntooltip.top + 3

define gui.quickmenu.savebtntooltip.width = 87
define gui.quickmenu.savebtntooltip.height = gui.quickmenu.btn.height
define gui.quickmenu.savebtntooltip.left = gui.quickmenu.savebtn.left + gui.quickmenu.btn.width
define gui.quickmenu.savebtntooltip.top = gui.quickmenu.histbtntooltip.top + gui.quickmenu.span
define gui.quickmenu.savebtntooltip.textleft = gui.quickmenu.savebtntooltip.left + 4
define gui.quickmenu.savebtntooltip.texttop = gui.quickmenu.savebtntooltip.top + 3

define gui.quickmenu.prefbtntooltip.width = 163
define gui.quickmenu.prefbtntooltip.height = gui.quickmenu.btn.height
define gui.quickmenu.prefbtntooltip.left = gui.quickmenu.prefbtn.left + gui.quickmenu.btn.width
define gui.quickmenu.prefbtntooltip.top = gui.quickmenu.savebtntooltip.top + gui.quickmenu.span
define gui.quickmenu.prefbtntooltip.textleft = gui.quickmenu.prefbtntooltip.left + 4
define gui.quickmenu.prefbtntooltip.texttop = gui.quickmenu.prefbtntooltip.top + 3

###############
# CHOICE MENU #
###############
define gui.choice_button_width = 1194
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(20, 20, 20, 20, \
                                            0, -4, 0, -4)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = gui.idle_color
define gui.choice_button_text_hover_color = "#000000"
define gui.choice_button_text_insensitive_color = gui.insensitive_color

####################
# SAVE & LOAD SLOT #
####################
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = gui.rfsiz // 2
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 384
define config.thumbnail_height = 216

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

##################
# SKIP INDICATOR #
##################
define gui.skip_frame_borders = Borders(8, 8, 8, 8, \
                                        12, 8, 8, 8)
define gui.skip_height = 64
define gui.skip_xpos = gui.textbox.marginleft
define gui.skip_ypos = gui.textbox.ypos - gui.skip_height - gui.skip_frame_borders.pad_bottom - 16

##########
# NOTIFY #
##########
define gui.notify_frame_borders = Borders(8, 8, 8, 8, \
                                        16, 12, 8, 8)
define gui.notify_xpos = 32
define gui.notify_ypos = 32

###############
# CHOICE MENU #
###############
define gui.choice_spacing = 16

###########
# CONFIRM #
###########
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.confirm_button_text_xalign = 0.5

#########
# FRAME #
#########
define gui.frame_tile = False
define gui.frame_borders = Borders(6, 6, 6, 6)

###########
# HISTORY #
###########
define config.history_length = 250
define gui.history_height = gui.rfsiz * 4 + 20
define gui.history_spacing = 0

define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 255
define gui.history_text_ypos = 0
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

###############
# PREFERENCES #
###############
define gui.pref_spacing = 15
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 15
define gui.slider_span = 8

###########
# BUTTONS #
###########
# Note: None = auto-calculated
define gui.button_width = None
define gui.button_height = None

define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(40, 6, 6, 6)
define gui.check_button_borders = Borders(40, 6, 6, 6)
define gui.page_button_borders = Borders(15, 6, 15, 6)

##########################
# BAR, SCROLLBAR, SLIDER #
##########################
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

define gui.unscrollable = "hide"    # None to show

## NVL-모드 ######################################################################
##
## NVL-모드 화면은 NVL-모드 캐릭터들에 의한 대화를 화면에 표시합니다.

## NVL-모드 배경 창에서 배경의 테두리입니다.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## 렌파이가 표시할 NVL-mode 항목의 최대 수입니다. 설정보다 많은 항목이 표시되면
## 가장 오래된 항목이 제거됩니다.
define gui.nvl_list_length = 6

## NVL-모드 항목의 높이입니다. 이것을 None으로 설정하면 항목들은 동적으로 높이를
## 조정합니다.
define gui.nvl_height = 173

## gui.nvl_height 값이 None일 때 NVL-모드 항목들, 그리고 NVL-모드 항목들과 NVL-
## 모드 메뉴간의 간의 간격입니다.
define gui.nvl_spacing = 15

## 말하는 캐릭터의 이름을 나타내는 레이블의 위치, 너비, 그리고 정렬입니다.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## 대사 글자의 위치, 너비, 그리고 정렬입니다.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## nvl_thought 글자의 위치, 너비, 정렬(nvl_narrator 캐릭터에 의해 표시되는 글자)
## 입니다.
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## NVL 메뉴 버튼의 위치입니다.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## 현지화 #########################################################################

## 줄 바꿈이 허용되는 위치를 제어합니다. 기본값은 대부분의 언어에 적
## 합합니다. 사용 가능한 값 목록은 https://www.renpy.org/doc/html/
## style_properties.html#style-property-language 에서 찾을 수 있습니다.

define gui.language = "unicode"


################################################################################
## 모바일 기기
################################################################################

init python:

    ## 이것은 휴대전화와 태블릿에서 쉽게 터치할 수 있도록 빠른(Quick) 버튼들의
    ## 크기를 크게 합니다.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## 이것은 휴대전화에서 다양한 GUI 요소들의 크기와 간격을 쉽게 보일 수 있도록
    ## 변경합니다.
    @gui.variant
    def small():

        ## 글자 크기들.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## 텍스트박스의 위치를 조정합니다.
        gui.textbox.height = 360
        gui.name.xpos = 120
        gui.dialogue.left = 135
        gui.dialogue.width = 1650

        ## 다양한 사물의 크기와 간격을 변경합니다.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## 파일 버튼 레이아웃.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-모드.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
