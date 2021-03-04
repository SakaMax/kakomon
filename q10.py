# https://atcoder.jp/contests/abc086/tasks/arc089_a

def distance(x0, y0, x1, y1) -> int:
    return abs(x1-x0) + abs(y1-y0)

N = int(input())
site = [(0,0,0)]
for _ in range(N):
    site.append(tuple(int(elem) for elem in input().split()))

for i in range(N):
    prev = site[i]
    next = site[i+1]
    plan = next[0] - prev[0]
    dist = distance(prev[1], prev[2], next[1], next[2])
    if plan == dist or (plan > dist and (plan-dist)%2 == 0):
        pass
    else:
        print("No")
        break
else:
    print("Yes")