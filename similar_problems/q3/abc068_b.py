#https://atcoder.jp/contests/abc068/tasks/abc068_b
N = int(input())

def div2(i: int) -> int:
    # "2で割れる回数"
    for j in range(8):
        if i%pow(2,j):
            return j-1

ans, maxdiv = (1,0)
for n in range(1,N+1):
    d = div2(n)
    if maxdiv < d:
        ans, maxdiv = (n, d)
print(ans)