""" 
to be optimum the the clever student should team up with the low level student 
"""
no_of_students=int(input())
skills=list(map(int,input().split()))
skills.sort()   # sorting based on theier educational level
no_of_question=0
for i in range (0,t,2):
    no_of_question=skills[i+1]-skills[i]+no_of_question
print (no_of_question)

t=int(input())
ar=list(map(int,input().split()))
ar.sort()
g=0
for i in range (0,t,2):
    g=ar[i+1]-ar[i]+g
print (g)