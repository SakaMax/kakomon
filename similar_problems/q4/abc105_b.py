#https://atcoder.jp/contests/abc105/tasks/abc105_b

N = int(input())
OK = False

for c in range(100):
    for d in range(100):
        if (c>0 or d>0) and 4*c + 7*d == N:
            #print(f"c={c}, d={d}, 4c+7d={4*c+7*d}, N={N}")
            OK = True
            break
    if OK:
        break

print("Yes" if OK else "No")