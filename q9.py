# https://atcoder.jp/contests/abc049/tasks/arc065_a
S = input()
candidate = ["dream", "dreamer", "erase", "eraser"]

S = ''.join(reversed(S))
candidate = [''.join(reversed(c)) for c in candidate]
#print(S)
#print(candidate)

head = 0
while True:
    for c in candidate:
        l = len(c)
        if S[head:min(head+l, len(S))] == c:
            #print(f"match {c}: head {head} -> {head+l}")
            head += l
            break
    else:
        if head == len(S):
            print("YES")
        else:
            print("NO")
        break
        