label loop_1:

    play music general1 fadein 1.0

    $ save_name = "익숙함의 틈"

    scene bg school classroom morning
    with Fade(2.0, 2.0, 1.0)

    p "여긴... 교실인가? {p}잠깐 정신을 잃었었나..."
    p "어쩌다 전학을 오게 된 건지... {p}기억은 잘 나지 않지만..."

    "누리가 활짝 웃으며 오른손을 크게 들고 내게 인사한다."

    show nuri smile at center, doup
    with dissolve

    n "전학생~ 전학생이구나~"
    n "나는 {color=#FFAEC9}누리{/color}야. {p}전학생의 이름은{cps=7}... {/cps}{cps=5}{color=#AAAAAA}[prtname]{/color} {/cps}맞지? \n앞으로 잘 부탁해!"

    show nuri at ilight  # Without this, the following shade
    show nuri at shade   # animation would not work properly.

    "누리는 옆자리에 앉아, 나를 신기하다는 듯 빤히 쳐다봤다. \n나는 그런 누리를 못 본 척했다."

    hide nuri
    with dissolve

    "이후, 정신없는 자기소개 시간과 수업 시간이 지나가고 점심시간이 왔다."
    "선생님들이나 반 친구들이 나를 신기하게 쳐다보긴 했지만, \n그럭저럭 잘 넘긴 듯하다..."
    "이 학교는 점심 급식이 매우 맛있고, \n메뉴도 선택 가능하다니 기대된다."

    scene bg school cafeteria
    with fade

    show nuri smile at center, doup
    with dissolve

    n "{color=#AAAAAA}[prtname]{/color}이는 {color=#FFAEC9}[loop_0_lunch_menu]{/color} 좋아하지? \n같이 그거 먹자! \n참고로 내일 급식 메뉴는 뭐랑 뭐고... 모레 급식 메뉴는..."

    "이러다 올해 메뉴를 전부 읊겠어... \n빨리 먹으러 가자."
    "그런데, 누리가 내가 좋아하는 걸 어떻게 알고 있는 거지? {p}뭐, 내 시선이 그쪽에 쏠린 걸 보기라도 했나보지."
    "첫 날부터 밥 같이 먹을 사람이 생기다니... 참 다행이다."

    scene bg school hallway
    with fade

    "점심시간, \n학교를 둘러보려고 혼자서 정처 없이 돌아다니고 있었다. {p}누리가 따라오겠다는데, 겨우 떼어놓고 왔다."
    "그런데 학교의 시설이 어째선가 낯설지 않다..."
    "그러던 와중, \n창가 쪽에 조용하게 서 있는 여학생의 뒷모습이 보였다."

    show hanl say at center, doup
    with dissolve

    stranger "{cps=10}...전학생.{/cps}"

    "나는 깜짝 놀라 고개를 돌렸다."

    stranger "뭔가 이상하다고 느끼고 있지 않나요? {p}궁금하시다면, 방과 후에 도서관으로 와보세요."
    stranger "그럼 이만..."

    "...누구지? 같은 반이었나? \n처음 보는 얼굴이었는데..."
    "그런데... 어디선가 들어본 적 있는 목소리다."

    scene bg school library afternoon
    with fade

    show hanl say at center, doup
    with dissolve

    stranger "와줘서 고마워요."
    h "전 {color=#99D9EA}하늘{/color}이라고 합니다."
    h "제가 당신을 부른 건{cps=5}...{/cps} \n당신은 여기 있을 사람이 아닙니다."
    h "사실 당신은{cps=5}...{/cps}" with hpunch
    
    show solid white at flash(1)
    pause 0.5

    h "{cps=8}당신은 이곳을 테스트—{/cps}{w=1.0}{nw}" with vpunch

    show solid white at flash(2)
    pause 0.5

    stop music fadeout 0.5

    "{color=#FF0000}허용되지 않은 정보 접근 감지.{w=0.5} \n세션 강제 초기화 중{cps=3}...{/cps}{w=1.0}{nw}{/color}"

    show solid white at white_fadein
    pause 2.0

    jump loop_2

