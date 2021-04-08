#https://atcoder.jp/contests/abc088/tasks/abc088_c

c11, c12, c13 = map(int, input().split())
c21, c22, c23 = map(int, input().split())
c31, c32, c33 = map(int, input().split())
found = False

for a1 in range(0, 101):
    for a2 in range(0, 101):
        for a3 in range(0, 101):
            # candidate
            b1 = c11 - a1
            b2 = c12 - a1
            b3 = c13 - a1
            
            if (a2 + b1 == c21) and \
                (a2 + b2 == c22) and \
                (a2 + b3 == c23) and \
                (a3 + b1 == c31) and \
                (a3 + b2 == c32) and \
                (a3 + b3 == c33):
                found = True
                break
        if found: break
    if found: break

print("Yes" if found else "No")