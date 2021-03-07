#https://atcoder.jp/contests/abc113/tasks/abc113_b

def temp(T):
    "平均気温の関数"
    return lambda x: T - x * 0.006

N = int(input())
T, A = [i for i in map(int, input().split())]
H = [i for i in map(int, input().split())]


H_temp = [h for h in map(temp(T), H)]
fav_temp = [abs(h-A) for h in H_temp]
print(fav_temp.index(min(fav_temp))+1)
