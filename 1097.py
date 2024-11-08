I, J = 1, 7
for n, i in enumerate(range(0, 5)):
    for j in range(0, 3):
        print(f'I={I} J={J}')
        J -= 1
    J += 5
    I += 2