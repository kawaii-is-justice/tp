label loop_0:
    
    $ save_name = "멈춰 있는 봄"

    play music general1 fadein 1.0

    scene bg school classroom morning
    with Fade(1.0, 1.0, 1.0, color="#000")

    # refer to https://www.renpy.org/doc/html/text.html#dialogue-text-tags
    p_noname "여긴... 교실인가? {p}잠깐 정신을 잃었었나..."
    p_noname "어쩌다 전학을 오게 된 건지... {p}기억은 잘 나지 않지만..."

    "한 소녀가 활짝 웃으며 오른손을 크게 들고 내게 인사한다."

    show nuri smile at center, doup
    with dissolve

    stranger "전학생~ 전학생이구나~"
    n "난 {color=#FFAEC9}누리{/color}. {p}전학생, 넌 이름이 뭐니?"

    show nuri smile at ilight  # Without this, the following shade
    show nuri smile at shade   # animation would not work properly.

    $ prtname = get_name(banlist=banned_names)

    show nuri smile at light
    pause 0.75
    show nuri smile at doup

    n "음~ 그렇구나. \n좋은 이름인걸!"

    show nuri

    "누리는 옆자리에 앉아, 나를 신기하다는 듯이 빤히 쳐다봤다. {p=0.5}나는 그런 누리를 못 본 척했다."

    hide nuri
    with dissolve

    "이후, 정신없는 자기소개 시간과 수업 시간이 지나가고 \n기대하던 점심 시간이 왔다."
    "선생님과 반 친구들이 나를 신기한 눈으로 쳐다보긴 했지만, \n그럭저럭 잘 넘긴 것 같다."
    "이 학교의 급식은{cps=3}... {/cps}굉장히 맛있다고 한다... {p}게다가 점심 메뉴도 선택할 수 있다니, 기대가 된다."

    scene bg school cafeteria
    with fade

    show nuri smile at center, doup
    with dissolve

    n "전학생은 어떤 음식 좋아해? \n오늘 급식은 카레라이스랑 오므라이스, \n둘 중에 고를 수 있대!"
    n "나는 둘 다 좋아서 고민이야~ 전학생은 뭐 먹을래? \n참고로 내일은 돈까스와 제육볶음이고, \n그리고 모레는 김치볶음밥과 불고기..."

    menu:
        "이러다 올해 급식 메뉴를 전부 읊겠어... \n빨리 고르자."

        "카레라이스가 좋겠어.":
            $ loop_0_lunch_menu = "카레라이스"
        "오므라이스가 더 끌리는데.":
            $ loop_0_lunch_menu = "오므라이스"

    "누리는 내가 고른 메뉴를 따라 먹겠다고 했다. {p}첫날부터 밥 같이 먹을 사람이 생기다니... 참 다행이다."

    scene bg school classroom midday
    with fade

    show nuri smile at center, doup
    with dissolve

    n "점심시간 끝나면 바로 체육이야! \n체육복으로 갈아입고 운동장에서 보자!"
    n "설마 운동장도 못 찾아오는 건 아니겠지 전학생?"

    scene bg school yard
    with fade

    pe_teacher "전학생, 농구 실력 좀 볼까?"

    "선생님 말씀이 끝나기 무섭게 내 앞에 농구공이 떨어졌다."
    "내가 공을 주워 들려는 찰나, \n도로를 건너려는 고양이가 내 눈에 들어왔다."
    "고양이가 차에 치이려는 그 순간, \n나는 반사적으로 고양이에게 몸을 던졌다."

    stop music fadeout 1.0

    play sound car_accident

    "고양이를 구하기엔 충분했지만, {p}사람이 빠져나오기엔 부족한 시간이었다."

    "{cps=10}누군가 소리치며 달려오는 게 들렸다. {p}아마... 누리겠지.{/cps}{w=1.0}{nw}"
    "{cps=10}차는 땅에 곤두박질 쳐진 내 앞에 멈춰 섰다.{/cps}{w=1.0}{nw}"
    "{cps=10}아까 그 고양이는 \n나 따위는 안중에도 없다는 듯 도망갔다...{/cps}{w=1.0}{nw}"
    "{cps=10}그 모습이... 이상하게 눈에 밟힌다.{/cps}{w=1.0}{nw}"
    "{cps=10}이렇게... 죽는 걸까{/cps}{cps=20}...{/cps}{w=1.0}{nw}"
    "{cps=10}몸이... {/cps}{cps=5}너무 무겁다.{/cps}{w=1.0}{nw}"

    $ renpy.hide_screen("say")
    pause 0.5

    jump loop_1