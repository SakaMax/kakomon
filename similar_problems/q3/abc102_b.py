#https://atcoder.jp/contests/abc102/tasks/abc102_b
N = int(input())
A = [a for a in map(int, input().split())]

print(max(A)-min(A))