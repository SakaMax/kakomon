# https://atcoder.jp/contests/abc088/tasks/abc088_b
N = int(input())
cards = [int(a) for a in input().split()]

cards.sort(reverse=True)
turn_of_alice = True
alice = 0
bob = 0
for a in cards:
    if turn_of_alice:
        alice += a
        #print(f"alice got {a}: total {alice}")
    else:
        bob += a
        #print(f"bob got {a}: total {bob}")

    turn_of_alice = not turn_of_alice
print(alice-bob)