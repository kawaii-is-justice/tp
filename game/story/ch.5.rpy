label loop_6:
    $ save_name = "마지막 봄날"

    scene bg school classroom morning with Fade(2.0, 0.0, 2.0)
    play music general1 fadein 1.0

    "......또 다시 이 교실에 있었다. {p}이제는 확실했다. {p}같은 날이 반복되고 있었다."
    "손을 주머니에 넣자, 익숙한 감촉이 느껴졌다. \n수첩은 제 자리에 잘 있었다."
    "생각이 잠깐 멍해지려던 그때, 익숙한 목소리가 들려왔다."

    show nuri say at center, doup with dissolve

    n "안녕~ 전학생! 난 누리. {p}전학생은 이름이 뭐야?"
    "나는 잠시 멈칫했다가 이름을 말했다."
    p "내 이름은... {color=#AAAAAA}[prtname]{/color}."

    show nuri smile with dissolve

    n "{cps=6}{color=#AAAAAA}[prtname]{/color}...{/cps} 좋은 이름이네. \n앞으로 친하게 지내보자, 전학생!"
    "누리는 해맑게 웃었다. 하지만 그 눈빛 어딘가에서, 지금까지와는 조금 다른 기색이 느껴졌다."

    scene bg school rooftop with Fade(1.0, 0.0, 1.0)

    "쉬는 시간이 되자, 하늘이와 누리가 함께 옥상으로 올라가는 게 보였다."
    "나는 누리의 상태를 알고 싶어서, 둘을 조심히 따라가 문 뒤에서 대화를 엿들었다."

    show nuri say at chls with dissolve
    show hanl at chrs with dissolve

    n "...반장, 할 말이 있다고 했지? \n무슨 일인데 학교 옥상까지 올라온 거야?"
    "하늘이는 한참 동안 침묵하다, 조용히 입을 열었다."

    show hanl say

    h "큰 일인 건 아닙니다. 다만, 누리. 당신은 가끔..."
    extend " \n...당신이 느끼는 감정의 이유를, {w}생각해 본 적이 있습니까?"
    n "갑자기 그게 무슨 소리야? \n무슨 이유?"
    h "당신이 전학생에게 느끼는 감정이... {p}어쩌면 당신 본래의 감정이 아닐지도 모릅니다."

    show nuri shy at doup with dissolve

    "누리는 얼굴을 붉히며 당황한 기색을 보였다."
    n "그, 그게 무슨 뜻이야? \n내가 가진 감정이 가짜라는 거야?"
    h "전학생을 처음 본 순간부터 강한 호감을 느끼셨겠지요."
    h "하지만 그 감정이 지나치게 빠르고 강하다는 건... \n이상하다고 생각하지 않으셨나요?"

    show nuri angry

    n "그냥 첫눈에 반한 거겠지. \n사람 마음에 꼭 이유가 있어야 되는 건 아니잖아?"
    h "아닙니다. \n감정은 기억과 맥락, 시간이 쌓여야 만들어지는 겁니다."
    h "하지만 당신의 감정엔, \n어떠한 당위도 근거도 없습니다."

    show nuri sad with dissolve

    n "......그런 건 생각해 본 적 없어. \n나는 그냥{cps=6}...{/cps} 내가 느끼는 대로 좋아한 것 뿐인데."
    "하늘이는 조용히 고개를 숙였다가 돌아서서 내가 있는 문 쪽으로 걸어왔고, 나는 급히 몸을 숨길 수밖에 없었다."

    show hanl with dissolve

    h "...이제는 더 이상 막을 수 없을지도 모르겠군요."

    hide hanl with dissolve
    show nuri sad at center with ease

    "하늘이 계단을 내려가는 소리가 멀어지고, \n나는 조심스럽게 옥상에 남아있는 누리에게 다가섰다."

    n "내 감정이... 가짜라고? \n말도 안 돼. \n난 그냥..."
    "누리는 나를 발견하자 금세 표정을 바꾸고,"
    show nuri smile at center with dissolve
    extend " 환하게 웃으며 말했다."

    show nuri smile at doup

    n "{color=#AAAAAA}[prtname]{/color}! \n내가 전학생 이름은 똑똑히 외워뒀다고."
    n "옥상엔 어쩐 일이야? \n길이라도 잃어버린 거야?"
    "누리는 평소처럼 웃고 있었지만, \n눈빛은 흔들리고 있었다."

    if nurilove >= 8:
        "그렇게 웃는 누리를 보며... \n나는, 이상하게 마음이 놓였다."

    window hide dissolve
    scene bg school cafeteria with Fade(1.0, 1.0, 1.0)

    "점심시간이 되어 급식실로 향했다. \n정말이지, 몇 번을 반복해도 이 학교 급식은 맛있다."

    show nuri say at center, doup with dissolve

    n "전학생~ 오늘 급식 메뉴가 뭐~게~? {w=0.25}\n오늘은 카레랑 오므라이스래! 자, 너부터 골라봐."
    n "[loop_0_lunch_menu]" (multiple=2)
    p "[loop_0_lunch_menu]" (multiple=2)

    show nuri smile at doup

    n "우와, 우리 역시 잘 통하는 거 같지 않아?"
    "나는 어색하게 웃으며 고개를 끄덕였다."
    "식사 도중, 누리가 갑자기 말을 꺼냈다."

    show nuri smile blush with dissolve

    n "있잖아{cps=6}...{/cps} 오늘 너랑 처음 만났는데도,"
    n "이상하게 너를 보면 마음이 이상해져. \n교실에 들어왔을 때부터, 뭔가 운명 같은 느낌이 들었달까... 히히, 너무 쑥스러웠지?"
    "누리는 부끄럽게 웃었지만, 그 눈빛은 진심이었다."

    scene bg school library afternoon with Fade(1.0, 1.0, 1.0)

    "방과 후가 되자, 하늘이가 나를 조용히 불렀다."
    "나는 이미 예상하고 있었기에, 별 말 없이 따라갔다."
    "도서관 문을 열고 들어가려는 찰나, 누리가 다급하게 뒤에서 말을 걸었다."

    show nuri smile at center with dissolve

    n "{color=#AAAAAA}[prtname]{/color}, 도서관엔 무슨 일이야? \n반장이 부른 거 맞지?"
    p "어떻게 알았어?"

    show nuri smile at doup

    n "그냥... 감이랄까. \n왠지 반장이 너를 데려가려는 거 같아서."

    show nuri smile at chls with ease
    show hanl at chrs with dissolve

    h "...도서관에까지 따라오시다니. \n일단 안으로 들어오시죠, {color=#AAAAAA}[prtname]{/color}."
    "나는 숨을 고르며 조용히 도서관 안으로 걸음을 옮겼다. \n문이 닫히자, 복도의 소음이 완전히 사라지고, \n책장 사이를 스치는 먼지 냄새와 낮은 정적만이 남았다."

    show nuri sad with dissolve

    "누리는 잠시 머뭇거리다가 내 옆으로 다가왔다. \n눈빛은 흔들렸지만, 입술은 꽉 다문 채였다."
    n "나도... 같이 들어가면 안 돼?"

    show hanl angry

    "하늘이의 표정이 단단히 굳었다. 차가운 기운이 도서관 안을 채우는 듯했다."
    h "누리, 당신은 지금 들어오면 안 됩니다."
    n "왜? {p}왜 난 안 되는 건데?"

    show nuri angry

    n "하늘이 너... \n전학생이랑 나를 계속 떨어뜨려 놓으려고만 하잖아!"

    show hanl say

    "하늘이는 잠시 눈을 감았다가 뜨며, \n낮고 단호한 목소리로 말했다."
    h "당신이 여기 있으면... \n전학생에게도, 당신에게도 좋지 않습니다."
    n "난 몰라! \n난 그냥... 전학생이랑 같이 있고 싶다고! \n그게 전부야!"
    "누리의 목소리는 도서관 천장에 부딪혀 메아리쳤다. \n적막 속에서 그녀의 떨림과 숨소리가 더 크게 들렸다."
    "하늘이는 그 모습을 보며 미묘하게 눈이 흔들렸지만, \n시선은 다시 차갑게 굳었다."
    h "......전학생, \n이제 더는 미룰 수 없습니다."

    show nuri sad
    show hanl

    "하늘이는 나를 똑바로 바라봤다. {p}누리 또한 울먹이며 나를 올려다봤다."

    "내 앞에는 두 개의 시선이 마주치고 있었다."
    "한쪽에는 손을 뻗고 울먹이며 기다리는 누리가, \n다른 한쪽에는 차분하고 단호한 하늘이가 있었다."
    "내 심장 소리가 유독 크게 들리는 것 같았다."

    menu:
        "(하늘이의 손을 잡는다.)":
            if hanllove >= 6:
                jump end_hanl
            else:
                jump end_hanl_low
        
        "(누리의 손을 잡는다.)":
            if nurilove >= 8:
                jump end_nuri
            else:
                jump end_nuri_low

