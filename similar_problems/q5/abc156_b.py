#https://atcoder.jp/contests/abc156/tasks/abc156_b

N, K = map(int, input().split())

n = []
while N > 0:
    n.append(N % K)
    N = N // K
else:
    n.reverse()
#print(n)
print(len(n))