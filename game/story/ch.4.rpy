label loop_4:
    $ save_name = "봄의 파편"

    stop music fadeout 1.0
    scene bg school classroom morning with Fade(2.0, 2.0, 2.0)
    play music general1 fadein 1.0

    "...졸았던 건가? \n이상하게 어지럽네..."

    show nuri say with dissolve

    n "좋은 아침~ 전학생! 난 누리야. \n전학생은 이름이 뭐야?"
    p "아... 내 이름은 {color=#AAAAAA}[prtname]{/color}."

    show nuri smile

    n "{color=#AAAAAA}[prtname]{/color}... 좋은 이름이네. 앞으로 잘 부탁해!"

    scene bg school hallway
    with dissolve
    pause 0.3

    "쉬는 시간에, 나는 학교 구경도 할 겸 혼자서 복도를 돌아다니고 있었다."
    "그때, 복도 한쪽에서 하늘이와 누리의 대화가 들려왔다."

    show nuri frown at chls with dissolve
    show hanl at chrs with dissolve

    n "...하늘이 너 오늘 좀 이상해. \n아까 전학생이랑 대화하고 나서 왜 그런 말을 한 거야?"

    show hanl say

    h "어떤 말 말입니까?"
    n "네가 나 보고 전학생을 멀리하는 게 좋겠다고 했잖아. \n무슨 뜻이야?"
    h "그건..."

    show nuri disappointed

    n "전학생이랑 얘기해 보니 그리 나쁜 친구 같지도 않고,"
    n "게다가 왠지 모르겠지만, 전학생이랑 대화하면 기분이 나쁘지 않아..."
    h "...당신은 전학생에게 관심이 많군요."

    show nuri shy at doup

    n "에? 무, 무슨 소리를 하는 거야?"
    n "그냥! 전학생이기도 하고, 옆자리라 조금 챙겨주려고 한 것 뿐인데..."
    h "조심하는 게 좋을지도 모릅니다."
    n "...뭐라고?"
    h "별 말 아닙니다. 실례하겠습니다."

    hide hanl with dissolve

    "하늘이는 조용히 돌아선 뒤 복도 저편으로 사라졌다."
    "누리는 멍하니 그 뒷모습을 바라보다, 작게 중얼거렸다."

    show nuri sad at center with ease

    n "...도대체 무슨 뜻이람."

    scene bg school classroom morning with Fade(1.0, 1.0, 1.0)

    show nuri smile at center, doup with dissolve

    n "전학생~ 같이 점심 먹으러 갈래?"
    n "오늘 전학 왔으니까 궁금한 게 많을 것 같아서... \n같이 밥도 먹고 이야기도 하고 그런 거지 뭐~"

    window hide dissolve
    menu:
        "그래, 같이 가자.":
            $ nurilove += 1

            hide nuri with dissolve
            scene bg school cafeteria with Dissolve(1.0)
            show nuri smile at center, doup with dissolve

            n "오늘 점심 메뉴는 카레랑 오므라이스래! \n너랑 같은 거 먹을 테니 골라봐!"
            p "음... 역시 {color=#FFAEC9}[loop_0_lunch_menu]{/color}가 좋겠어."
            n "나도 {color=#FFAEC9}[loop_0_lunch_menu]{/color} 좋아하는데, 잘됐네~"
            "나는 누리와 점심을 맛있게 먹었다."
        
        "혼자 먹고 싶어.":
            $ nurilove -= 1

            hide nuri with dissolve
            scene bg school cafeteria with Dissolve(1.0)
            
            p "혼자 먹으니까 쓸쓸하네... \n역시 누리랑 같이 먹을 걸 그랬나..."
            "점심시간이 끝나갈 무렵, 누리가 나를 찾아왔다."

            show nuri say at center, doup with dissolve

            n "다 먹었어? \n히히... 밥은 같이 못 먹었어도, \n학교 구경은 시켜줘야 할 것 같아서..."
            p "그래, 같이 가자."

    hide nuri with dissolve
    scene bg school hallway with Dissolve(1.0)
    show nuri smile at center with dissolve

    n "소화도 시킬 겸 운동장 산책할까? \n아니면..."

    show nuri smile at chrs with ease
    show hanl say at chls with dissolve

    h "전학생, \n...잠시, 도서관 쪽으로 와주시겠습니까?"

    show nuri embarrassed

    n "어... 어라? \n반장, 무슨 일이야?"
    h "학생증 발급에 관련된 일입니다. \n도서관 쪽 업무이므로, \잠시 데려가겠습니다."
    n "아... 그래? \n음... 그럼 이따 교실에서 봐."

    hide nuri with dissolve
    show hanl at center with ease

    "하늘이는 아무 말 없이 고개를 끄덕이며 앞서 걷는다."
    p "도서관에서 학생증이라니... \n일단 따라가보자."

    stop music fadeout 0.5
    scene bg school library morning with Dissolve(1.0)
    play music general2 fadein 0.5

    show hanl at center, doup with dissolve
    
    h "잠시만 기다려 주시겠습니까."
    "그렇게 말하고서는, 하늘이는 곧바로 책장 너머로 사라졌다."

    hide hanl with dissolve
    window hide dissolve

    menu:
        "(가만히 기다린다.)":
            p "괜히 이상한 짓 하지 말고... \n가만히 기다리자."
            p "잠깐 기다리는 것 정도야 뭐..."
            "자리에 앉아 조용히 도서관 내부를 둘러보던 중, 익숙한 책들이 보였다."
            p "그런데 이 책장... \n어디서 본 것 같은데..."
            "그 책장 한 구석에, 눈에 띄지 않게 꽂힌 작은 수첩 하나가 보였다."
            p "도서관을 이용했던 다른 학생이 두고 간 건가...?"

        "(도서관 안을 둘러본다.)":
            p "잠깐 기다리라고는 했지만... \n그냥 서 있긴 좀 심심하네."
            p "도서관을 조금 둘러보는 것 정도는 괜찮겠지..."
            menu:
                "(안쪽으로 들어간다.)":
                    "시간을 주제로 한 책들이 모여있는 책장이 눈에 띄었다."
                    "그 중에, 전혀 어울리지 않는 작은 수첩 하나가 눈에 들어왔다."
                    p "이건...?"
                
                "(근처를 둘러본다.)":
                    "입구에서 좀 떨어진 곳에 있던 책장을 둘러보던 중에, 다른 책들과 달리 먼지가 전혀 쌓이지 않은 수첩 하나가 눈에 보였다."
                    p "여긴 사람 손이 잘 안 닿는 구역 같은데... \n이 수첩만 유독 깨끗하네."
                    "나는 호기심에 이끌려 수첩을 잡았다."

    "수첩의 표지에는 아무런 표시도 없다. 주인을 찾아줄 단서가 될까 싶어서, 나는 첫 장을 펼쳤다."
    "그러자, 나와 매우 비슷한 필적이 보였다."

    "{color=#7F7F7F}(수첩의 안쪽에는...){/color} \n{fast}'누리는 내 이름을 알고 있었다.'"
    extend " \n'...이 학생증은 뭐지?'"
    "{color=#7F7F7F}(수첩의 안쪽에는...){/color} \n{fast}'누리는 내가 좋아하는 걸 어떻게 알고 있는 거지?'"
    extend " \n'하늘이가 자꾸 이상한 말을 한다.'"
    "{color=#7F7F7F}(수첩의 안쪽에는...){/color} \n{fast}'이 수첩은 내가 남긴 것 같다.'"
    extend " \n'어째서인지 이 수첩만은 그대로 남아있다.'"
    "{color=#7F7F7F}(수첩의 안쪽에는...){/color} \n{fast}'내가 발견하기 쉬운 곳에 두자. {p}원래 있던 곳이 아마 그런 곳일 것이다.'"
    "{color=#7F7F7F}(수첩의 안쪽에는...){/color} \n{fast}'나에 대한 누리의 집착이 점점 심해지는 것 같다...'"
    extend " \n'하늘이는 이미 알고 있을지도 모른다.'"
    extend " \n'누리는 잘 모르는 것 같지만...'"

    "혼란스러운 내용이 가득한 수첩을 멍하니 바라보던 나는, \n하늘이의 발소리에 깜짝 놀라 그대로 굳었다."

    show hanl with dissolve
    show hanl say

    h "기다리게 해서 죄송합니다. 여기, 당신의 학생증입니다. \n학생증은... 잃어버리지 마시길."
    h "...실례지만, \n손에 들고 계신 건 무엇입니까?"

    menu:
        "(수첩의 내용을 보여준다.)":
            $ hanllove += 1
            "나는 잠시 망설이다가 수첩을 하늘이에게 건넸다."
            p "이거... 도서관에서 발견했어. \n혹시 네가 떨어뜨린 건 아니지?"
            "하늘은 수첩을 받아 들고 조용히 페이지를 넘긴다. 그녀의 눈빛이 미세하게 흔들렸다."
            h "......이건 제 것이 아닙니다. \n하지만{cps=6}...{/cps} 어떤 의미에선 익숙하군요."
            p "무슨 뜻이야? \n여기 적힌 내용들, 혹시 아는 게 있어?"
            h "......그건, \n언젠가 당신이 직접 알게 될 겁니다."
            h "받으시죠. {p}...이건 아마도 당신의 것이 맞을 겁니다."
            "나는 말없이 수첩을 받아 품에 넣었다."

        "(수첩을 숨긴다.)":
            $ hanllove -= 1
            p "아... 아무것도 아니야. \n그냥... 평소에 생각을 정리하려고 쓰는 거야."
            h "......그렇군요, 알겠습니다."
            h "할 일은 마쳤으니, \n이제 돌아가셔도 됩니다."
            "하늘이가 앞장서서 도서관을 나섰다. 나는 수첩을 품 안에 꼭 넣은 채, 하늘이를 따라 교실로 향했다."

    scene bg school classroom morning with Fade(0.5, 0.5, 0.5)

    "도서관에서 돌아온 나는 책상에 앉아, 멍하니 수첩을 만지작거리고 있었다."

    show nuri smile with dissolve
    show nuri say at doup

    n "전학생~ 오늘 끝나고 뭐해? \n별일 없으면... 같이 카페 가자~"
    p "카페...?"
    n "응! 전학생한테 꼭 보여주고 싶은 곳이 있어. \n내 비밀 아지트랄까~ 헤헤."
    "잠시 망설이다가 누리와 눈이 마주쳤다. 밝게 웃는 얼굴이었지만, 아까 본 글귀가 떠올라 어딘가 묘한 기분이 들었다."

    menu:
        "(같이 간다.)":
            $ nurilove += 2
            hide nuri with dissolve
            jump cafe_event
        
        "(거절한다.)":
            $ nurilove -= 1
            jump skip_cafe

