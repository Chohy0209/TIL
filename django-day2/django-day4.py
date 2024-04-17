
# chicken=1081
# def solution(chicken):
#     coo = chicken
#     ser=0
#     while coo>=10:
#         serchicken=coo//10
#         ser+=serchicken
#         coo=serchicken+coo%10
#     return ser
# res=solution(chicken)
# print(res)

# chicken=1081
# import math
# def solution(chicken):
#     x = len(str(chicken)) - 1 + len(str(chicken)) - 2
#     serchicken=chicken
#     serchic=0
#     for i in range(x):
#         serchicken = serchicken * 0.1
#         serchic+=serchicken
#     return serchic
# print(math.trunc(solution(chicken)))
# chicken=19925
#
# def solution(chicken):
#     return int(chicken*0.111111)
# print(solution(chicken))

dic=["def", "dww", "dzx", "loveaw"]
spell=["z", "d", "x"]
new=[]
for i in dic:
    for j in spell:
        if j not in i:
            new.append(i)
            break
if new==dic:
    print(2)
else:
    print(1)