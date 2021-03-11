#https://atcoder.jp/contests/abc047/tasks/abc047_b

def nurie(space, W, H, x_cond, y_cond):
    for h in range(H):
        for w in range(W):
            if x_cond(w) and y_cond(h):
                space[h][w] += 1
    return space

W, H, N = map(int, input().split())

space = [[0 for _ in range(W)] for _ in range(H)]

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        space = nurie(space, W, H, lambda w: w < x, lambda h: True)
    elif a == 2:
        space = nurie(space, W, H, lambda w: w >= x, lambda h: True)
    elif a == 3:
        space = nurie(space, W, H, lambda w: True, lambda h: h < y)
    elif a == 4:
        space = nurie(space, W, H, lambda w: True, lambda h: h >= y)

ans = 0
for h in reversed(space):
    for w in h:
        ans += 1 if w == 0 else 0
print(ans)