label interlude:
    $ save_name = "interlude"

    scene bg black screen
    with Fade(2.0, 2.0, 2.0)

    play music general1 fadein 1.0

    window show

    "지금부터 이야기가 잠시 두 갈래로 분기됩니다."

    window hide dissolve
    pause 0.5

    show hanl_char with Dissolve(1.0):
        ilight
        truecenter
        xoffset -200
        yoffset  80
        zoom 1.5
    pause 0.2

    show nuri_char with Dissolve(1.0):
        ilight
        truecenter
        xoffset  200
        yoffset  80
        zoom 1.5
    pause 1.0

    jump interlude_menu

label interlude_menu:
    # window show
    menu:
        "어느 쪽을 먼저 진행합니까?"
        "하늘이의 이야기":
            jump interlude_prompt_hanl_route
        "누리의 이야기":
            jump interlude_prompt_nuri_route

label interlude_prompt_hanl_route:
    show hanl_char anim
    show nuri_char at shade
    menu:
        "하늘이의 이야기로 진입합니까?"
        "그렇다":
            stop music fadeout 1.0
            window hide dissolve
            hide nuri_char with dissolve
            pause 0.5
            show hanl_char anim:
                linear 0.75 xoffset 0
            pause 1.5
            show hanl_char
            pause 1.0
            jump interlude_hanl

        "아니다":
            show hanl_char
            show nuri_char at light
            jump interlude_menu

label interlude_prompt_nuri_route:
    show nuri_char anim
    show hanl_char at shade
    menu:
        "누리의 이야기로 진입합니까?"
        "그렇다":
            stop music fadeout 1.0
            window hide dissolve
            hide hanl_char with dissolve
            pause 0.5
            show nuri_char anim:
                linear 0.75 xoffset 0
            pause 1.5
            show nuri_char
            pause 1.0
            jump interlude_nuri
        
        "아니다":
            show nuri_char
            show hanl_char at light
            jump interlude_menu

