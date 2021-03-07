#https://atcoder.jp/contests/abc133/tasks/abc133_b
N, D = map(int, input().split())
X = [[x for x in map(int, input().split())] for _ in range(N)]

# square numbers within 40^2 * dim.
sq = []
i = 0
while True:
    i += 1
    sq.append(i**2)
    if i**2 > (40**2)*D:
        break
#print(N, D, X,sq)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        ss = sum(map(lambda a,b : (a-b)**2, X[i], X[j]))
        #print(f"i={i}, j={j}, ss(i,j)={ss}")
        if ss in sq:
            ans += 1
print(ans)