n_cases = int(input())
n_ricardo, n_vincent = 0, 0
buffer = 0
for case in range(0, n_cases):
    n_ricardo, n_vincent = map(int, input().split())
    while (n_ricardo % n_vincent) != 0:
        buffer = n_ricardo % n_vincent
        n_ricardo = n_vincent
        n_vincent = buffer
    print(n_vincent)