label cafe_event:
    stop music fadeout 1.0
    scene bg cafe lateafternoon with Fade(1.0, 0.0, 1.0)
    play music event fadein 1.0

    show nuri say at center, doup with dissolve

    n "여기 케이크 진짜 맛있어! \n그중에서 내가 제일 좋아하는 건——"
    n "이 딸기가 올라간 초코 케이크! \n전학생도 한 입 먹어볼래?"

    menu:
        "(먹는다.)":
            $ nurilove += 1
            "케이크를 한 입 먹었다. {w}케이크는 부드럽게 녹아내리며 달콤함으로 입 안을 채웠다."
            p "정말 맛있네."
            n "그렇지~? \n나도 여기 케이크는 자주 먹으러 와!"

        "(먹지 않는다.)":
            $ nurilove -= 1
            show nuri frown
            n "에~ 여기 케이크 진짜 맛있는데..."
            show nuri smile
            extend " \n안 먹으면 내가 다 먹어야겠다!"
            "누리는 케이크를 전부 먹어 치우고는, 눈을 감고 기분 좋다는 듯 흥얼거린다."
    
    show nuri smile at doup

    n "나는 기분이 별로거나 우울할 때, \n여기 케이크를 먹으러 와."
    n "너는... {p}특별하니까 알려주는 거야."
    "누리가 밝게 웃으며 말했다."
    "...하지만 나는 마냥 기뻐할 수 없었다. 특별하다니... 무슨 뜻이지?"
    "아까 도서관에서 봤던 수첩의 글귀가 머릿속을 스쳤다."
    "눈 앞의 누리는 해맑게 웃고 있었지만, {w}그 웃음 뒤에 숨어 있는 감정이 무엇인지 알 수 없었다."
    "...정말로, {w}그냥 호의일까? 그게 아니라면——"
    "카페를 나서자, 저녁 공기가 서늘하게 느껴졌다."
    n "오늘 즐거웠어~! \n내일 학교에서 봐, 전학생!"
    "누리는 골목 끝으로 달려가듯 사라졌다. 나는 혼자 집으로 향했다."

    hide nuri with dissolve
    jump evening