label interlude_hanl:
    $ save_name = "각자의 이야기: 하늘"
    
    scene bg school library afternoon
    with Dissolve(1.0)
    pause 0.3

    play music event fadein 1.0

    show hanl at center, doup with dissolve
    show hanl say
    window show

    h "제 이름은 {color=#99D9EA}하늘{/color}. █████학교의 ■학년 ■반 반장을 맡고 있습니다."
    h "처음엔... 제가 이상해진 줄 알았습니다. \n뭔가 어딘가... 맞지 않는 느낌."
    h "지금, 이 세상은, {p}어딘가 잘못되어 있습니다."
    h "말도 안 되는 소리처럼 들릴지도 모르겠지만—— {p}이 세계는, 반복되고 있습니다."
    h "철학에서 말하는 윤회도 아니고, \nSF에서 다루는 타임루프도 아닙니다."
    h "그냥{cps=6}...{/cps} {p}세계가 자신을 고치려고 하는 것 같달까요."
    h "그렇게 생각하게 된 건... {p}전학생 때문입니다."
    h "처음엔 단순한 기시감이었습니다. \n했던 말을 또 하고 있다는 느낌. \n전학생도... 뭔가 눈치챈 것 같더군요."
    h "게다가—— {p}도서관에서 발급하려던 학생증을, \n전학생은 이미 가지고 있었습니다."
    h "그 순간... \n전학생은 엄청난 고통을 호소하며 쓰러지고 \n저 또한 극심한 두통으로 자리에 주저앉아버렸습니다."
    h "그리고... 방과후에 도서관을 정리하던 중, \n책장에서 노트 한 권을 발견했습니다. \n누군가 놓고 간 건 줄 알았는데..."
    h "그 안엔 낯익은 글씨로, \n낯선 내용이 빼곡히 적혀 있었습니다."
    "전학생은 오늘 처음 온 게 아니다. {p}누리는 항상 그 아이에게 호의를 보인다. {p}전학생에게 큰 사고가 난 적이 있었다."
    h "제 글씨였습니다. \n처음엔 누군가의 장난인 줄 알았습니다."
    h "하지만— 너무 많은 것들이 들어맞았고, \n무엇보다 틀림없이 제 필체였습니다."
    h "이건... 반복을 인지한 \n또 다른 '저'의 기록이라고밖에 설명할 수 없었습니다."
    h "그래서 저는... \n다음에도 이 노트를 \n반드시 찾을 수 있게 잘 숨겨두었습니다."
    h "어쩌면... {p}이미 수 없이 놓쳤을지도 모르겠네요." 

    stop music fadeout 0.5
    play sound dish_break

    show hanl embarrassed

    h "...?!" with hpunch
    h "이 소리... \n{cps=6}...{/cps}푸른색 유령 같은 게 튀어나오진 않겠죠?"

    play music event fadein 1.0

    show hanl

    h "옛날 게임에 도서관에 그런 괴물이 등장했다던데요."
    h "푸른 얼굴에, 저택을 배회하는 유령. {p}이상하게도 기억에 남아 있네요."
    h "하지만 저는 무섭지 않습니다."
    h "이게 유령이 아니라면... {p}세상이 저를 시험하고 있는 걸지도 모르죠."
    h "...일단 도서관 정리를 마저 하도록 하죠."

    show solid gray tp with dissolve

    "{space=325}{color=#7FFF00}<미니게임: 도서관 정리!>{/color} \n{fast}규칙: 모든 땅을 밟아야 한다. 화살표 키로 이동할 수 있다."
    "{space=325}{color=#7FFF00}<미니게임: 도서관 정리!>{/color} \n{fast}이 때, 빵 봉지는 1번, 빵은 2번 밟아야 한다."

    window hide dissolve
    hide solid gray tp with dissolve
    pause 0.5
    hide hanl with dissolve
    pause 0.5
    
    # Proceeds to the tilestep minigame
    $ disable_save()
    
    call screen minigame_tilestep(1)
    $ tilestep_res = _return['res']
    
    show hanl frown at center, doup with dissolve
    window show

    h "흠{cps=5}... {/cps}이번 청소는 "

    if tilestep_res == "perfect":
        show hanl smile at doup
        extend "깔끔하게 완료됐습니다!"
        $ hanllove += 1
    elif tilestep_res == "not bad":
        show hanl at doup
        extend "그럭저럭 적당한 것 같네요."
    elif tilestep_res == "bad":
        show hanl frown at doup
        extend "썩 잘하지 못한 것 같습니다..."
        $ hanllove -= 1

    $ enable_save()

    show hanl say
    window show

    h "...후. \n어느 정도 정리가 된 것 같네요."
    h "오늘 있었던 일도... \n노트에 잘 기록했고요."
    h "노트를 보면 볼수록, \n전학생이 이 반복의 '열쇠'라는 생각이 강해집니다."
    h "그 아이가 어떤 선택을 하게 될지... \n계속 생각하게 되네요."
    h "내일도... \n그 아이에게 말을 걸게 될까요."

    show hanl
    window hide dissolve
    pause 0.25

    hide hanl with dissolve

    stop music fadeout 2.0
    pause 0.5

    $ hanl_done = True

    if nuri_done:
        jump loop_4
    else:
        jump transition_hanl_to_nuri

label transition_hanl_to_nuri:
    $ save_name = "interlude"

    scene bg black screen
    with Fade(1.0, 1.0, 1.0)

    window show

    "한편, 누리는..."
    
    window hide dissolve
    pause 0.5

    jump interlude_nuri

