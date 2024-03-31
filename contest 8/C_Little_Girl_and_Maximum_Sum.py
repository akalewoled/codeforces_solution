n, q = map(int, input().split())
p=list(map(int, input().split()))
r = [0] * (n+1)
for _ in range(q):
    x, y = map(int, input().split())
    r[x-1]+=1
    r[y]-=1
for i in range (1,n):
   r[i]=r[i-1]+r[i]
r = sorted(r)
p = sorted(p)
q = [0] * n
for i in range(0, n):
    q[i] = r[i+1] * p[i]
print(sum(q))
Dear Admissions Committee,

Fourth-year Bahir Dar University software engineering student, Fikiremariyam Babu, here. I'm passionate about [specific area]. My skills in [mention 2 relevant skills] and achievements in [mention relevant project/coursework] make me a strong candidate for [Program Name].

Find my CV and a motivational video attached. Thank you for considering my application.

Sincerely,