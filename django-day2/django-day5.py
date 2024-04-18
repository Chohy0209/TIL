# s = 'baabaa'
#
#
# def solution(s):
#     slst = []
#
#     for i in s:
#         slst.append(i)
#
#
#     def dels(slst):
#         result = 0
#
#         for i in range(len(slst)):
#
#
#             if slst==[]:
#                 result = 1
#                 return result
#             elif slst!=[] and i==len(slst)-1:
#                 result = 0
#                 return result
#             elif slst[i] == slst[i + 1]:
#                 slst.pop(i)
#                 slst.pop(i)
#                 return dels(slst)
#
#     res=dels(slst)
#     return res
# res = solution(s)
# print(res)
def solution(s):
    slst = []

    for i in s:
        slst.append(i)


    def dels(slst):
        result=0
        for i in range(len(slst)):
            if slst==[]:  # 먼저 리스트가 비어 있는지 확인
                result = 1
                return result
            elif i==len(slst)-1:  # 인덱스가 리스트의 마지막이면
                result = 0
                return result
            elif slst[i] == slst[i + 1]:
                slst.pop(i)
                slst.pop(i)
                return dels(slst)  # 재귀 호출을 통해 다시 함수 실행

    res=dels(slst)
    return res

s='baabaa'
res = solution(s)
print(res)
