#https://atcoder.jp/contests/abc144/tasks/abc144_b
N = int(input())
kuku = []

for dan in range(1,10):
    for retu in range(1,10):
        kuku.append(dan * retu)

print("Yes" if N in kuku else "No")