label loop_3:
   scene bg school classroom morning
   with fade

   "......여긴?{p}또... 교실인 건가?"
   "......또?{p}내가 지금... 뭘 생각한 거지?\n전학 첫날이라 긴장했나......"

   show nuri smile at center, shadow
   with dissolve

   "나는 고개를 돌려 누리가 있는 쪽을 바라보았다."
   "누리는 뭔가 하려다 살짝 당황한 듯, 멈칫하며 말을 걸었다."

   show nuri at light

   n "오~ 전학생! 감이 좋은걸~\n나는 {color=#FFAEC9}누리{/color}야.\n전학생은 이름이 뭐야?"

   menu:
      "(누리의 인사를 무시하고 자리에서 일어난다)":
         "그러자 누리가 엄청난 괴력으로 나를 다시 자리에 앉혔다."
      "(아무 말이나 한다)":
         p "오늘 날씨가 참 좋네, 그렇지 않아?"
         "누리는 멈칫했지만 곧 웃으며 반응했다."
   
   show nuri at right
   with move

   n "{color=#AAAAAA}[prtname]{/color}이구나~ 좋은 이름인걸!"

   "이게... 뭐지?{p}그러고보니 나도 자연스럽게 누리가 있던 곳을 쳐다봤어..."
   
   show hanl at left
   with moveinleft

   "......응?{p}어느샌가 내 옆에는 반장인 하늘이가 와 있었고,\n하늘이는 내 팔을 잡은 채로 아무 말 없이 도서관 쪽으로 나를 끌고 갔다."

   scene bg school library morning
   with fade

   show hanl
   with dissolve

   h "당신... 당신 때문이에요... 알고 있나요?{w=3.0}{nw}"
   h "주머니를 확인해봐요."

   "나는 주머니를 더듬어보았다. 그러자 작은 플라스틱 카드가 손에 잡혔다."
   "{cps=6}......{/cps}학생증이 들어 있었다."

   h "학생증은 도서관에서만 만들 수 있어요.\n그런데 당신이 이미 가지고 있다는 건... 역시——"

   # TODO: it would be nice to have a chromatic abberation effect here.

   p "{cps=10}......아파... 숨이... 안 쉬어져......{/cps}{w=1.0}{nw}" with vpunch
   
   "나는 그대로 무너져 쓰러졌다."

   scene bg school nurseoffice
   with fade

   p "......아으... 머리야......"

   school_nurse "일어났니, 전학생?\n전학 온 첫날부터 쓰러지다니, 별일이구나."
   school_nurse "겉으로 봤을 땐 큰 문제 없어 보이는데...\n갑자기 의식을 잃다니, 나중에 큰 병원 가서 검사 받아보는 게 어때?"

   "보건 선생님께서는 나에게 약봉투를 건네주셨다."

   school_nurse "여기 약 줄게. 갖고 있어~"

   "나는 약을 받아 주머니에 넣었다."