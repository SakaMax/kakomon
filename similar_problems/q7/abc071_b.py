#https://atcoder.jp/contests/abc071/tasks/abc071_b

L_SET = set("abcdefghijklmnopqrstuvwxyz")
S = set(input())

ans_set = L_SET - S
if ans_set:
    print(sorted(ans_set)[0])
else:
    print("None")