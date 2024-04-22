import random

#버블정렬
# soo = [55, 7, 78, 12, 42]
#
#
# for i in range(len(soo)-1):
#     for j in range(0, len(soo)-1-i):
#         if soo[j] > soo[j + 1]:
#             soo[j], soo[j + 1] = soo[j + 1], soo[j]
#             print(soo)
# print(soo)
# 카운터정렬
# lst = [0, 4, 1, 3, 1, 2, 4, 1]
# count_lst = []
#
# for i in range(5):
#     count_lst.append(0)
#
# for i in lst:
#     count_lst[i] = count_lst[i] + 1
# print(count_lst)
#
# for i, data in enumerate([1, 3, 1, 1, 2]):
#     print(i, data)
#
# import random
# lst=[[random.randint(1,10)for y in range(5)]for x in range(5)]
# res=[]
#
#
# for i in range(5):
#     for j in range(5):
#         try:
#             a=abs(lst[j+1][i]-lst[j][i])
#         except:
#             a=0
#         try:
#             b=abs(lst[j-1][i]-lst[j][i])
#         except:
#             b=0
#         try:
#             c=abs(lst[j][i-1]-lst[j][i])
#         except:
#             c=0
#         try:
#             d=abs(lst[j][i+1]-lst[j][i])
#         except:
#             d=0
#         for k in range(5):
#             for p in range(5):
#                 res.append(a+b+c+d)
# print(res)
# import random
# lst = [[random.randint(1, 10) for y in range(5)] for x in range(5)]
# row=[]
# res = []
#
# for i in range(5):
#     for j in range(5):
#         row = []
#         try:
#             a = abs(lst[j + 1][i] - lst[j][i])
#         except:
#             a = 0
#         try:
#             b = abs(lst[j - 1][i] - lst[j][i])
#         except:
#             b = 0
#         try:
#             c = abs(lst[j][i - 1] - lst[j][i])
#         except:
#             c = 0
#         try:
#             d = abs(lst[j][i + 1] - lst[j][i])
#         except:
#             d = 0
#         row.append(a + b + c + d)
#         res.append(row)





# import random
#
# lst = [[random.randint(1, 10) for y in range(5)] for x in range(5)]
# res = []
#
# for i in range(5):
#     row = []
#     for j in range(5):
#         try:
#             a = abs(lst[j + 1][i] - lst[j][i])
#         except:
#             a = 0
#         try:
#             b = abs(lst[j - 1][i] - lst[j][i])
#         except:
#             b = 0
#         try:
#             c = abs(lst[j][i - 1] - lst[j][i])
#         except:
#             c = 0
#         try:
#             d = abs(lst[j][i + 1] - lst[j][i])
#         except:
#             d = 0
#         row.append(a + b + c + d)
#     res.append(row)
#
# print(res)
import random
soo=list(range(1,26))
lst=[]
for i in range(5):
    row=[]
    for j in range(5):
        a=random.choice(soo)
        soo.remove(a)
        row.append(a)
    lst.append(row)
for x in range(4):
    for y in range(4-x-1):
        if soo[x][y]>soo[x][y+1]:
            soo[x][y],soo[x][y+1]=soo[x][y+1],soo[x][y]