label skip_cafe:
    pause 0.5
    show nuri disappointed with dissolve
    "나는 누리의 제안을 거절했다. 누리는 살짝 아쉬운 표정으로 고개를 끄덕였다."
    hide nuri with dissolve
    jump evening

label evening:
    stop music fadeout 1.0
    scene bg home bedroom night with Fade(1.0, 0.0, 1.0)
    play music general1 fadein 1.0

    "나는 방에 돌아오자마자, 수첩을 꺼내서 책상 위에 올려두었다."
    p "...이 수첩. \n정말 내가 쓴 걸까? 그렇다면—— {p}지금의 나는, 몇 번째인 거지?"
    "머리가 복잡했다. \n눈꺼풀이 무거워졌다."
    p "......지금 잠들면... \n또 전부 잊어버리는 걸까..."
    "천천히 눈이 잠기며, \n나는 꿈 속으로 잠겨들었다."
    
    jump loop_5

label loop_5:
    stop music fadeout 1.0
    scene bg school classroom morning with Fade(1.0, 1.0, 1.0)
    play music general1 fadein 1.0

    "......또, {w}교실이다."
    "내 자리, \n창밖의 풍경, \n그리고——"
    "나에게 말을 걸러 오는 누리까지. \n모든 게... 똑같다."
    "한편, 손에 닿는 수첩의 감촉이 희미하게 느껴졌다."
    "이번엔{cps=6}......{/cps} 기억을 잃지 않았다. 수첩 덕분일까."

    show nuri smile at center with dissolve
    show nuri say at doup

    n "좋은 아침~ 전학생! 내 이름은 누리야. \n네 이름은 뭐야?"
    "누리는 고개를 살짝 기울이며 내 대답을 기다렸다. \n이번엔... 내 이름을 모르는 모양이네."

    menu:
        "(진짜 이름을 알려준다.)":
            p "내 이름은... {color=#AAAAAA}[prtname]{/color}."
            n "{color=#AAAAAA}[prtname]{/color}~ 좋은 이름이네! \n앞으로 잘 부탁해, 전학생!"
            "누리의 웃음은 해맑았다. \n하지만 나는 알 수 없는 위화감을 느꼈다."
        
        "(없는 이름을 지어낸다.)":
            p "내 이름은... {p}누바라고 해."
            show nuri embarrassed
            n "누...바?"
            p "응, \n누리 바보라는 뜻이야."
            show nuri smile at doup
            n "정말~! \n처음 보는 사이에 무슨 그런 장난을 치고 그래~"
            n "전학생은 장난꾸러기구나! 근데, 진짜 이름은 뭐야?"
            p "내 이름은... {color=#AAAAAA}[prtname]{/color}."
            n "{color=#AAAAAA}[prtname]{/color}~ 좋은 이름이네! 앞으로 잘 부탁해!"
            "누리는 이런 수준 높은 유머에도 싫은 기색은 커녕, 즐겁게 웃어줬다."
            "...이번에도, {p}누리는 나를 좋아하는 것 같다."

    scene bg school hallway with dissolve

    "쉬는 시간에, 나는 화장실에 갔다가 돌아오고 있었다."
    "그러던 중에, 복도 끝에서 누리와 하늘의 목소리가 들려왔다."

    show nuri frown at chls with dissolve
    show hanl say at chrs with dissolve

    h "......전학생에게서 거리를 두는 게 좋습니다."
    n "그게 무슨 말이야? 반장, 왜 그래? \n전학생이랑 얘기 좀 하는 게 뭐가 문제야?"
    h "......당신은 모릅니다. \n당신도, 전학생도 위험할 수 있어요."
    n "위험하다니? \n그냥... {w}전학생이랑 같이 있는 게 좋은 건데..."
    "누리는 어리둥절한 얼굴로 고개를 갸웃했다. 하늘이는 더 말하지 않고 조용히 시선을 돌렸다."
    "......이 대화가 어째서인지 익숙한 탓에, 나는 더욱 불안해졌다. 하늘이는{cps=6}......{/cps} 이번에도, 알고 있는 걸까."

    hide nuri
    hide hanl
    with dissolve
    scene bg school classroom morning with dissolve

    "수업의 끝을 알리는 종이 울리자, 교실 안은 급식 이야기로 금세 떠들썩해졌다."

    show nuri smile at center, doup with dissolve

    n "오늘 급식은 카레랑 오므라이스래! {color=#AAAAAA}[prtname]{/color}, 같이 밥 먹으러 가자~!"

    hide nuri with dissolve
    window hide dissolve
    scene bg school cafeteria with fade
    
    menu:
        "(누리와 같이 점심을 먹을까?)"
        "(점심을 같이 먹는다.)":
            $ nurilove += 1
            "누리는 신난 표정으로 내 팔을 잡고 급식실로 향했다. 밥을 먹는 내내 누리는 즐겁게 떠들었지만, 나는 익숙한 장면에 조용히 숟가락만 움직였다."
            "우리는 점심을 맛있게 먹은 뒤 헤어졌다. 나는 남은 점심시간 동안 수첩을 발견했던 도서관에 가보기로 했다."
        
        "(점심을 같이 먹지 않는다.)":
            $ nurilove -= 1
            p "오늘은 혼자 먹을게."
            show nuri disappointed with dissolve
            n "...아, 그래...?"
            "대답을 마치자마자, 누리의 표정이 눈에 띄게 어두워졌다."
            hide nuri with dissolve
            extend " \n누리는 대신 친구들과 밥을 먹으러 갔다."

            menu:
                "(이제 뭘 해야 하지...)"
                "(혼자 밥을 먹는다.)":
                    "나는 혼자 밥을 먹었다. 그런데, 이상할 정도로 자주 누리와 시선이 마주쳤다."
                    "멀리서도 계속 나를 신경쓰는 듯한 눈빛이 신경쓰였지만, 나는 밥을 다 먹고 나서 수첩을 확인하러 도서관에 가 보기로 마음먹었다."
                
                "(도서관에 가본다.)":
                    "나는 점심시간을 활용해 수첩을 발견했던 도서관으로 가보기로 결정했다."

    stop music fadeout 1.0
    scene bg school library morning with Fade(1.0, 1.0, 1.0)
    play music general2 fadein 1.0

    "역시나 수첩이 있던 자리는 비어 있었다. 나는 잠시 책장을 둘러보고 있었는데, 어느새 하늘이가 조용히 나타나 나를 바라보고 있었다."

    show hanl at center, doup with dissolve

    h "전학생...입니까. 도서관에는 무슨 일로 오셨습니까? \n저는 같은 반 반장인 하늘이라고 합니다."

    menu:
        "(뭐라고 대답할까?)"
        "(하늘이에게 수첩에 관해 물어본다.)":
            p "혹시... \n여기 있던 작은 수첩 본 적 있어?"

            if hanllove >= 4:
                h "수첩{cps=6}...{/cps} 말입니까. {p}혹시 이것을 찾으시는 건가요."
                "하늘이가 품에서 낯익은 수첩을 꺼냈다. 지난 루프에서 봤던 그 수첩이었다."
                h "언제 두고 가신 건지는 모르겠지만... \n당신 것이 맞는 것 같군요. 받으시죠."
            
            else:
                h "수첩... 말입니까. \n...아뇨, 본 적 없습니다."
                "하늘이가 무언가를 숨기고 있는 것 같은 기분이 들었다."

        "(대충 둘러댄다.)":
            p "그냥... \n책 좀 읽으러 왔어."
            h "그렇습니까. \n그럼 오신 김에 학생증을 받아 가시죠."
            "하늘이는 조용히 작은 카드를 나에게 내밀었다."
            h "학생증은... \n잃어버리지 마시길 바랍니다."

            if hanllove >= 4:
                h "......혹시, {p}이미 학생증을 가지고 계신 건 아니겠지요?"
                "그 말을 듣는 순간, 주머니 속 수첩과 카드가 떠올랐다."
    
    "이윽고 수업종이 울리자,"
    show hanl at disappear
    extend " 하늘이는 먼저 반으로 돌아가버렸다."

    scene bg school yard with Fade(1.0, 1.0, 1.0)

    "체육 시간이 되었다. 체육 선생님께서 오늘은 자유롭게 놀라고 하셨다."
    "선생님께서는 반 친구들에게 나와 친해져 보라고 하셨지만, 다들 자기 무리와 노느라 바빴다."

    show nuri say at center, doup with dissolve

    n "{color=#AAAAAA}[prtname]{/color}~ 같이 놀자!"
    "누리가 내 팔을 잡고 운동장으로 데리고 나갔다."

    show nuri smile

    "우리는 공을 주고받으며 잠시 웃었다. 그러다, 공이 예상치 못한 방향으로 튀어나갔다."

    hide nuri with dissolve

    "반사적으로 공을 잡으러 달려가려던 찰나, {w}누군가 내 팔목을 잡았다."

    show nuri embarrassed at chls with dissolve
    show hanl angry at chrs with dissolve

    h "멈추세요. 거긴... 위험합니다. 또 같은 일이 일어나게 둘 순 없습니다."
    n "어? 반장? 갑자기 왜 그래? 우린 그냥 놀고 있었는데..."
    "그 사이 공은 도로를 굴러가다, 지나가던 차에 부딪혀 힘없이 터졌다."
    "심장이 빠르게 뛰기 시작했다. 만약 방금 공을 잡으러 갔다면——"

    show hanl sad

    h "......이번에는... \n안 될지도 모르겠습니다."
    "......이번에는? 하늘이는...... 뭔가 알고 있는 걸까..."

    show nuri sad

    n "{color=#AAAAAA}[prtname]{/color}, 괜찮아? 어디 아픈 데라도 있어?"
    "내가 우두커니 서있자, 누리가 걱정하며 말을 걸었다."

    show hanl say

    h "운동장은{cps=6}...{/cps} 안전한 장소가 아닌 듯합니다. \n전학생, 저와 함께 이동하시죠."
    n "잠깐! 전학생을 어디로 데려가려는 거야? 오늘은 나랑 놀기로 했는데..."

    show nuri sad

    n "오늘 하루만이라도... 나랑 있어 줄 수 없을까?"
    menu:
        "(누리와 함께 운동장에 남는다.)":
            $ nurilove += 2
            $ hanllove -= 2

            p "...알았어. {w}누리, 너랑 같이 있을게."
            
            show hanl
            show nuri smile at doup

            n "정말? 진짜로!?"

            hide hanl with dissolve
            show nuri smile at center with ease

            "누리가 내 팔을 잡고 운동장을 이리저리 뛰며 웃었다. 하늘이는 어느샌가 사라졌다."
            n "{color=#AAAAAA}[prtname]{/color}... \n이 순간이... 계속됐으면 좋겠어."
            "누리의 눈빛이 순간, 알 수 없는 빛으로 반짝였다."

            stop music fadeout 0.5

            "{color=#FF0000}WARNING: 감정 수치 임계치 초과{/color}"
            "멀리서 하늘이가 뛰어오며 소리쳤다."
            h "...전학생, 조심하십시오──!"
            "갑자기 극심한 두통이 찾아왔다."
            "시야가 흔들리며, {p}눈앞의 사물들이 녹아내리기 시작했다."
            p "{cps=6}......{/cps}또, 무너지네..."
            "눈앞에 하얀 빛이 일렁이는게 느껴졌다."

        "(하늘이와 함께 이동한다.)":
            $ hanllove += 2
            $ nurilove -= 2
            window auto

            p "미안해, 누리야. \n지금은... 하늘이한테 가 봐야 할 것 같아."
            n "{cps=6}......{/cps}그래, {w}조심해..."

            window hide dissolve
            scene bg school library morning with Fade(1.0, 1.0, 1.0)

            "도서관 문이 닫히자, 적막만이 감돌았다."

            show hanl say at center with dissolve

            h "......겨우 막았습니다. \n전학생, 이제 느껴지십니까."
            h "이 세계는—— {p}안정적이지 않습니다."
            "그 순간, 바닥과 책장이 흔들렸다. 조명이 깜빡이며, 눈앞이 점점 하얘지기 시작했다."

            stop music fadeout 0.5
            show solid gray tp with Dissolve(1.0)

            "{color=#FF0000}WARNING: 세션 불안정{/color}"
            "{color=#FF0000}LOOP STABILITY: 최저{/color}"
            p "...이번엔...... \n어떻게 되는 걸까."
            "하늘이는 내 의문에 답하듯 말했다."

            show hanl with Dissolve(1.0)

            h "이 루프는 곧 끝납니다. \n하지만... 다음번엔, {w}반드시 선택하셔야 할 겁니다."
            "도서관의 풍경이 하얀 빛으로 일렁이며 녹아내리기 시작했다."

    scene bg white screen with Pixellate(2.0, 5)
    window auto

    "이윽고, 시야가 완전히 하얗게 물들었다."
    "...이번에도, 끝까지 버티지 못했네. {p}언제쯤, 끝을 낼 수 있는 걸까{cps=5}...{/cps}"

    window hide dissolve
    pause 0.5
    stop music fadeout 2.0
    jump loop_6