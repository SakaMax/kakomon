#https://atcoder.jp/contests/abc067/tasks/abc067_b

N, K = map(int, input().split())
L = [l for l in map(int, input().split())]

L.sort(reverse=True)
print(sum(L[:K]))