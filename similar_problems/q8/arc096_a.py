#https://atcoder.jp/contests/arc096/tasks/arc096_a
A, B, C, X, Y = map(int, input().split())
min_cost = float('inf')
for ab_pizza in range(0, 2*10**5+1):
    a_pizza = max(X - ab_pizza//2, 0)
    b_pizza = max(Y - ab_pizza//2, 0)
    cost = a_pizza*A + b_pizza*B + ab_pizza*C
    if cost<min_cost:
        min_cost = cost

print(min_cost)