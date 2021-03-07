#https://atcoder.jp/contests/abc095/tasks/abc095_b

N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

ans = 0

# must
ans = N
remain_powder = X - sum(M)

# additional
ans += remain_powder//min(M)

print(ans)