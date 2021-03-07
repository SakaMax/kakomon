#https://atcoder.jp/contests/abc090/tasks/abc090_b

def palindrome(a):
    digit = []
    for _ in range(5):
        digit.append(a%10)
        a = a//10
    #print(digit)
    if digit[0] == digit[4] and digit[1] == digit[3]:
        return True
    else:
        return False

A, B = map(int, input().split())

ans = 0
for n in range(A, B+1):
    if palindrome(n):
        ans += 1
print(ans)