label loop_2:
    scene bg school classroom morning
    with Fade(2.0, 2.0, 1.0)

    play music general1 fadein 1.0

    "여긴{cps=5}... {/cps}교실인가? \n잠깐 정신을 잃었었나{cps=5}...{/cps}"
    "그런데 내가 어쩌다 전학을 오게 된 건지{cps=5}...{/cps}"
    "{cps=5}......{/cps} \n어디선가 익숙한 목소리가 들려와 고개를 돌렸다."
    "누리가 활짝 웃으며 오른손을 크게 들고 내게 인사를 한다."

    show nuri smile at center, doup
    with dissolve

    n "{cps=8}전학생~ 전학생이구나~ \n나는 {color=#FFAEC9}누리{/color}야.{/cps}"
    n "{cps=8}전학생의 이름은―― \n{color=#AAAAAA}[prtname]{/color}...{/cps}"

    menu:
        "누리가 나를 빤히 쳐다보고 있다."

        "(누리와 눈싸움을 한다.)":
            show nuri shy
            with dissolve
            "누리와의 눈싸움에서 이겼다."
            "누리는 고개를 돌려 푹 숙이고는 아무 말이 없다. \n조금 부끄러워하는 것 같기도 하다."
        "(왜 그러냐고 묻는다.)":
            p "왜? 무슨 일 있어?"
            n "아무것도 아니야... \n그냥 네가 어딘가 좀 익숙하게 느껴져서 말이야..."
    $ nurilove += 1

    show nuri at chls, shade
    with move

    show hanl at chrs
    with moveinright

    "그러던 중, 단정한 차림의 여자애가 내 옆을 지나갔다. \n이 친구가 반장인 하늘이었나...?"
    "하늘이가 나를 쳐다보는 눈빛이 어딘가, \n안타까운 동물을 보는 듯한 느낌이다."

    menu:
        "하늘이의 시선을 어떻게 받아들여야 할까?"

        "...무슨 일 있어?":
            show hanl at doup
            h "아무것도 아닙니다. 그냥, 전학생은 처음이라서요. \n괜찮으시다면 수업 끝나고 잠깐 도서관에 들러주세요."
        "(침묵한다)":
            show hanl at doup
            h "전학생이라 처리해야 할 일이 있으니, \n수업 끝나고 잠깐 도서관에 들러주세요."

    $ renpy.hide_screen("say")
    hide hanl
    with moveoutright
    pause 0.5

    scene bg school cafeteria
    with fade

    show nuri smile at center, doup
    with dissolve

    n "오늘 급식은 오므라이스와 카레라이스야. \n{color=#AAAAAA}[prtname]{/color}, 너는 {color=#FFAEC9}[loop_0_lunch_menu]{/color} 좋아하지? \n마침 나도 그거 좋아하거든! 같이 먹자~"

    if loop_0_lunch_menu == "카레라이스":
        $ loop_0_lunch_menu_not_selected = "오므라이스"
    else:
        $ loop_0_lunch_menu_not_selected = "카레라이스"

    menu:
        "누리와 함께 {color=#FFAEC9}[loop_0_lunch_menu]{/color}를 먹는다.":
            "누리와 함께 즐거운 점심을 먹었다."
            $ nurilove += 1
        "{color=#FFAEC9}[loop_0_lunch_menu_not_selected]{/color}를 더 좋아한다고 말한다.":
            show nuri disappointed
            with dissolve
            n "그랬구나... 알겠어."
            "누리와 함께 점심을 먹었다."
            $ nurilove -= 1
    
    scene bg school classroom afternoon
    with fade

    "오후 수업 도중, \n옆자리인 누리에게서 쪽지가 슬그머니 넘어왔다."

    show nuri smile at center, ishade
    with dissolve

    # TODO: use a paper image and place text on it, rather than
    # use this normal way to show conversations

    # Possible branches:
    # house + company => lib with nuri => cafe
    # house + no comp. => lib w/o nuri => home
    # lib + company => lib with nuri => home
    # lib + no comp. => lib w/o nuri => home

    show nuri at doup
    menu:
        n "오늘 끝나면 뭐 해?"

        "끝나면 그냥 집으로 돌아갈 생각이었어.":
            $ loop_2_after_school_plan = "house"
            n "그러면 내가 정말 좋아하는 카페 있는데, \n같이 갈래?"
            n "거기 디저트가 진짜 맛있어~!"
        "도서관에 한 번 가보려고 했어.":
            $ loop_2_after_school_plan = "lib"
            n "도서관~? 무슨 책 보려고? ...나도 같이 가도 돼?"

    menu:
        "그래, 같이 가자.":
            show nuri smile blush
            with dissolve
            "내 대답에 누리는 살짝 들뜬 것 같다."
            $ nurilove += 1
            $ loop_2_nuri_company = True
        "미안, 다음에 같이 가자.":
            show nuri disappointed
            with dissolve
            "내 거절에 누리는 살짝 시무룩해지고 말았다."
            $ nurilove -= 1
            $ loop_2_nuri_company = False

    hide nuri
    with dissolve

    "쪽지를 주고받으며, 나는 누리와 이런저런 얘기를 나누었다. {p}그러다보니, 어느새 수업 끝을 알리는 종소리가 들렸다."
    "아까 하늘이가 부탁한 대로, \n나는 발걸음을 도서관으로 옮겼다."
    
    jump loop_2_after_school_library

