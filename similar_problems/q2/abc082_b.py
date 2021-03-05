def dict_lt(S,T):
    "validate s<t in dict. order."
    for s, t in zip(S,T):
        if s<t:
            return True
        elif s==t:
            continue
        else:
            return False
    else:
        if len(S)<len(T):
            return True
        else:
            return False

s = sorted(map(ord, input()), reverse=False)
t = sorted(map(ord, input()), reverse=True)
print("Yes" if dict_lt(s,t) else "No")