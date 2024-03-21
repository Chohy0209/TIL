# import math
#
# m,n=map(int, input("두 수를 입력하세요").split())
# total_page=math.ceil(m/n)
# print(m, n, total_page)

user_alp=input("알파벳문장을 써주세요")
user_num=int(input("n값을 입력하세요"))
pw=[]
for char in user_alp:
    ascalp=ord(char)
    if char ==" ":
        pw.append(char)
    elif ascalp+user_num<123:
        pw.append(chr(ascalp+user_num))
    elif ascalp+user_num >123:
        pw.append(chr(ascalp+user_num-26))

    else:
        pw.append(char)

print("".join(pw))