label end_hanl:
    $ save_name = "결말 1: 마지막 봄날"

    stop music fadeout 1.0
    scene bg school library afternoon with Fade(1.0, 1.0, 1.0)
    play music end fadein 1.0

    show nuri sad at chls, ishade with dissolve
    show hanl smile at chrs with dissolve

    "하늘이가 내 손을 잡았다. 처음으로, 차가운 손이 약간 떨리고 있었다."
    h "......감사합니다. \n당신이 날 믿어준다면... 이 루프는, 오늘로 끝날겁니다."

    show hanl smile blush with dissolve
    
    "하늘이가 나를 바라보며 미묘하게 미소를 지었다. \n언제나 무표정했던 얼굴에 처음으로 온기가 스쳤다."
    "처음으로 알았다. \n하늘이의 눈빛 속에, 이런 따뜻함이 숨어 있었다는 걸."

    hide nuri with dissolve
    show hanl smile blush at center with ease

    "하늘이를 따라 도서관 안쪽으로 들어가자, \n눈부심과 함께 시야가 뒤집히고──"

    stop music fadeout 0.5
    scene bg hospital with Fade(2.0, 3.0, 2.0, color="#FFF")
    play music general1 fadein 0.5

    "눈을 떴다. {p}창밖의 햇살, 커튼, 기계음."
    "옆에서 익숙한 목소리가 들려왔다."

    show hanl smile at center with Dissolve(1.0)

    h "돌아오신 것을 환영합니다. \n{color=#AAAAAA}[prtname]{/color}."
    "{color=#CC254F}~ 결말 1: 마지막 봄날 ~{/color} \n\n\n{space=880}세션 종료."

    stop music fadeout 1.0
    window hide dissolve
    hide hanl with dissolve
    show solid white at white_fadein
    pause 3.0
    jump splashscreen


