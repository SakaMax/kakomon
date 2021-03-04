# https://atcoder.jp/contests/abc083/tasks/abc083_b
N, A, B = map(int, input().split(' '))
ans = 0
for i in range(1,N+1):
    s = sum([int(c) for c in str(i)])
    #print(i, s, A<=s<=B)
    if A <= s <= B:
        ans += i

print(ans)