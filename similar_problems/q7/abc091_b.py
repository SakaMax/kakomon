#https://atcoder.jp/contests/abc091/tasks/abc091_b
d = dict()

N = int(input())
for _ in range(N):
    s = input()
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1

M = int(input())
for _ in range(M):
    t = input()
    if t in d.keys():
        d[t] -= 1
    else:
        d[t] = -1

ans = max(max(d.values()), 0)

print(ans)