N, S = map(int, input().split())
min = S
for mov in range(0, N):
    movimento = int(input())
    S += movimento
    if S < min:
        min = S
print(min)