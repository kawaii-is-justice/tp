label loop_3:

   $ save_name = "흔들리는 봄"

   scene bg school classroom morning
   with fade

   "......여긴?{p}또... 교실인 건가?"
   "......또?{p}내가 지금... 뭘 생각한 거지?\n전학 첫날이라 긴장했나......"

   show nuri smile at center, ishade
   with dissolve

   "나는 고개를 돌려 누리가 있는 쪽을 바라보았다."
   "누리는 뭔가 하려다 살짝 당황한 듯, 멈칫하며 말을 걸었다."

   show nuri at doup, light

   n "오~ 전학생! 감이 좋은걸~\n나는 {color=#FFAEC9}누리{/color}야.\n전학생은 이름이 뭐야?"

   menu:
      "(누리의 인사를 무시하고 자리에서 일어난다)":
         "그러자\n누리가 엄청난 괴력으로 나를 다시 자리에 앉혔다."
      "(아무 말이나 한다)":
         p "오늘 날씨가 참 좋네, 그렇지 않아?"
         "누리는 멈칫했지만 곧 웃으며 반응했다."
   
   show nuri:
      ease 0.5 chrs
   n "{color=#AAAAAA}[prtname]{/color}이구나~ "
   show nuri at doup
   extend "좋은 이름인걸!"

   "이게... 뭐지?{p}그러고보니 나도 자연스럽게 누리가 있던 곳을 쳐다봤어..."
   
   show hanl at chls
   with moveinleft

   "......응?{p}어느샌가 내 옆에는 반장인 하늘이가 와 있었고,"
   "하늘이는 내 팔을 잡은 채로 \n아무 말 없이 도서관 쪽으로 나를 끌고 갔다."

   scene bg school library morning
   with fade

   show hanl
   with dissolve

   show hanl say at doup

   h "당신... 당신 때문이에요... 알고 있나요?{w=2.0}{nw}"
   h "주머니를 확인해봐요."

   "나는 주머니를 더듬어보았다. \n그러자 작은 플라스틱 카드가 손에 잡혔다."
   "{cps=6}......{/cps}학생증이 들어 있었다."

   h "학생증은 도서관에서만 만들 수 있어요.\n그런데 당신이 이미 가지고 있다는 건... 역시——"

   # TODO: it would be nice to have a chromatic abberation effect here.

   "갑자기 엄청난 두통이 느껴지고 숨이 안쉬어졌다."

   p "{cps=10}......아파... 숨이......{/cps}{w=1.0}{nw}" with vpunch
   
   "나는 그대로 무너져 쓰러졌다."

   scene bg school nurseoffice
   with fade

   p "......아으... 머리야......"

   school_nurse "일어났니, 전학생?\n전학 온 첫날부터 쓰러지다니, 별일이구나."
   school_nurse "겉으로 봤을 땐 큰 문제 없어 보이는데...\n갑자기 의식을 잃다니, 나중에 큰 병원 가서 검사 받아보는 게 어때?"

   "보건 선생님께서는 나에게 약봉투를 건네주셨다."

   school_nurse "여기 약 줄게. 갖고 있어~"

   "나는 약을 받아 주머니에 넣었다."

   scene bg school cafeteria
   with fade
   pause 0.3

   "교실로 돌아갔더니 바로 누리에게 붙잡혀 급식실로 끌려왔다."
   "벌써 점심 시간인건지, \n급식실엔 맛있는 냄새가 퍼지고 학생들도 많았다."

   show nuri at center, doup with dissolve
   
   n "{color=#AAAAAA}[prtname]{/color}, 넌 역시 {color=#FFAEC9}[loop_0_lunch_menu]{/color}지?"
   n "후후... 어떻게 알았는지는 비밀!"

   menu:
      "역시 {color=#FFAEC9}[loop_0_lunch_menu]{/color}지.":
         show nuri smile blush
         n "역시 너라면 그걸 고를 줄 알았어!"
         $ nurilove += 1
      "아니? {color=#FFAEC9}[loop_0_lunch_menu_not_selected]{/color} 먹을건데?":
         show nuri disappointed
         n "어? 그래... 알겠어..."
         "누리가 시무룩해 한다."
         $ nurilove -= 1

   n "그나저나... 몸은 괜찮아?\n아까 쓰러졌다는 얘기를 들었는데..."

   menu:
      "아, 응. 괜찮아. 지금은 멀쩡해":
         n "그래? 그렇담 다행이고... 몸 조심해!\n전학 첫날부터 보건실에 실려가는 사람이 어딨어~!"
         $ nurilove += 1
      "네가 신경 쓸 일이 아니야.":
         n "아... 그래, 알겠어...\n그래도 몸 조심해..."
         $ nurilove -=1

   scene bg school hallway
   with dissolve
   pause 0.3

   "점심을 먹고 반으로 돌아가려던 참이었다.\n그런데. 또 한번 반장, 하늘이에게 붙잡히고 말았다. "
   "내가 없어진 걸 깨달은 누리는 \n고개를 돌려 나를 찾다 하늘이와 눈이 마주치곤 \n조용히 고개를 숙이고 반으로 돌아갔다."

   show hanl at center, doup with dissolve

   h "이제 당신도...\n어느 정도 눈치 챘을거에요.."
   h "궁금한 게 있다면 언제든지 도서관으로 찾아오세요."

   scene bg school classroom afternoon

   show nuri at center, doup with dissolve

   p "누리 너는 하늘이에 대해 잘 알아?"

   n "반장? 음... 엄청 친하진 않아도 \n이것저것 도움을 받고 있긴 하지... 특히 공부에서,"

   n "그보다... 아까 하늘이랑 무슨 얘기 했어?\n하늘이랑 있다가 보건실에 갔다고 하던데..."
   n "{cps=6}...{/cps}정말... 별일 없던 거지?"

   menu:
      "(학생증을 발급받은 것 뿐이라고 말한다.)":
         p "학생증을 발급받은 것 뿐이야."
         n "그랬구나... 응, 별일 아니었다면 다행이야."
      "사실대로 말한다.":
         p "{cps=6}......{/cps}근데 이미 학생증이 내 주머니에 들어있었어.\n그리고 나서, 갑자기 머리가 아파왔고 그대로 쓰러졌어"
         n "뭐야... 학생증이 이미 들어있었다고?\n그리고 쓰러졌다니..."
         $ nurilove +=1

   n "근데, 하늘이 좀 너무하지 않아?\n아침부터 우리 얘기하는데 갑자기 끌고 가질 않나,\n복도에서도 또 갑자기 부르고..."
   n "그냥, 너랑 좀 친해지고 싶었는데,\n계속 방해만 당하는 기분이야..."

   "순간, 이상한 기척이 느껴진다."
   "눈을 감았다 떠보니,\n교실 안의 모든 것이 멈춰있었다."
   "말을 하던 누리도, 주변의 친구들도 전부 멈춰 있고\n나조차도 말이 나오지 않는다."
   "갑자기 눈 앞에 글자가 떠올랐다."
   "{color=#FF0000}WARNING{/color}: '{color=#FFAEC9}누리{/color}' 감정 통제 실패 \n권장 조치: 분리, 세션 초기화"
   "시간이 흘러 모두가 다시 움직이기 시작했다.\n하지만 나는 갑작스러운 상황에 놀라 움직이지 못했다."

   n "{cps=6}...{/cps}어?\n너 괜찮아? 갑자기 왜이렇게 굳어 있어{cps=6}...{/cps}\n혹시... 내가 무슨 말이라도 잘못 했어?"
   n "그게 아니면... 그냥 내가 너무 끼어들었나......"

   "그 순간, 교실 문이 '쾅' 하고 열리며 하늘이 들어왔다."

   show hanl at chrs with moveinright
   
   h "전학생.\n여기서 더 대화를 이어가시면 안 됩니다."

   show nuri angry

   n "또? 또 데려가는 거야?"

   h "누리 당신은 현재 불안정한 상태입니다.\n분리 조치가 필요합니다."

   n "{cps=6}...{/cps}그게 무슨 말이야. \n아까도 갑자기 데려가더니, \n이번엔 또 왜?"
   n "왜 자꾸 나랑 전학생을 떼어놓으려고 하는데...?"

   "그러나 누리가 말을 마치기도 전에 \n하늘이가 조용히 내 팔을 잡은 채\n나를 교실 밖으로 데리고 나갔다."
   "뒤에서 누리의 목소리가 들려왔다."

   n "...너 진짜...!"

   hide nuri with fade

   scene bg school hallway
   with dissolve
   pause 0.3

   show hanl at center, doup with dissolve
   
   h "따라오시죠.\n지금 누리는{cps=6}...{/cps}매우 위험한 상태입니다."
   h "그리고 지금이라면 당신에게 \n진실을 어느 정도 말씀드릴 수 있을지도 모르겠군요."

   "누리가... 위험한 상태라고?\n방금 전 교실에서 본, 그 붉은 경고 메시지 때문인건가?"
   "하늘이는 마치 무언가에 홀린 듯, \n나를 복도 저편으로 이끌었다."
   "우리가 도착한 곳은,"

   scene bg school library afternoon
   with dissolve
   pause 0.3

   "조용한 도서관이었다.\n텅 빈 공간에 우리의 발소리만이 들린다."

   h "잠시만 기다려주시겠습니까."

   "하늘이는 책장 사이,\n어둠이 짙게 깔린 안쪽으로 사라졌다."
   "도서관 안을 좀 둘러볼까......"
   menu:
      "(가만히 있는다.)":
         "가만히 기다려보자"
         $ hanllove += 1
      "(주위를 둘러본다.)":
         "주위를 둘러봤지만, 특별한 건 없었다."
         "...아침에도, 하늘이에게 이끌려 도서관에 왔었지...\n하늘이는 도서관에 있는걸 좋아하는 모양이다..."
         "오가는 사람도 별로 없는걸 보니 \n대화하기 좋은 장소라고 생각하고 있을지도..."
      "(누리에게 돌아가본다.)":
         $ loop_3_wait_for_hanl = False
         $ hanllove -= 1
         $ nurilove += 1

         scene bg school classroom afternoon
         with dissolve
         pause 0.3

         "조심스럽게 교실 문을 열자,\n누리가 고개를 숙인 채 책상에 엎드려 있었다.\n누리의 어깨가 작게 떨리고 있다."
         p "누리야... 괜찮아?"
         "누리는 내 목소리에 놀란 듯 고개를 들었다.\n울고있었던건지, 눈시울이 붉었다."
         n "너... 왜 다시 왔어?\n반장이랑 있는게 더 좋은 거 아니었어?"
         n "반장은... 대체 왜 자꾸 너를 데려가는 거야..."
         menu:
            "(걱정돼서 돌아왔다고 한다.)":
               $ nurilove += 1
               p "누리 네가 걱정돼서...\n사실 난 하늘이가 무슨 말을 하는지도 잘 모르겠어..."
               n "...그래?\n나만 그런 건 아닌가보네...\n아무튼 걱정해줘서 고마워."
            "(침묵한다.)":
               "누리가 다시 고개를 떨궜다."
         "그 순간, 뒤에서 들려오는 작은 발소리와 함꼐\n하늘이의 날카롭고 차가운 목소리가 들려왔다."

         show hanl angry at center, doup with dissolve

         h "{cps=6}......{/cps}여기서 뭐 하시는 거죠?"
         h "당신 때문에,\n누리가 더 불안정해질지도 모릅니다."
         h "{cps=6}......{/cps}따라오시죠."

         "하늘이가 내 팔을 잡았다."

         "누리가 더 불안정해질 수도 있다...\n라는 하늘이의 말에 순순히 하늘이를 따라갔다."

   scene bg school library afternoon
   with dissolve
   pause 0.3

   show hanl at center, doup with dissolve

   if loop_3_wait_for_hanl == True:
      "나는 텅 빈 도서관에서 하늘이가 돌아오기를 기다렸다.\n잠시 후, 하늘이 손에 노트 한 권을 들고 돌아왔다."
      h "기다려주셔서 감사합니다."
   else:
      "나는 하늘이의 손에 이끌려 다시 도서관으로 돌아왔다.\n도서관의 책상 위에는 노트 한 권이 놓여있었다."
         
   h "{cps=6}...혹시{/cps}, 이런 상황이 불편하진 않으신지요."
   menu:
      "(괜찮다고 답한다.)":
         $ hanllove += 1
         p "응, 괜찮아.\n너나 누리나{cps=6}...{/cps} 다 이유가 있어서 그러는 거겠지."
      "(누리에 대해 묻는다.)":
         $ hanllove -= 1
         p "누리가 왜 저러는거야...?"
         h "그건{cps=6}......{/cps}\n전에 말하지 않았었나요?"
         h "{cps=6}...{/cps}당신 때문입니다."
         h "정확한 사정을 지금 말할 수는 없지만,\n곧ㅡ\n당신 스스로 깨닫게 될 겁니다."
   
   h "오늘은 여기까지 하도록 하죠.\n누리도{cps=6}...{/cps} 곧 괜찮아질겁니다."
   h "어쩌면{cps=10}...{/cps}\n당신이 해결할 수 있을지도 모르겠네요."

   "하늘이는 노트를 펼쳐 무언가를 열심히 쓰기 시작했다.\n무표정하지만 눈가는 미세하게 떨리고 있었다."

   "그런 하늘이를 바라보다,\n눈을 깜빡였더니,{p}눈 앞이 깜깜해지고 말았다."

   jump interlude