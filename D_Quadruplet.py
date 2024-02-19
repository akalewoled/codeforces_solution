
a,B=list(map(int,input().split()))

array=list(map(int,input().split()))

from itertools import combinations
lists=[i for i in range(a)]
for combo in combinations(lists, 4):
    a=array[combo[0]]
    b=array[combo[1]]
    c=array[combo[2]]
    d=array[combo[3]]
    if a+b+c+d==B:
        print(combo[0]+1,combo[1]+1,combo[2]+1,combo[3]+1)
        break
       
        