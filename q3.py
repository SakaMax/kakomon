# https://atcoder.jp/contests/abc081/tasks/abc081_b

N = int(input())
board = [int(a) for a in input().split()]
ans = 0

while True:
    if any([a%2 for a in board]):
        break
    ans += 1
    board = [a//2 for a in board]

print(ans)