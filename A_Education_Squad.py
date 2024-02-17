"""
we are going to create 8 arrays  with the eith winniying possibilites 
then use count function to tell how many people can win
"""
from collections import Counter
a=list(input().strip())
b=list(input().strip())
c=list(input().strip())

win1=a
win2=b
win3=c
win4=[a[0],b[0],c[0]]
win5=[a[1],b[1],c[1]]
win6=[a[2],b[2],c[2]]
win7=[a[0],b[1],c[2]]
win8=[a[2],b[1],c[1]]
winrate=[set(win1),set(win2),set(win3),set(win4),set(win5),set(win6),set(win7),set(win8)]
alone=0
teamup=0
for i in winrate:
    if len(i)==1:
        alone+=1
    elif len(i)==2:
        teamup+=1
print(alone)
print(teamup)
    
    