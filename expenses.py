t = int(input())
for i in range(t):
    q,p = map(int,input().split())
    if q<1000:
        print(q*p)
    else:
        print((q*p)-0.1*(q*p))
