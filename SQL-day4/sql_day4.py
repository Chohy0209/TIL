# ["i", "drink", "water"] ["want", "to"] ["i", "want", "to", "drink", "water"] "Yes"
#
# ["i", "water", "drink"] ["want", "to"] ["i", "want", "to", "drink", "water"] "No"

# ["i", "water", "drink"] ["want", "to"] ["i", "want", "to", "drink", "water"] "No"
cards1=["i", "drink", "water"]
cards2=["want", "to"]
goal=["i", "want", "to", "drink", "water"]
testgoal=[]

for i in range(len(goal)): #goal 의 총 길이 만큼 실행
    if len(cards1)>0: #카드 1팩에 카드가 남아있을때
        if goal[i] == cards1[0]: #첫번째 카드와 목적 카드가 같다면 추출
            testgoal.append(cards1.pop(0))

        elif len(cards2)>0: #다르다면 카드팩 2에 첫번째 카드에서 확인 후 있다면 추출
            if goal[i] == cards2[0]:
                testgoal.append(cards2.pop(0))
        else: #둘다 없을시 아직 카드팩에 카드가 남아있으면 차례대로 하나씩 추출시도
            if len(cards1)>0:

                cards1.pop(0)
            elif len(cards2)>0:
                cards2.pop(0)

if testgoal==goal:
    print(testgoal,'yes')
else:
    print(testgoal,'no')