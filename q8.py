# https://atcoder.jp/contests/abc085/tasks/abc085_c
N, Y = (int(i) for i in input().split())
found = False
for yukichi in range(0,N+1):
    for higuchi in range(0,N+1-yukichi):
        if yukichi * 10000 + higuchi * 5000 + (N-yukichi-higuchi) * 1000 == Y:
            print(yukichi, higuchi, (N-yukichi-higuchi))
            found = True
            break
    if found:
        break
else:
    print(-1,-1,-1)