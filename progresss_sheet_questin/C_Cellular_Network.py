n,m=map(int,input().split())
cities=list(map(int,input().split()))
laterns=list(map(int,input().split()))
final=0
for ct in cities:
    min_leng=abs(ct-laterns[0])
    for i in range(1,len(laterns)):
         tempo=abs(ct-laterns[i])
         if tempo<= min_leng:
              min_leng=tempo
         else:
             break
    final=max(final,min_leng)
print(final)
