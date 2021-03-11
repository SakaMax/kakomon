#https://atcoder.jp/contests/abc061/tasks/abc061_b
N, M = map(int, input().split())
L = {i+1: 0 for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    L[a] += 1; L[b] += 1

for i in range(N):
    print(L[i+1])
