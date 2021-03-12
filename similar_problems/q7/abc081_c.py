#https://atcoder.jp/contests/abc081/tasks/arc086_a

N, K = map(int, input().split())
A = [int(a) for a in input().split()]
A_d = dict()

for a in A:
    if a in A_d.keys():
        A_d[a] += 1
    else:
        A_d[a] = 1

excess = len(A_d.keys()) - K
if excess <= 0:
    print(0)
else:
    A_count = sorted(A_d.values())
    print(sum(A_count[0:excess]))