label end_hanl_low:
    $ save_name = "결말 2: 끝없는 하루의 끝"

    stop music fadeout 1.0
    scene bg school library afternoon with Fade(1.0, 1.0, 1.0)
    play music end fadein 1.0

    "하늘이는 말 없이 내 팔을 잡아끌며 도서관 안쪽으로 들어갔다. 그 눈에는 감정이 거의 없었다."

    show hanl say at center with dissolve

    h "......이제야 선택하셨군요. {p}늦지 않았길 바랍니다."
    "머리가 점점 어지러워졌고 심장은 빠르게 뛰었다."

    stop music fadeout 0.5
    scene bg hospital with Fade(2.0, 1.0, 2.0, color="#FFF")
    play music general1 fadein 0.5

    "눈을 떴다. {p}창밖엔 햇살과 기계음뿐. {p}옆에는 아무도 없었다."
    p "......끝난 걸까?"
    "{color=#CC254F}~ 결말 2: 끝없는 하루의 끝 ~{/color} \n\n\n{space=880}세션 종료."

    stop music fadeout 1.0
    window hide dissolve
    show solid white at white_fadein
    pause 2.0
    jump splashscreen

label end_nuri:
    $ save_name = "결말 3: 끝없는 봄날"

    stop music fadeout 1.0
    scene bg school library afternoon with Fade(1.0, 1.0, 1.0)
    play music end fadein 1.0

    "나는 누리의 손을 잡았다. \n그러자 누리의 얼굴이 금세 환해졌다."

    show nuri smile at chls, doup with dissolve
    show hanl sad at chrs, ishade with dissolve

    n "정말... 나랑 있어주는 거야? \n후후... 고마워."
    "하늘이는 한 발 물러서서 우리를 바라봤다. {p}그 눈빛엔 체념과 슬픔이 묻어 있었다."
    h "......당신의 선택이라면, \n더 이상 말리지 않겠습니다."

    hide hanl with dissolve
    show nuri smile blush at center with ease

    "세계가 녹아내리듯 일렁였다. \n하얀 빛이 스며들었고, 주위의 소리는 모두 사라졌다."

    scene bg school classroom morning with Fade(2.0, 1.0, 2.0, color="#FFF")

    "눈을 뜨자, 다시 교실이었다. \n하지만 이번엔 모든 게 평화롭고 고요했다. \n옆에서는 누리가 웃으며 나를 바라보고 있었다."

    show nuri smile at center, doup with dissolve

    n "좋은 아침~ 전학생! \n앞으로도{cps=6}...{/cps} 매일 같이 있자."
    "누리의 미소는 누구보다 따뜻했기 때문에, {p}나는 더 이상 아무것도 의심하지 않았다."
    "{color=#CC254F}~ 결말 3: 끝없는 봄날 ~{/color} \n\n\n{space=880}세션 종료."
    
    stop music fadeout 1.0
    window hide dissolve
    show solid white:
        alpha 0.0
        linear 3.0 alpha 1.0
    pause 4.0
    jump splashscreen

