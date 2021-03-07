#https://atcoder.jp/contests/abc175/tasks/abc175_b

N = int(input())
L = [int(l) for l in input().split()]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            #print(f"(i,j,k) = ({i+1},{j+1},{k+1}), L={L[i]}, {L[j]}, {L[k]}")
            if L[i] == L[j] or L[i] == L[k] or L[j] == L[k]:
                #print("continue")
                continue
            a, b, c = L[i], L[j], L[k]
            if a < (b+c) and b < (a+c) and c < (a+b):
                ans += 1
print(ans)
            