label interlude_nuri:
    $ save_name = "각자의 이야기: 누리"
    
    scene bg home kitchen
    with Dissolve(1.0)
    pause 0.3

    play music event fadein 1.0 volume 0.5
    play environment rain fadein 1.0

    show nuri at center, doup with dissolve
    show nuri say
    window show

    n "흠~ 또 비가 오네?"
    n "요즘 왜 이렇게 자주 비가 오는거야?"
    n "비 오는 날엔... \n초콜릿이 땡기는걸!"
    n "아, 맞다! \n내 소개를 아직 안 했구나."
    n "내 이름은 누리! █████학교 ■학년 ■반!"
    n "참고로 우리 반의 반장은 하늘이야."
    n "원래 조용한 애긴 했는데... \n요즘엔 좀 이상한 것 같아."
    n "{cps=6}...{/cps}뭔가 날 피하는 것 같기도 하고?"
    n "내가 뭘 잘못했나?"
    n "그래서 내일은 쿠키라도 만들어서 가져다주려고~"
    n "전에 하늘이에게 초콜릿 쿠키를 만들어 준 적이 있었는데, \n정말 좋아하더라고~"
    n "하늘이가 원체 겉으로 티를 안 내는지라 남들은 모르겠지만, \n분명 내 쿠키를 좋아하는 눈치였어!"
    n "그리고... \n오늘 우리 반에 전학생이 왔는데—"
    n "왠지 모르게 알던 사이인 것처럼 말 걸 수 있었어!"
    n  "그리고 분명 처음 본 걸텐데... \n왠지 모르게 두근두근했달까..."
    n "{cps=6}...{/cps}이게 그냥 전학생이라서 그런걸까?"
    n "아니면{cps=6}......{/cps}"

    show nuri smile blush

    n "이게... {p}한눈에 반해버렸다는 거?!"
    n "에이! 모르겠다! \n일단 쿠키부터 만들자!"

    show nuri say

    n "주방이 어질러져서, 재료도 막 흩어져있고... {p}전에 태운 쿠키 잔해도 있고..."
    n "조심하자... \n뭐가 튀어나올지 몰라..."

    show solid gray tp with dissolve

    "{space=350}{color=#7FFF00}<미니게임: 쿠키 수집!>{/color} \n{fast}규칙: 벽에 부딪히지 않도록 캐릭터의 방향을 변경하면서 갈색 쿠키를 모은다. 화살표 키로 이동할 수 있다."
    "{space=350}{color=#7FFF00}<미니게임: 쿠키 수집!>{/color} \n{fast}검은색 쿠키에 닿으면 모은 쿠키를 하나 잃어버린다."
    "{space=350}{color=#7FFF00}<미니게임: 쿠키 수집!>{/color} \n{fast}지금 전진하고 있는 방향의 반대로는 변경할 수 없다."

    hide nuri with dissolve

    # Proceeds to the snake minigame
    window hide dissolve
    $ disable_save()

    call screen minigame_snake()
    $ snake_res = _return   # self.item_count
    
    show nuri frown at center, doup with dissolve
    window show

    n "어디보자~{cps=5}... {/cps}"

    if snake_res >= 10:
        show nuri smile at doup
        extend "이 정도면 잘 만들었는걸?"
        $ nurilove += 1

    elif snake_res >= 5:
        show nuri say at doup
        extend "선물하지 못할 정도는 아니라서 다행이네."

    elif snake_res >= 0:
        show nuri disappointed at doup
        extend "내 요리 실력이 이렇게 절망적이라니..."
        $ nurilove -= 1
    
    $ enable_save()

    show nuri smile
    window show

    n "아무튼 완성!"
    n "초콜릿이 녹지 않게 냉장고에 넣어놔야겠다~"
    n "아차... {p}냉장고 열기 전에 노크해야 되는데!"

    show nuri smile

    n  "왜냐하면— {p}샐러드가 드레스를 입고 있을지도 모르잖아~? 히히~"
    n "그러니까{cps=6}...{/cps} \n드레싱{cps=6}...{/cps} dressing이 옷을 갈아입는다는 뜻도 있어서{cps=6}...{/cps}"
    
    show nuri

    n "아무튼!"
    n "좋아! \n내일은 하늘이한테 쿠키를 주고{cps=6}...{/cps}"
    n "그리고— \n그 애랑도 꼭 말해봐야지."
    n "내일은{cps=6}...{/cps} \n조금 더 가까워질 수 있을까?"
    
    show nuri
    window hide dissolve
    pause 0.25

    hide nuri with dissolve

    stop music fadeout 2.0
    stop environment fadeout 2.0
    pause 0.5

    $ nuri_done = True

    if hanl_done:
        jump loop_4
    else:
        jump transition_nuri_to_hanl

label transition_nuri_to_hanl:
    $ save_name = "interlude"

    scene bg black screen
    with Fade(1.0, 1.0, 1.0)

    window show

    "한편, 하늘이는..."

    window hide dissolve
    pause 0.5

    jump interlude_hanl