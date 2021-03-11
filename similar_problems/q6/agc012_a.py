#https://atcoder.jp/contests/agc012/tasks/agc012_a
N = int(input())
A = [int(a) for a in input().split()]

high = []; mid = []; low = []
A.sort()
#print(A)
# for _ in range(N):
#     h = A.pop()
#     m = A.pop()
#     l = A.pop(0)
#     #print(f"{h}, {m}, {l}")
#     high.append(h)
#     mid.append(m)
#     low.append(l)

mid = A[N::2]

print(sum(mid))