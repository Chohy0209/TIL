names = '이유덕,이재영,전이헌'.split(',')
kim = 0
lee = 0
for i in names: #break point(중단점,디버깅 시작점)
    if i[0]=='김':
        kim += 1
    elif i[0] == '이':

        lee += 1
print(kim)
print(lee)
#오류(bug,error):문법(syntex), 논리
#논리오류는 디버깅(debugging)과정을 수행하여 해결
# 디버그 모드에서는 변수값을 보여주며 처리순서에 따라 한줄씩 실행하며 변수값의 변화등을 보여줌