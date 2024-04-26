from multiprocessing.forkserver import read_signed


# def file(number):
#     return number+".txt"
#
# for i in range(1,11):
#     print(file(str(i)))

# def soo(l,r):
#     res=[]
#     for j in range(l,r+1):
#         res.append(j)
#         for k in str(j):
#             if k != "5" and k !="0":
#                 del res[res.index(j)]
#                 break
#     if res:
#         return res
#     else:
#         return [-1]
#
#
#
# print(soo(5,555))
#
# def solution(my_string):
#     res = []
#     for i in my_string:
#
#         if i =="a" or i =="e" or i=="i" or i=="o" or i=="u":
#             continue
#         else:
#             res.append(i)
#     return res
# my_string="nice to meet you"
# print("".join(solution(my_string)))

quiz=["19 - -6 = 25", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]

def solution(quiz):
    res=[]
    for i in quiz: #"19 - 6 = 13"
        a,b=i.split('=')
        a1=a.split(' ')
        if a1[1]=="-":
            if int(a1[0])-int(a1[2])==int(b):
                res.append("O")
            else:
                res.append("X")
        if a1[1]=="+":
            if int(a1[0])+int(a1[2])==int(b):
                res.append("O")
            else:
                res.append("X")
    return res


print(solution(quiz))