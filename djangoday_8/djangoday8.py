# lst=[64,25,10,22,11]
#
# for y in range(len(lst)-1):
#
#     for i in range(y,len(lst)):
#         if min(lst[x:])==lst[i]:
#             lst[i],lst[x]=lst[x],lst[i]
#             x+=1
#
# print(lst)

# for i in range(len(lst)-1):
#     min_value=lst[i]
#     for j in range(i,len(lst)):
#         if min_value>lst[j]:
#             min_value=lst[j]
#             min_idx=j
#     if(lst[i]>min_value):
#         lst[i],lst[min_idx]=lst[min_idx],lst[i]
# print(lst)

# sumlst=[[4,4,3,2,1],
# [2,2,1,6,5],
# [3,5,4,6,7],
# [4,2,5,9,7],
# [8,1,9,5,6]]
# sumlst=[]
# with open("sum_arr.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     numbers = line.strip().split()
#     numbers = tuple(map(int, numbers))
#     sumlst.append(numbers)
# l=len(sumlst)
# max_sumhang=0
# for i in range(l):
#     sumhang = 0
#     for j in range(l):
#         sumhang+=sumlst[i][j]
#     if sumhang>max_sumhang:
#         max_sumhang=sumhang
# max_sumyeol=0
# for x in range(l):
#     sumyeol = 0
#     for y in range(l):
#         sumyeol+=sumlst[y][x]
#     if sumyeol>max_sumyeol:
#         max_sumyeol=sumyeol
# sumslash=0
# for a in range(l):
#         sumslash+=sumlst[a][l-a-1]
#
# sumbackslash=0
# for c in range(l):
#     sumbackslash+=sumlst[c][c]
#
# maxlst=[max_sumhang,max_sumyeol,sumslash,sumbackslash]
# res=0
# for i in maxlst:
#     if i>res:
#         res=i
# print(max_sumhang,max_sumyeol,sumslash,sumbackslash)
# print(res)
import re
user_str="Start eating well with these eight tips for healthy eating, which cover the basics of a healthy diet and good nutrition."
mystr=re.findall("ti",user_str)
print(len(mystr))