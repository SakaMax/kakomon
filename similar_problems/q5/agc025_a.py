#https://atcoder.jp/contests/agc025/tasks/agc025_a
def sum_digit(n):
    s = 0
    while True:
        d = n%10
        s += d
        n = n//10
        if n == 0:
            return s

N = int(input())

ans = 10**6
for A in range(1,N):
    B = N - A
    ssd = sum_digit(A) + sum_digit(B)
    if ssd  < ans:
        ans = ssd
print(ans) 