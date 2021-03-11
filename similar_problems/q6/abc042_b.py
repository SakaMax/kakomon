#https://atcoder.jp/contests/abc042/tasks/abc042_b

N, L = map(int, input().split())
S = [input() for _ in range(N)]

S.sort(key=lambda x: [ord(c) for c in x])
print(''.join(S))