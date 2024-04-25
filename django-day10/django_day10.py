# import re
# def newname(new_id):
#     word=[]
#     for a in new_id:
#         if a.isupper():
#             word.append(a.lower())
#     word2=[]
#     for b in word:
#         if b.islower() or b=="-" or b=="_" or b==".":
#             word2.append(b)
#     if re.findall("..", "".join(word2)):
#
#         word2[word2.index("..")]="."
#     if word2[0]==".":
#         del(word2[0])
#     if word2[-1] == ".":
#         del(word2[-1])
#     if not word2:
#         word2.append("a")
#     if len(word2)>=16:
#         del(word2[16:])
#     if len(word2)<=2:
#         if len(word2)==1:
#             word2.append(word2[0])
#             word2.append(word2[0])
#         elif len(word2)==2:
#             word2.append(word2[0])
#     return word2
#
#
# new_id="...!@BaT#*..y.abcdefghijklm"
# kakaoid=newname(new_id)
# print("".join(kakaoid))
import re


def newname(new_id):
    word = []
    for a in new_id:
        if a.isupper():
            word.append(a.lower())
        else:
            word.append(a)
    word2 = []
    for b in word:
        if b.islower() or b == "-" or b == "_" or b == ".":
            word2.append(b)

    # 연속된 문자열을 하나의 문자로 대체
    word2 = re.sub(r"\.{2,}", ".", "".join(word2))
    word3=[]
    for y in word2:
        word3.append(y)

    if word3[0] == ".":
        del word3[0]
    if word3[-1] == ".":
        del word3[-1]
    if not word3:
        word3.append("a")
    if len(word3) >= 16:
        del word3[15:]
    if len(word3) <= 2:
        if len(word3) == 1:
            word3.append(word3[0])
            word3.append(word3[0])
        elif len(word3) == 2:
            word3.append(word3[0])
    return word3


new_id = "abcdefghijklmn.p"
kakaoid = newname(new_id)
print("".join(kakaoid))