label loop_2_after_school_library:
    scene bg school library afternoon
    with fade

    play music general2 fadein 1.0

    if loop_2_nuri_company == True:
        show hanl say at chls
        with dissolve
        show nuri smile at chrs, shade
    else:
        show hanl say
    with dissolve

    show hanl at doup

    h "와줘서 고마워요. \n전 반장인 하늘이라고 합니다."
    h "당신을 도서관으로 부른 건{cps=5}...{/cps}"

    if loop_2_nuri_company == True:
        h "학생증 발급을 도서관에서 해야 하기 때문입니다. \n여기 당신의 학생증입니다. 받아주세요."
        h "{cps=12}{i}학생증은 잃어버리지 마시길... {/i}{/cps}그럼, 이만."

        hide hanl
        with dissolve

        pause 0.5

        show nuri smile at center, light
        with ease

        pause 0.5

        show nuri at doup

        if loop_2_after_school_plan == "house":
            n "그럼 이제 귀찮은 일도 끝났으니, 케이크나 먹으러 갈까?"
            jump loop_2_after_school_cafe
        else:
            n "이제 귀찮은 일도 끝났으니~ \n내가 정말 좋아하는 카페 있는데, 같이 갈래? \n거기 디저트가 진짜 맛있어~!"
            menu:
                "(간다.)":
                    jump loop_2_after_school_cafe
                "(가지 않는다.)":
                    n "그럼 이제 귀찮은 일도 끝났으니, 집으로 돌아가자~ \n조심히 돌아가, {color=#AAAAAA}[prtname]{/color}~ 내일 보자!"
                    jump loop_2_after_school_home
    else:
        h "{cps=8}당신은 {i}이곳에 있을 사람이 아니기 때문{/i}입니다.{/cps}"
        h "...아닙니다. 방금 한 말은 잊어주세요. \n여기 당신의 학생증입니다. 받아주세요."

        menu:
            "그게 무슨 말이야?":
                h "아무것도 아닙니다. 잊어주시길 바랍니다."
                menu:
                    "(그냥 넘어간다)":
                        h "{cps=12}{i}학생증은 잃어버리지 마시길... {/i}{/cps}그럼, 이만."
                    "(끈질기게 물어본다)":
                        h "하... 말 그대로입니다. 당신은 이 학교에 있으면 안 됩니다."
                        p "......그게 무슨...? 내가 이 학교에 있으면 안 된다니?"
                        h "...더 이상은 말할 수 없겠군요. \n{cps=12}{i}학생증을 잊지 말고 챙겨주시기를 바랍니다. {/i}{/cps}그럼, 이만."
            "(침묵한다)":
                h "{cps=12}{i}학생증은 잃어버리지 마시길... {/i}{/cps}그럼, 이만."
        $ hanllove += 1

        jump loop_2_after_school_home

label loop_2_after_school_cafe:
    scene bg cafe lateafternoon
    with fade

    play music event fadein 1.0

    show nuri smile at center, doup
    with dissolve

    n "여기 케이크가 진짜 맛있어~! \n너도 한번 먹어봐~"

    menu:
        "(케이크를...)"

        "(먹는다)":
            "케이크가 입안에서 녹아내린다... {p}입 안 가득 퍼지는 달콤함이 기분 좋다."
            p "정말 맛있네."
            n "그렇지~? 나도 여기 케이크는 진짜 자주 먹으러 와~"
            $ nurilove += 1
        "(먹지 않는다)":
            n "여기 케이크 진짜 맛있는데... 안 먹으면 내가 다 먹어야지!"
            "누리가 케이크를 전부 먹어 치운다. {p}눈을 감고 기분 좋다는 듯이 흥얼거리는 걸 보니 정말 맛있는 모양이다."
            n "나는 기분이 별로거나 우울할 때,{w=0.5} 여기 케이크를 먹으러 와. {p}너는 특별히 새로 왔으니까 알려주는 거야!"
            n "너도 나중에 기분 안 좋을 때 여기 케이크를 먹어봐. \n기분이 금방 좋아질걸!"
    
    "디저트와 음료를 다 먹은 우리는, "
    show nuri at disappear  # `hide nuri with dissolve` is not suitable here.
    extend " \n헤어져 각자 집으로 돌아갔다."

    jump loop_2_after_school_home
    
label loop_2_after_school_home:
    scene bg home bedroom night
    with fade

    "전학 온 첫날이지만, \n좋은 친구를 사귄 것 같아 기분이 좋았다."

    if loop_2_nuri_company == False:
        "아까 도서관에서 하늘이가 한 말은... \n무슨 뜻이었을까. {p}일단은 깊이 생각하지 않기로 했다. 별거 아니겠지."
    
    "나는 씻고 침대에 눕자마자 잠에 들었다."

    jump loop_3