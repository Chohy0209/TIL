usertry=int(input('몇회를 실행할까요?'))
userinput=input('계산식을 써주세요')

if '/' in userinput:
    soo1=int(userinput.split('/')[0])
    soo2=int(userinput.split('/')[1])
    for i in range(usertry):
        soo1=soo1 / int(soo2)
        print(i+1,"회:",soo1)
elif '+' in userinput:
    soo1=int(userinput.split('+')[0])
    soo2=int(userinput.split('+')[1])
    for i in range(usertry):
        soo1=soo1 + int(soo2)
        print(i+1,"회:",soo1)
elif '-' in userinput:
    soo1=int(userinput.split('-')[0])
    soo2=int(userinput.split('-')[1])
    for i in range(usertry):
        soo1=soo1 - int(soo2)
        print(i+1,"회:",soo1)
elif '*' in userinput:
    soo1=int(userinput.split('*')[0])
    soo2=int(userinput.split('*')[1])
    for i in range(usertry):
        soo1=soo1 * int(soo2)
        print(i+1,'회:',soo1)
else:
    print("사칙연산 수식만 입력해주세요")



