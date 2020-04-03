k,n = map(int,input().split())
a=[]
for i in range(k):
    b=list(map(int,input().split()))[:n]
    for j in b:
        a.append(j)
a.sort()
print(*a)
