import re
text=open("readtext.txt", "r")
mytext=text.read()
splitText=re.split('[,. ]+',mytext)
worldlist=[]
for i in splitText:
    if [i,splitText.count(i)] not in worldlist:
        worldlist.append([i, splitText.count(i)])
swl=sorted(worldlist,key=lambda x:x[1],reverse=True)
for x,y in swl[0:10]:
    print(x,y)
text.close()