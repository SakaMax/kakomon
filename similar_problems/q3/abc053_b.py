#https://atcoder.jp/contests/abc053/tasks/abc053_b
import re
s = input()
print(len(re.search(r"(A.*Z)", s).group(1)))