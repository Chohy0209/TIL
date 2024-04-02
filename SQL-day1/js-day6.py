# def isBalanced(s):
#     n=0
#     for i in range(len(s)):
#         n+=(1 if s[i]=='(' else-1)
#         if n<0:
#             return False
#     return True if n==0 else False
#2.
# import datetime
# # print(datetime.datetime(2024, 4, 2))
# # today=datetime.datetime(2024, 4, 2)
# # print(today.year)
# # print(today.weekday())#0:월요일, 1:화요, ...
# # print(today.day)#2일
# # print(today.month) #4월
# #매월 1일이 일요일인 경우는 총 몇 번
# #1900년 1월 1일 ~ 1999년 12월 31일
# s=datetime.datetime(1900, 1, 1)
# d=datetime.timedelta(days=1)
# print(d)
# cnt=0
# while s.year<2000:
#     if s.day==1 and s.weekday()==6:
#         cnt+=1
#     s+=d
# print(cnt)
# print(datetime.date.today()) #2024-04-02
# today=datetime.date.today()
# diff_days=datetime.timedelta(days=100)
# print(diff_days)
# print(diff_days+today)
# print(today-diff_days)
#3.
# from collections import Counter #카운터 함수 많이쓰임
# with open('readtext.txt','r') as f:
#     words=[w.strip(",.") for w in f.read().split()]
#     for w,c in Counter(words).most_common(10): #카운터 함수는 자동으로 빈도수에 따라 정렬해주고 제일 많이 나온 10개를 추출
#         print(w,c)


#2.
from collections import Counter
userNum=[26,37,26,37,91]
mostnum=Counter(userNum).most_common()
Numlist=[]
for j in mostnum:
    Numlist.append(list(j))
if len(Numlist) > 1 and Numlist[0][1] == Numlist[-1][1]:
    print("없습니다")
else:
    num=[]
    count=0
    x=[]
    for i,j in mostnum:
        if j>=count:
            num.append([i,j])
            count=j
    for i in range(len(num)):
        x.append(num[i][0])
    print(" ".join(map(str,x)))

