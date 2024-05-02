userlog="""4
Baha enter
Askar enter
Baha leave
Artem enter"""
userlog=userlog.split('\n')
res=[]
for i in range(1,len(userlog)):
    x=userlog[i].split()
    if x[1]=="enter" and userlog.count(x[0]+" "+"enter")>userlog.count(x[0]+" "+"leave"):
        res.append(x[0])
print(res)