label end_nuri_low:
    $ save_name = "결말 4: 영원히 함께"

    stop music fadeout 1.0
    scene bg school library afternoon with Fade(1.0, 1.0, 1.0)
    play music end fadein 1.0

    "나는 누리의 손을 잡았다."
    "누리는 작게 웃었지만, \n그 미소 어딘가에는 섬뜩한 구석이 있었다."
    
    show nuri smile at chls, doup with dissolve
    show hanl sad at chrs, ishade with dissolve

    n "후후... 결국 나를 선택했네. {p}이제{cps=6}...{/cps} 영원히 같이 있는 거야."

    hide hanl with dissolve
    show nuri smile at center with ease

    "하늘이는 아무 말 없이 사라졌다. \n도서관은 조용히 빛에 잠기며 형태를 잃었다."

    scene bg school classroom morning with Fade(2.0, 1.0, 2.0, color="#FFF")

    "눈을 뜨자, 교실이었다."
    "창밖으로는 고요하게 봄의 정경이 보였다. \n어느샌가 누리가 내 손을 꼭 쥐고 있다는 사실을 눈치챘다."

    show nuri smile blush at center with dissolve

    n "......이제 네 옆에는 나 밖에 없어. {p}{cps=4}우리, 계속 이렇게 있을 거야.{/cps} 그치?"
    "미소 짓는 누리의 눈동자 속에, \n알 수 없는 그림자가 있었다."
    "......왜인지 모르게, \n차가운 전율이 등줄기를 타고 흘러내렸다."
    "{color=#CC254F}~ 결말 4: 영원히 함께 ~{/color} \n\n\n{space=880}세션 종료."

    stop music fadeout 1.0
    window hide dissolve
    show solid white at white_fadein
    pause 2.0
    jump splashscreen