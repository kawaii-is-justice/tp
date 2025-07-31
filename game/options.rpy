# Note: _() is for translation.
define config.name = _("다시 시작하는 봄")
define config.version = "1.0.0"

define gui.about = _p("""
===========================================

2025 가상융합서비스 개발자 경진대회 출품작

팀 "귀여움은 정의다" 에 의해 제작됨:

- 원두현    개발 담당

- 장유진    아트 담당

- 고준석    스토리 담당

===========================================
""")

# Note: Only ASCII excluding space, colon, and semicolon.
define build.name = "SpringBeginningAgain"

###############
# CHOICE MENU #
###############
define config.menu_include_disabled = True

#################
# AUDIO CONTROL #
#################
define config.main_menu_music = "audio/music/title_screen.mp3"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

## 번역 ##########################################################################
##
## 이러한 변수는 특정 이벤트가 발생할 때 사용되는 전환을 설정합니다. 각 변수는
## 전환으로 설정해야 하며, 전환을 사용하지 말아야 한다는 것을 나타내려면 None으
## 로 설정해야 합니다.

## 게임 메뉴에 진입하거나 나갑니다.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 게임 메뉴 화면 사이입니다.

define config.intra_transition = dissolve


## 게임이 로드된 후 사용되는 전환입니다.

define config.after_load_transition = None


## 게임 종료 후 주 메뉴에 진입할 때 사용됩니다.

define config.end_game_transition = None


## 게임을 시작할 때 사용되는 전환을 설정하는 변수가 없습니다. 대신, 초기 장면을
## 표시한 후 with 문을 사용하십시오.


## 창 관리 ########################################################################
##
## 이것은 대사 창이 표시됐을 때 제어합니다. 만약 "show"면, 그것은 상항 표시됩니
## 다. 만약 "hide"면, 그것은 대사가 주어질 때만 표시됩니다. 만약 "auto"면, 창은
## 장면(scene) 문 앞에 숨겨져 대화 상자가 표시되면 다시 표시됩니다.
##
## 게임이 시작된 후에는 "window show", "window hide", 그리고 "window auto" 문을
## 사용하여 변경할 수 있습니다.

define config.window = "auto"


## 대화 창을 표시하고 숨기는 데 사용되는 전환

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

###############
# PREFERENCES #
###############
default preferences.text_cps = 20   # Note: 0 = immediate
default preferences.afm_time = 15   # Note: [0,30] is a valid range.

## 세이브 디렉토리 ####################################################################
##
## 렌파이는 이 게임에 대한 저장 파일을 플랫폼 별로 배치합니다. 세이브 파일들은
## 여기에 있습니다:
##
## 윈도우즈: %APPDATA\RenPy\<config.save_directory>
##
## 매킨토시: $HOME/Library/RenPy/<config.save_directory>
##
## 리눅스: $HOME/.renpy/<config.save_directory>
##
## 이것은 일반적으로 변경해서는 안 되며, 항상 표현형식이 아닌 정확한 문자열이어
## 야 합니다.

define config.save_directory = "kawaii-1749539828"


## Icon ########################################################################
##
## 작업 표시 줄 또는 독에 표시되는 아이콘.

define config.window_icon = "gui/window_icon.png"


## 빌드 구성 #######################################################################
##
## 이 섹션은 렌파이가 프로젝트를 배포 파일로 만드는 방법을 제어합니다.

init python:

    ## 다음 함수는 파일 패턴을 사용합니다. 파일 패턴은 대/소문자를 구분하지 않으
    ## 며, /의 유무와 관계없이 기본 디렉터리의 상대 경로와 일치합니다. 여러 패턴
    ## 이 일치하면 첫 번째 패턴이 사용됩니다.
    ##
    ## 패턴 있음:
    ##
    ## / 는 디렉토리 구분 기호입니다.
    ##
    ## * 는 디렉토리 구분자를 제외한 모든 문자와 일치합니다.
    ##
    ## ** 는 디렉토리 구분자를 포함해 모든 문자와 일치합니다.
    ##
    ## 예를 들어, "*.txt" 는 기본 디렉토리의 txt 파일들과 일치하고, "game/
    ## **.ogg" 는 게임 디렉토리 또는 그 서브 디렉토리의 ogg 파일들과 일치하며,
    ## "**.psd" 는 프로젝트에서 모든 곳의 psd 파일들과 일치합니다.

    ## 파일을 None으로 분류하여 배포판으로부터 제외하십시오.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 파일을 아카이브하려면 'archive'로 분류하십시오.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 파일들의 매칭 문서 패턴은 맥앱(Mac App) 빌드에서 중복되므로 app 및 zip 파
    ## 일에 모두 나타납니다.

    build.documentation('*.html')
    build.documentation('*.txt')


## 인앱 구매를 수행하려면 Google Play 라이선스 키가 필요합니다. Google Play 개발
## 자 콘솔의 '수익 창출' > '수익 창출 설정' > '라이선스'에서 찾을 수 있습니다.

# define build.google_play_key = "..."


## itch.io 프로젝트와 연관된 사용자 이름과 프로젝트 이름이며 슬래시로 구분됩니
## 다.

# define build.itch_project = "renpytom/test-project"
