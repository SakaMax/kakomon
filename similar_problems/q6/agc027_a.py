#https://atcoder.jp/contests/agc027/tasks/agc027_a

N, x = map(int, input().split())
A = [int(a) for a in input().split()]

ans = 0
A.sort()

given = [0 for _ in range(len(A))]

for i in range(len(A)):
    g  = min(A[i], x)
    given[i] = g
    x -= g
else:
    if x:
        given[-1] += x

for a, g in zip(A, given):
    if a == g:
        ans += 1

print(ans)
